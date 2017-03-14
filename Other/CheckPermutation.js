function checkPerm(a1, a2){
	var hash = {};
	var sum = 0;

	for(i=0; i<a1.length; i++){
		if(hash[a1[i]] === undefined){
			hash[a1[i]] = 1;
		} else{
			hash[a1[i]]++;
		}
	}

	for(i=0; i<a2.length;i++){
		if(hash[a2[i]] === undefined){
			return false;
		} else {
			hash[a2[i]]--;
			if(hash[a2[i]] < 0){
				return false
			}
		}
	}

	for(key in hash){
		sum += hash[key]
	}

	if(sum === 0){
		return true;
	} else {
		return false;
	}
}

console.log(checkPerm('abc', 'bca'));
console.log(checkPerm('abc', 'bc'));
console.log(checkPerm('abc', 'cca'));