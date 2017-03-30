function mergeSort(arr){
	if(arr.length <= 1){
		return arr;
	}

	var mid = Math.floor(arr.length/2);
	var left = mergeSort(arr.slice(0, mid));
	var right = mergeSort(arr.slice(mid, arr.length));

	var i = 0, j = 0, k = 0;
	var sorted = [];
	
	while(i < left.length && j < right.length){
		if(left[i] < right[j]){
			sorted[k] = left[i];
			i++
		} else {
			sorted[k] = right[j];
			j++
		}
		k++;
	}

	while(k < arr.length){
		if(i < left.length){
			sorted[k] = left[i];
			i++;
		}

		if(j < right.length){
			sorted[k] = right[j];
			j++
		}
		k++;
	}

	return sorted;
}

console.log(mergeSort([6, 8, 2, 3, 0, 5]));