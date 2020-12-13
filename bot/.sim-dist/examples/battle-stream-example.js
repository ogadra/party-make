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


function send(msg, room) {
	const contents = room === undefined ? msg : msg + '@' + room;
	if (isChildProcess) {
		process.send(contents);
	} else {
		process.emit('fromRoomHandler', contents);
	}
} // Probably won't work unless i change it.


const isChildProcess = module === process.mainModule;

const logger = require('log4js').getLogger("roomhandler");
logger.info("Room handler starts!");

// set global variables cloned from parent
global.program = require('commander');

const BattleRoom = require('../tools/random-player-ai');
const p1 = new BattleRoom(1, send, formatId, p1spec.team, streams.p1);
const p2 = new BattleRoom(2, send, formatId, p2spec.team, streams.p2);

console.log("p1 is " + p1.constructor.name);
console.log("p2 is " + p2.constructor.name);
// console.log(p1);
// void p1.start();
// void p2.start();
console.log();

void (async () => {
	for await (const chunk of streams.omniscient) {
		console.log(chunk);
		let log = p1.recieve(chunk);
		console.log(log);
	}
})();

void streams.omniscient.write(`>start ${JSON.stringify(spec)}
>player p1 ${JSON.stringify(p1spec)}
>player p2 ${JSON.stringify(p2spec)}`);
