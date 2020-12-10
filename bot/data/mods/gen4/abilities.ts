export const Abilities: {[k: string]: ModdedAbilityData} = {
	airlock: {
		inherit: true,
		onSwitchIn() {},
		onStart() {},
	},
	angerpoint: {
		inherit: true,
		onAfterSubDamage(damage, target, source, move) {
			if (!target.hp) return;
			if (move && move.effectType === 'Move' && target.getMoveHitData(move).crit) {
				target.setBoost({atk: 6});
				this.add('-setboost', target, 'atk', 12, '[from] ability: Anger Point');
			}
		},
		rating: 1.5,
	},
	blaze: {
		onBasePowerPriority: 2,
		onBasePower(basePower, attacker, defender, move) {
			if (move.type === 'Fire' && attacker.hp <= attacker.maxhp / 3) {
				this.debug('Blaze boost');
				return this.chainModify(1.5);
			}
		},
		name: "Blaze",
		rating: 2,
		num: 66,
	},
	cloudnine: {
		inherit: true,
		onSwitchIn() {},
		onStart() {},
	},
	colorchange: {
		inherit: true,
		onDamagingHit(damage, target, source, move) {
			if (!damage || !target.hp) return;
			const type = move.type;
			if (target.isActive && move.category !== 'Status' && type !== '???' && !target.hasType(type)) {
				if (!target.setType(type)) return false;
				this.add('-start', target, 'typechange', type, '[from] ability: Color Change');
			}
		},
		onAfterMoveSecondary() {},
	},
	cutecharm: {
		inherit: true,
		onDamagingHit(damage, target, source, move) {
			if (damage && move.flags['contact']) {
				if (this.randomChance(3, 10)) {
					source.addVolatile('attract', this.effectData.target);
				}
			}
		},
	},
	effectspore: {
		inherit: true,
		onDamagingHit(damage, target, source, move) {
			if (damage && move.flags['contact'] && !source.status) {
				const r = this.random(100);
				if (r < 10) {
					source.setStatus('slp', target);
				} else if (r < 20) {
					source.setStatus('par', target);
				} else if (r < 30) {
					source.setStatus('psn', target);
				}
			}
		},
	},
	flamebody: {
		inherit: true,
		onDamagingHit(damage, target, source, move) {
			if (damage && move.flags['contact']) {
				if (this.randomChance(3, 10)) {
					source.trySetStatus('brn', target);
				}
			}
		},
	},
	flashfire: {
		inherit: true,
		onTryHit(target, source, move) {
			if (target !== source && move.type === 'Fire') {
				if (target.status === 'frz') {
					return;
				}
				if (!target.addVolatile('flashfire')) {
					this.add('-immune', target, '[from] ability: Flash Fire');
				}
				return null;
			}
		},
		condition: {
			noCopy: true, // doesn't get copied by Baton Pass
			onStart(target) {
				this.add('-start', target, 'ability: Flash Fire');
			},
			onModifyDamagePhase1(atk, attacker, defender, move) {
				if (move.type === 'Fire') {
					this.debug('Flash Fire boost');
					return this.chainModify(1.5);
				}
			},
			onEnd(target) {
				this.add('-end', target, 'ability: Flash Fire', '[silent]');
			},
		},
	},
	flowergift: {
		inherit: true,
		onAllyModifyAtk(atk) {
			if (this.field.isWeather('sunnyday')) {
				return this.chainModify(1.5);
			}
		},
		onAllyModifySpD(spd) {
			if (this.field.isWeather('sunnyday')) {
				return this.chainModify(1.5);
			}
		},
	},
	forewarn: {
		inherit: true,
		onStart(pokemon) {
			let warnMoves: Move[] = [];
			let warnBp = 1;
			for (const target of pokemon.side.foe.active) {
				if (target.fainted) continue;
				for (const moveSlot of target.moveSlots) {
					const move = this.dex.getMove(moveSlot.move);
					let bp = move.basePower;
					if (move.ohko) bp = 160;
					if (move.id === 'counter' || move.id === 'metalburst' || move.id === 'mirrorcoat') bp = 120;
					if (!bp && move.category !== 'Status') bp = 80;
					if (bp > warnBp) {
						warnMoves = [move];
						warnBp = bp;
					} else if (bp === warnBp) {
						warnMoves.push(move);
					}
				}
			}
			if (!warnMoves.length) return;
			const warnMove = this.sample(warnMoves);
			this.add('-activate', pokemon, 'ability: Forewarn', warnMove);
		},
	},
	insomnia: {
		inherit: true,
		rating: 2.5,
	},
	intimidate: {
		inherit: true,
		onStart(pokemon) {
			let activated = false;
			for (const target of pokemon.side.foe.active) {
				if (target && this.isAdjacent(target, pokemon) &&
					!(target.volatiles['substitute'] ||
						target.volatiles['substitutebroken'] && target.volatiles['substitutebroken'].move === 'uturn')) {
					activated = true;
					break;
				}
			}

			if (!activated) {
				this.hint("In Gen 4, Intimidate does not activate if every target has a Substitute (or the Substitute was just broken by U-turn).", false, pokemon.side);
				return;
			}
			this.add('-ability', pokemon, 'Intimidate', 'boost');

			for (const target of pokemon.side.foe.active) {
				if (!target || !this.isAdjacent(target, pokemon)) continue;

				if (target.volatiles['substitute']) {
					this.add('-immune', target);
				} else if (target.volatiles['substitutebroken'] && target.volatiles['substitutebroken'].move === 'uturn') {
					this.hint("In Gen 4, if U-turn breaks Substitute the incoming Intimidate does nothing.");
				} else {
					this.boost({atk: -1}, target, pokemon, null, true);
				}
			}
		},
	},
	leafguard: {
		inherit: true,
		onSetStatus(status, target, source, effect) {
			if (effect && effect.id === 'rest') {
				return;
			} else if (this.field.isWeather('sunnyday')) {
				return false;
			}
		},
	},
	lightningrod: {
		inherit: true,
		onTryHit() {},
		rating: 0,
	},
	magicguard: {
		onDamage(damage, target, source, effect) {
			if (effect.effectType !== 'Move') {
				return false;
			}
		},
		onSetStatus(status, target, source, effect) {
			if (effect && effect.id === 'toxicspikes') {
				return false;
			}
		},
		name: "Magic Guard",
		rating: 4.5,
		num: 98,
	},
	minus: {
		onModifySpA(spa, pokemon) {
			const allyActive = pokemon.side.active;
			if (allyActive.length === 1) {
				return;
			}
			for (const ally of allyActive) {
				if (ally && ally.position !== pokemon.position && !ally.fainted && ally.ability === 'plus') {
					return spa * 1.5;
				}
			}
		},
		name: "Minus",
		rating: 0,
		num: 58,
	},
	naturalcure: {
		inherit: true,
		onCheckShow(pokemon) {},
		onSwitchOut(pokemon) {
			if (!pokemon.status || pokemon.status === 'fnt') return;

			// Because statused/unstatused pokemon are shown after every switch
			// in gen 3-4, Natural Cure's curing is always known to both players

			this.add('-curestatus', pokemon, pokemon.status, '[from] ability: Natural Cure');
			pokemon.setStatus('');
		},
	},
	normalize: {
		inherit: true,
		onModifyMove(move) {
			if (move.id !== 'struggle') {
				move.type = 'Normal';
			}
		},
	},
	overgrow: {
		onBasePowerPriority: 2,
		onBasePower(basePower, attacker, defender, move) {
			if (move.type === 'Grass' && attacker.hp <= attacker.maxhp / 3) {
				this.debug('Overgrow boost');
				return this.chainModify(1.5);
			}
		},
		name: "Overgrow",
		rating: 2,
		num: 65,
	},
	pickup: {
		name: "Pickup",
		rating: 0,
		num: 53,
	},
	plus: {
		onModifySpA(spa, pokemon) {
			const allyActive = pokemon.side.active;
			if (allyActive.length === 1) {
				return;
			}
			for (const ally of allyActive) {
				if (ally && ally.position !== pokemon.position && !ally.fainted && ally.ability === 'minus') {
					return spa * 1.5;
				}
			}
		},
		name: "Plus",
		rating: 0,
		num: 57,
	},
	poisonpoint: {
		inherit: true,
		onDamagingHit(damage, target, source, move) {
			if (damage && move.flags['contact']) {
				if (this.randomChance(3, 10)) {
					source.trySetStatus('psn', target);
				}
			}
		},
	},
	pressure: {
		onStart(pokemon) {
			this.add('-ability', pokemon, 'Pressure');
		},
		onDeductPP(target, source) {
			if (target === source) return;
			return 1;
		},
		name: "Pressure",
		rating: 1.5,
		num: 46,
	},
	roughskin: {
		inherit: true,
		onDamagingHit(damage, target, source, move) {
			if (damage && move.flags['contact']) {
				this.damage(source.baseMaxhp / 16, source, target);
			}
		},
	},
	serenegrace: {
		inherit: true,
		onModifyMove(move) {
			if (move.secondaries) {
				this.debug('doubling secondary chance');
				for (const secondary of move.secondaries) {
					if (secondary.chance) secondary.chance *= 2;
				}
			}
		},
	},
	simple: {
		onModifyBoost(boosts) {
			let key: BoostName;
			for (key in boosts) {
				boosts[key]! *= 2;
			}
		},
		name: "Simple",
		rating: 4,
		num: 86,
	},
	soundproof: {
		inherit: true,
	},
	static: {
		inherit: true,
		onDamagingHit(damage, target, source, move) {
			if (damage && move.flags['contact']) {
				if (this.randomChance(3, 10)) {
					source.trySetStatus('par', target);
				}
			}
		},
	},
	stench: {
		name: "Stench",
		rating: 0,
		num: 1,
	},
	stickyhold: {
		inherit: true,
		onTakeItem(item, pokemon, source) {
			if (this.suppressingAttackEvents(pokemon)) return;
			if ((source && source !== pokemon) || (this.activeMove && this.activeMove.id === 'knockoff')) {
				this.add('-activate', pokemon, 'ability: Sticky Hold');
				return false;
			}
		},
	},
	stormdrain: {
		inherit: true,
		onTryHit() {},
		rating: 0,
	},
	sturdy: {
		inherit: true,
		onDamage() {},
		rating: 0,
	},
	swarm: {
		onBasePowerPriority: 2,
		onBasePower(basePower, attacker, defender, move) {
			if (move.type === 'Bug' && attacker.hp <= attacker.maxhp / 3) {
				this.debug('Swarm boost');
				return this.chainModify(1.5);
			}
		},
		name: "Swarm",
		rating: 2,
		num: 68,
	},
	synchronize: {
		inherit: true,
		onAfterSetStatus(status, target, source, effect) {
			if (!source || source === target) return;
			if (effect && effect.id === 'toxicspikes') return;
			let id: string = status.id;
			if (id === 'slp' || id === 'frz') return;
			if (id === 'tox') id = 'psn';
			source.trySetStatus(id, target);
		},
	},
	thickfat: {
		onSourceBasePowerPriority: 1,
		onSourceBasePower(basePower, attacker, defender, move) {
			if (move.type === 'Ice' || move.type === 'Fire') {
				return this.chainModify(0.5);
			}
		},
		name: "Thick Fat",
		rating: 3.5,
		num: 47,
	},
	torrent: {
		onBasePowerPriority: 2,
		onBasePower(basePower, attacker, defender, move) {
			if (move.type === 'Water' && attacker.hp <= attacker.maxhp / 3) {
				this.debug('Torrent boost');
				return this.chainModify(1.5);
			}
		},
		name: "Torrent",
		rating: 2,
		num: 67,
	},
	trace: {
		inherit: true,
		onUpdate(pokemon) {
			if (!pokemon.isStarted) return;
			const target = pokemon.side.foe.randomActive();
			if (!target || target.fainted) return;
			const ability = target.getAbility();
			const bannedAbilities = ['forecast', 'multitype', 'trace'];
			if (bannedAbilities.includes(target.ability)) {
				return;
			}
			if (pokemon.setAbility(ability)) {
				this.add('-ability', pokemon, ability, '[from] ability: Trace', '[of] ' + target);
			}
		},
	},
	vitalspirit: {
		inherit: true,
		rating: 2.5,
	},
	wonderguard: {
		inherit: true,
		onTryHit(target, source, move) {
			if (move.id === 'firefang') {
				this.hint("In Gen 4, Fire Fang is always able to hit through Wonder Guard.");
				return;
			}
			if (target === source || move.category === 'Status' || move.type === '???' || move.id === 'struggle') return;
			this.debug('Wonder Guard immunity: ' + move.id);
			if (target.runEffectiveness(move) <= 0) {
				this.add('-immune', target, '[from] ability: Wonder Guard');
				return null;
			}
		},
	},
};
