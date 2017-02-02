function mergeArray(arr1, arr2){
	var arr = [];

	while(arr1.length != 0 && arr2.length != 0){
		if(arr1[0] < arr2[0]){
			arr.push(arr1.shift());
		} else{
			arr.push(arr2.shift());
		}
	}
	while(arr1.length > 0){
		arr.push(arr1.shift());
	}
	while(arr2.length > 0){
		arr.push(arr2.shift());
	}
	console.log(arr);
}

mergeArray([1, 4, 7, 10], [2, 8, 9, 15]);