"use strict";Object.defineProperty(exports, "__esModule", {value: true});/**
 * Simulator Battle
 * Pokemon Showdown - http://pokemonshowdown.com/
 *
 * @license MIT license
 */
var _utils = require('../.lib-dist/utils');

/**
* Converts anything to an ID. An ID must have only lowercase alphanumeric
* characters.
*
* If a string is passed, it will be converted to lowercase and
* non-alphanumeric characters will be stripped.
*
* If an object with an ID is passed, its ID will be returned.
* Otherwise, an empty string will be returned.
*
* Generally assigned to the global toID, because of how
* commonly it's used.
*/
 function toID(text) {
	// The sucrase transformation of optional chaining is too expensive to be used in a hot function like this.
	/* eslint-disable @typescript-eslint/prefer-optional-chain */
	if (text && text.id) {
		text = text.id;
	} else if (text && text.userid) {
		text = text.userid;
	} else if (text && text.roomid) {
		text = text.roomid;
	}
	if (typeof text !== 'string' && typeof text !== 'number') return '';
	return ('' + text).toLowerCase().replace(/[^a-z0-9]+/g, '') ;
	/* eslint-enable @typescript-eslint/prefer-optional-chain */
} exports.toID = toID;

 class BasicEffect  {
	/**
	 * ID. This will be a lowercase version of the name with all the
	 * non-alphanumeric characters removed. So, for instance, "Mr. Mime"
	 * becomes "mrmime", and "Basculin-Blue-Striped" becomes
	 * "basculinbluestriped".
	 */
	
	/**
	 * Name. Currently does not support Unicode letters, so "Flabébé"
	 * is "Flabebe" and "Nidoran♀" is "Nidoran-F".
	 */
	
	/**
	 * Full name. Prefixes the name with the effect type. For instance,
	 * Leftovers would be "item: Leftovers", confusion the status
	 * condition would be "confusion", etc.
	 */
	
	/** Effect type. */
	
	/**
	 * Does it exist? For historical reasons, when you use an accessor
	 * for an effect that doesn't exist, you get a dummy effect that
	 * doesn't do anything, and this field set to false.
	 */
	
	/**
	 * Dex number? For a Pokemon, this is the National Dex number. For
	 * other effects, this is often an internal ID (e.g. a move
	 * number). Not all effects have numbers, this will be 0 if it
	 * doesn't. Nonstandard effects (e.g. CAP effects) will have
	 * negative numbers.
	 */
	
	/**
	 * The generation of Pokemon game this was INTRODUCED (NOT
	 * necessarily the current gen being simulated.) Not all effects
	 * track generation; this will be 0 if not known.
	 */
	
	/**
	 * A shortened form of the description of this effect.
	 * Not all effects have this.
	 */
	
	/** The full description for this effect. */
	
	/**
	 * Is this item/move/ability/pokemon nonstandard? Specified for effects
	 * that have no use in standard formats: made-up pokemon (CAP),
	 * glitches (MissingNo etc), Pokestar pokemon, etc.
	 */
	
	/** The duration of the condition - only for pure conditions. */
	
	/** Whether or not the condition is ignored by Baton Pass - only for pure conditions. */
	
	/** Whether or not the condition affects fainted Pokemon. */
	
	/** Moves only: what status does it set? */
	
	/** Moves only: what weather does it set? */
	
	/** ??? */
	

	constructor(data, ...moreData) {
		this.exists = true;
		data = combine(this, data, ...moreData);

		this.name = _utils.Utils.getString(data.name).trim();
		this.id = data.realMove ? toID(data.realMove) : toID(this.name); // Hidden Power hack
		this.fullname = _utils.Utils.getString(data.fullname) || this.name;
		this.effectType = _utils.Utils.getString(data.effectType)  || 'Condition';
		this.exists = !!(this.exists && this.id);
		this.num = data.num || 0;
		this.gen = data.gen || 0;
		this.shortDesc = data.shortDesc || '';
		this.desc = data.desc || '';
		this.isNonstandard = data.isNonstandard || null;
		this.duration = data.duration;
		this.noCopy = !!data.noCopy;
		this.affectsFainted = !!data.affectsFainted;
		this.status = data.status  || undefined;
		this.weather = data.weather  || undefined;
		this.sourceEffect = data.sourceEffect || '';
	}

	toString() {
		return this.name;
	}
} exports.BasicEffect = BasicEffect;

 class Learnset {
	
	/**
	 * Keeps track of exactly how a pokemon might learn a move, in the
	 * form moveid:sources[].
	 */
	
	/** True if the only way to get this Pokemon is from events. */
	
	/** List of event data for each event. */
	
	
	

	constructor(data) {
		this.exists = true;
		this.effectType = 'Learnset';
		this.learnset = data.learnset || undefined;
		this.eventOnly = !!data.eventOnly;
		this.eventData = data.eventData || undefined;
		this.encounters = data.encounters || undefined;
	}
} exports.Learnset = Learnset;

 class Nature extends BasicEffect  {
	
	
	
	constructor(data, ...moreData) {
		super(data, moreData);
		data = this;

		this.fullname = `nature: ${this.name}`;
		this.effectType = 'Nature';
		this.gen = 3;
		this.plus = data.plus || undefined;
		this.minus = data.minus || undefined;
	}
} exports.Nature = Nature;



 class TypeInfo  {
	/**
	 * ID. This will be a lowercase version of the name with all the
	 * non-alphanumeric characters removed. e.g. 'flying'
	 */
	
	/** Name. e.g. 'Flying' */
	
	/** Effect type. */
	
	/**
	 * Does it exist? For historical reasons, when you use an accessor
	 * for an effect that doesn't exist, you get a dummy effect that
	 * doesn't do anything, and this field set to false.
	 */
	
	/**
	 * The generation of Pokemon game this was INTRODUCED (NOT
	 * necessarily the current gen being simulated.) Not all effects
	 * track generation; this will be 0 if not known.
	 */
	
	/**
	 * Type chart, attackingTypeName:result, effectid:result
	 * result is: 0 = normal, 1 = weakness, 2 = resistance, 3 = immunity
	 */
	
	/** The IVs to get this Type Hidden Power (in gen 3 and later) */
	
	/** The DVs to get this Type Hidden Power (in gen 2). */
	

	constructor(data, ...moreData) {
		this.exists = true;
		data = combine(this, data, ...moreData);

		this.id = data.id || '';
		this.name = _utils.Utils.getString(data.name).trim();
		this.effectType = _utils.Utils.getString(data.effectType)  || 'Type';
		this.exists = !!(this.exists && this.id);
		this.gen = data.gen || 0;
		this.damageTaken = data.damageTaken || {};
		this.HPivs = data.HPivs || {};
		this.HPdvs = data.HPdvs || {};
	}

	toString() {
		return this.name;
	}
} exports.TypeInfo = TypeInfo;

 function combine(obj, ...data) {
	for (const d of data) {
		if (d) Object.assign(obj, d);
	}
	return obj;
} exports.combine = combine;

