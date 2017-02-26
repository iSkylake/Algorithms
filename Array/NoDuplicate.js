function noDuplicate(arr){
	var count = 1;
	for(i=1; i<arr.length; i++){
		if(arr[i-1] !== arr[i]){
			count++;
		}
	}
	return count
}

console.log(noDuplicate([1, 1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 9, 9]));