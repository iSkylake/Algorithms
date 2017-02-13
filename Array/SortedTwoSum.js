function sortTwoSum(arr, k){
	var l = 0;
	var r = arr.length;
	var total = 0
	while(l < r){
		total = arr[l] + arr[r];
		if(total === k){
			return true;
		} else if(total < k){
			l++;
		} else{
			r--;
		}
	}
	return false;
}

console.log(sortTwoSum([1, 3, 5, 6, 10], 9));
console.log(sortTwoSum([2, 3, 5, 7, 9], 15));
