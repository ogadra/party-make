"use strict";Object.defineProperty(exports, "__esModule", {value: true});var _dexdata = require('./dex-data');




































































































































































































































































































































































































































































































































































































 class Condition extends _dexdata.BasicEffect  {
	
	

	
	
	
	
	

	constructor(data, ...moreData) {
		super(data, ...moreData);
		data = this;
		this.effectType = (['Weather', 'Status'].includes(data.effectType) ? data.effectType : 'Condition');
	}
} exports.Condition = Condition;
