function twoSum(arr, k){
	var hash = {};
	for(var i=0; i<arr.length; i++){
		if(hash[arr[i]] === undefined){
			var sum = k - arr[i];
			hash[sum] = arr[i];
		} else{
			return [hash[arr[i]], arr[i]];
		}
	}
	return [-1, -1];
}

console.log(twoSum([6, -1, 4, 2, 9], 3));
console.log(twoSum([9, 2, -4, 0, -3], 10));