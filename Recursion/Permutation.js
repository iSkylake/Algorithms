function permutation(arr){
	if(arr.length <= 1){
		return arr;
	}

	var perms = [];

	for(var i=0; i<arr.length; i++){
		var char = arr[i];
		
		var rem = arr.slice(0,i) + arr.slice(i+1, arr.length);

		for(var p of permutation(rem)){
			perms.push(char+p);
		}
		
	}

	return perms;
}

console.log(permutation('123'));