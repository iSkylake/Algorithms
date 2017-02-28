function sortedSubString(arr){
	var left = 1;
	var right = arr.length - 1;
	var index = [];

	while(left < arr.length || right > 1){
		if(arr[left] < arr[left-1]){
			index[1] = left;
		} 

		if(arr[right] < arr[right-1]){
			index[0] = right-1;
		}
		left++;
		right--;
	}
	return index;
}

console.log(sortedSubString([3, 4, 8, 7, 10, 6, 17]));
console.log(sortedSubString([3, 4, 8, 7, 20, 6, 17]));