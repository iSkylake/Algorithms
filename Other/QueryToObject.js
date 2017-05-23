let query = 'http://www.randomSite.com/?name=hana&time=43627543&favorite=mech,starcraft,stream'

function queryToObj(query){
	let urlList = query.split("?");
	let queryList = urlList[1].split("&");
	let obj = {};
	for(let i=0; i<queryList.length; i++){
		let item = queryList[i].split("=");
		obj[item[0]] = item[1]
	}
	return obj;
}

console.log(queryToObj(query));