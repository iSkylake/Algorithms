function insertionSort(arr){
	for(var i=1; i<arr.length; i++){
		j = i;
		while(arr[j]<arr[j-1]){
			temp = arr[j];
			arr[j] = arr[j-1]
			arr[j-1] = temp;
			j--;
		}
	}
	console.log(arr);
}

insertionSort([5, 3, 1, 8, 9, 6]);