// export class PokemonSet {
// 	/**
// 	 * The Pokemon's set's nickname, which is identical to its base
// 	 * species if not specified by the player, e.g. "Minior".
// 	 */
// 	name: string;
// 	/**
// 	 * The Pokemon's species, e.g. "Minior-Red".
// 	 * This should always be converted to an id before use.
// 	 */
// 	species: string;
// 	/**
// 	 * The Pokemon's set's item. This can be an id, e.g. "whiteherb"
// 	 * or a full name, e.g. "White Herb".
// 	 * This should always be converted to an id before use.
// 	 */
// 	item: string;
// 	/**
// 	 * The Pokemon's set's ability. This can be an id, e.g. "shieldsdown"
// 	 * or a full name, e.g. "Shields Down".
// 	 * This should always be converted to an id before use.
// 	 */
// 	ability: string;
// 	/**
// 	 * An array of the Pokemon's set's moves. Each move can be an id,
// 	 * e.g. "shellsmash" or a full name, e.g. "Shell Smash"
// 	 * These should always be converted to ids before use.
// 	 */
// 	moves: string[];
// 	/**
// 	 * The Pokemon's set's nature. This can be an id, e.g. "adamant"
// 	 * or a full name, e.g. "Adamant".
// 	 * This should always be converted to an id before use.
// 	 */
// 	nature: string;
// 	/**
// 	 * The Pokemon's set's gender.
// 	 */
// 	gender: GenderName;
// 	/**
// 	 * The Pokemon's set's effort values, used in stat calculation.
// 	 * These must be between 0 and 255, inclusive.
// 	 */
// 	evs: StatsTable;
// 	/**
// 	 * The Pokemon's individual values, used in stat calculation.
// 	 * These must be between 0 and 31, inclusive.
// 	 * These are also used as DVs, or determinant values, in Gens
// 	 * 1 and 2, which are represented as even numbers from 0 to 30.
// 	 * From Gen 2 and on, IVs/DVs are used to determine Hidden Power's
// 	 * type, although in Gen 7 a Pokemon may be legally altered such
// 	 * that its stats are calculated as if these values were 31 via
// 	 * Bottlecaps. Currently, PS handles this by considering any
// 	 * IV of 31 in Gen 7 to count as either even or odd for the purpose
// 	 * of validating a Hidden Power type, though restrictions on
// 	 * possible IVs for event-only Pokemon are still considered.
// 	 */
// 	ivs: StatsTable;
// 	/**
// 	 * The Pokemon's level. This is usually between 1 and 100, inclusive,
// 	 * but the simulator supports levels up to 9999 for testing purposes.
// 	 */
// 	level: number;
// 	/**
// 	 * Whether the Pokemon is shiny or not. While having no direct
// 	 * competitive effect except in a few OMs, certain Pokemon cannot
// 	 * be legally obtained as shiny, either as a whole or with certain
// 	 * event-only abilities or moves.
// 	 */
// 	shiny?: boolean;
// 	/**
// 	 * The Pokemon's set's happiness value. This is used only for
// 	 * calculating the base power of the moves Return and Frustration.
// 	 * This value must be between 0 and 255, inclusive.
// 	 */
// 	happiness: number;
// 	/**
// 	 * The Pokemon's set's Hidden Power type. This value is intended
// 	 * to be used to manually set a set's HP type in Gen 7 where
// 	 * its IVs do not necessarily reflect the user's intended type.
// 	 * TODO: actually support this in the teambuilder.
// 	 */
// 	hpType?: string;
// 	/**
// 	 * The pokeball this Pokemon is in. Like shininess, this property
// 	 * has no direct competitive effects, but has implications for
// 	 * event legality. For example, any Rayquaza that knows V-Create
// 	 * must be sent out from a Cherish Ball.
// 	 * TODO: actually support this in the validator, switching animations,
// 	 * and the teambuilder.
// 	 */
// 	pokeball?: string;
//
// 	constructor(data: Partial<PokemonSet>) {
// 		this.name = '';
// 		this.species = '';
// 		this.item = '';
// 		this.ability = 'noability';
// 		this.moves = [];
// 		this.nature = '';
// 		this.gender = '';
// 		this.evs = {hp: 0, atk: 0, def: 0, spa: 0, spd: 0, spe: 0};
// 		this.ivs = {hp: 31, atk: 31, def: 31, spa: 31, spd: 31, spe: 31};
// 		this.level = 100;
// 		this.shiny = undefined;
// 		this.happiness = 255; // :)
// 		this.hpType = undefined;
// 		this.pokeball = undefined;
// 		Object.assign(this, data);
// 	}
// }
