function median(arr1, arr2){
	var i = 0, j = 0, k = 0;
	var prev, current;

	while(k < arr1.length + 1){
		
		if(k > 0){
			prev = current;
		}

		if(i < arr1.length && arr1[i] < arr2[j]){
			current = arr1[i];
			i++;
		} else {
			current = arr2[j];
			j++;
		}

		k++;
	}

	return (current+prev)/2;
}

console.log(median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45]));
console.log(median([1, 10, 13, 15], [2, 4, 6, 7]));
console.log(median([1], [5]));