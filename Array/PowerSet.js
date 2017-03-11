function powerSet(string){
	setList = [];

	function traverse(sets, level){

		if(level === string.length){
			setList.push(sets);
			return
		}

		traverse(sets, level+1);
		traverse(sets+string[level], level+1)
	}

	traverse("", 0);
	return setList;
}

console.log(powerSet("ab"));
console.log(powerSet("abc"));