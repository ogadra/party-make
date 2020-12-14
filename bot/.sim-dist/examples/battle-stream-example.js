"use strict";/**
 * Battle Stream Example
 * Pokemon Showdown - http://pokemonshowdown.com/
 *
 * Example of how to create AIs battling against each other.
 * Run this using `node build && node .sim-dist/examples/battle-stream-example`.
 *
 * @license MIT
 * @author Guangcong Luo <guangcongluo@gmail.com>
 */


var _dex = require('../dex');
var _battlestream = require('../battle-stream');


// var _randomplayerai = require('../tools/random-player-ai');

/*********************************************************************
 * Run AI
 *********************************************************************/

const streams = _battlestream.getPlayerStreams.call(void 0, new (0, _battlestream.BattleStream)());

const spec = {
	formatid: "gen8customgame",
	// format is written in https://github.com/smogon/pokemon-showdown/blob/master/data/aliases.ts
	// formatid: "cc1v1",
};
const p1spec = {
	name: "Bot 1",
	// team: process.argv[2],
	team: _dex.Dex.packTeam(_dex.Dex.generateTeam('gen7randombattle')),
};
const p2spec = {
	name: "Bot 2",
	// team: process.argv[3],
	team : _dex.Dex.packTeam(_dex.Dex.generateTeam('gen7randombattle')),
};

// setting battle role and team
const formatId = 'base';

const isChildProcess = module === process.mainModule;

const logger = require('log4js').getLogger("roomhandler");
logger.info("Room handler starts!");

process.on(isChildProcess ? 'message' : 'fromBot', (msg) => {
	recieve(msg);
}) 


function send(msg, room) {
	const contents = room === undefined ? msg : msg + '@' + room;
	if (isChildProcess) {
		process.send(contents);
	} else {
		process.emit('fromRoomHandler', contents);
		console.log('test');
	}
} // Probably won't work unless i change it.

function recieve(data) {
	logger.trace("<< " + data);

	var roomid = '';
	if (data.substr(0,1) === '>') { // First determine if this command is for a room
		var nlIndex = data.indexOf('\n');
		if (nlIndex < 0) return;
		roomid = util.toRoomid(data.substr(1,nlIndex-1));
		data = data.substr(nlIndex+1);
	}
	if (data.substr(0,6) === '|init|') { // If it is an init command, create the room
		if (!roomid) roomid = 'lobby';
		var roomType = data.substr(6);
		var roomTypeLFIndex = roomType.indexOf('\n');
		if (roomTypeLFIndex >= 0) roomType = roomType.substr(0, roomTypeLFIndex);
		roomType = util.toId(roomType);

		logger.info(roomid + " is being opened.");
		addRoom(roomid, roomType);

	} else if ((data+'|').substr(0,8) === '|expire|') { // Room expiring
		var room = ROOMS[roomid];
		logger.info(roomid + " has expired.");
		if(room) {
			room.expired = true;
			if (room.updateUser) room.updateUser();
		}
		return;
	} else if ((data+'|').substr(0,8) === '|deinit|' || (data+'|').substr(0,8) === '|noinit|') {
		if (!roomid) roomid = 'lobby';

		// expired rooms aren't closed when left
		if (ROOMS[roomid] && ROOMS[roomid].expired) return;

		logger.info(roomid + " has been closed.");
		removeRoom(roomid);
		return;
	}
	if(roomid) { //Forward command to specific room
		if(ROOMS[roomid]) {
			ROOMS[roomid].recieve(data);
		} else {
			logger.error("Room of id " + roomid + " does not exist to send data to.");
		}
		return;
	}

	// Split global command into parts
	var parts;
	if(data.charAt(0) === '|') {
		parts = data.substr(1).split('|');
	} else {
		parts = [];
	}

	switch(parts[0]) {
		// Recieved challenge string
		case 'challenge-string':
		case 'challstr':
			logger.info("Recieved challenge string...");
			CHALLENGE_KEY_ID = parseInt(parts[1], 10);
			CHALLENGE = parts[2];

			// Now try to rename to the given user
			// handled by parent's rename() func 
			send('rename' + '|' + CHALLENGE_KEY_ID + '|' + CHALLENGE);
			break;
		// Server is telling us to update the user that we are currently logged in as
		case 'updateuser':
			// The update user command can actually come with a second command (after the newline)
			var nlIndex = data.indexOf('\n');
			if (nlIndex > 0) {
				recieve(data.substr(nlIndex+1));
				nlIndex = parts[3].indexOf('\n');
				parts[3] = parts[3].substr(0, nlIndex);
			}

			var name = parts[1];
			var named = !!+parts[2];

			if(name == global.account.username) {
				logger.info("Successfully logged in.");
				onLogin()
			}
			break;
		// Server tried to send us a popup
		case 'popup':
			logger.info("Popup: " + data.substr(7).replace(/\|\|/g, '\n'));
			break;
		// Someone has challenged us to a battle
		case 'updatechallenges':
			var challenges = JSON.parse(data.substr(18));
			if(challenges.challengesFrom) {
				for(var user in challenges.challengesFrom) {
					if(challenges.challengesFrom[user] == "gen6randombattle") {
						logger.info("Accepting challenge from " + user);
						send("/accept " + user);
					} else if (challenges.challengesFrom[user] == "gen6battlespotsingles") {
						send("/utm " + team6g);
						send("/accept " + user);
					} else if (challenges.challengesFrom[user] == "gen7randombattle") {
						logger.info("Accepting challenge from " + user);
						send("/accept " + user);
					} else if (challenges.challengesFrom[user] == "gen7battlespotsingles") {
						send("/utm " + team7g);
						send("/accept " + user);
					} else if (challenges.challengesFrom[user] == "gen8randombattle") {
						logger.info("Accepting challenge from " + user);
						send("/accept " + user);
					} else if (challenges.challengesFrom[user] == "gen8battlestadiumsingles") {
						logger.info("Accepting challenge from " + user);
						send("/utm " + team8g);
						send("/accept " + user);
					} else {
						logger.warn("Won't accept challenge of type: " + challenges.challengesFrom[user]);
						send("/reject " + user);
					}
				}
			}
			break;
		// Unkown global command
		default:
			logger.warn("Did not recognize command of type: " + parts[0]);
			break;
	}
}
module.exports.send = send;

// set global variables cloned from parent
global.program = require('commander');

const BattleRoom = require('../tools/random-player-ai');
const p1 = new BattleRoom(1, 'p1', formatId, p1spec.team, streams.p1);
const p2 = new BattleRoom(2, 'p2', formatId, p2spec.team, streams.p2);

console.log("p1 is " + p1.name);
console.log("p2 is " + p2.name);
// console.log(p1);
void p1.start();
void p2.start();
console.log();

void (async () => {
	for await (const chunk of streams.omniscient) {
		console.log(chunk);
		// let log = p1.receive(chunk);
		// console.log(log);

	}
})();


void streams.omniscient.write(`>start ${JSON.stringify(spec)}
>player p1 ${JSON.stringify(p1spec)}
>player p2 ${JSON.stringify(p2spec)}`);
