/**
 * Battle Stream Example
 * Pokemon Showdown - http://pokemonshowdown.com/
 *
 * Example of how to create AIs battling against each other.
 * Run this using `node build && node .sim-dist/examples/battle-stream-example`.
 *
 * @license MIT
 * @author Guangcong Luo <guangcongluo@gmail.com>
 */

import { processManagers } from '../../lib/process-manager';
import {BattleStream, getPlayerStreams} from '../battle-stream';
import {Dex} from '../dex';
import {RandomPlayerAI} from '../tools/random-player-ai';

/*********************************************************************
 * Run AI
 *********************************************************************/

const streams = getPlayerStreams(new BattleStream());

const spec = {
	formatid: "gen8customgame",
	// format is written in https://github.com/smogon/pokemon-showdown/blob/master/data/aliases.ts
	// formatid: "cc1v1",
};
const p1spec = {
	name: "Bot 1",
	team: process.argv[2],
};
const p2spec = {
	name: "Bot 2",
	team: process.argv[3],
};

const p1 = new RandomPlayerAI(streams.p1);
const p2 = new RandomPlayerAI(streams.p2);

console.log("p1 is " + p1.constructor.name);
console.log("p2 is " + p2.constructor.name);

void p1.start();
void p2.start();

void (async () => {
	for await (const chunk of streams.omniscient) {
		console.log(chunk);
	}
})();

void streams.omniscient.write(`>start ${JSON.stringify(spec)}
>player p1 ${JSON.stringify(p1spec)}
>player p2 ${JSON.stringify(p2spec)}`);
