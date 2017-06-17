function balanceBracket(comb){

	if(comb.length%2 !== 0){
		return false;
	}

	let bracketStack = [];
	let openBrackets = ['[', '{', '('];
	let closeBrackets = {']': '[', '}': '{', ')': '('};

	for(let i=0; i<comb.length; i++){
		if(openBrackets.includes(comb[i])){
			bracketStack.push(comb[i]);
		} else {
			if(bracketStack.length < 1){
				return false;
			}
			let lastBracket = bracketStack.pop();
			if(lastBracket !== closeBrackets[comb[i]]){
				return false;
			}
		}
	}

	if(bracketStack.length < 1){
		return true;
	} else {
		return false;
	}
}

console.log(balanceBracket("[{()}]"));
console.log(balanceBracket("][()"));
console.log(balanceBracket("({[(][)]})"));
console.log(balanceBracket("(){}["));