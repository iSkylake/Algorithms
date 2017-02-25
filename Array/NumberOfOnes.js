function numOfOnes(arr){
	if(arr[0] === 1){
		return arr.length;
	} else if(arr[arr.length-1] === 0){
		return 0;
	}
	var first = 0; 
	var last = arr.length;
	var mid = Math.floor((first+last)/2);
	while(arr[mid] !== 1 || arr[mid-1] !== 0){
		if(arr[mid]===0){
			first = mid + 1;
		} else{
			last = mid - 1;
		}
		mid = Math.floor((first+last)/2);
	}
	return arr.length - mid;
}

console.log(numOfOnes([0, 0, 1, 1])); // 2
console.log(numOfOnes([0, 0, 0, 1, 1])); // 2
console.log(numOfOnes([0, 0, 1, 1, 1])); // 3
console.log(numOfOnes([0, 0, 0, 0, 0, 1, 1])); //2
console.log(numOfOnes([0, 1, 1, 1, 1])); // 4
console.log(numOfOnes([0, 0, 1])); // 1
console.log(numOfOnes([0, 1])); // 1
console.log(numOfOnes([1, 1, 1, 1, 1, 1])); // 6
console.log(numOfOnes([0, 0, 0, 0, 0])); // 0
console.log(numOfOnes([0])); // 0
console.log(numOfOnes([1])); // 1