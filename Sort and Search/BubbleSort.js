function bubbleSort(array){
	for(var i=0;i<array.length;i++){
		for(var j=1;j<array.length-i;j++){
			if(array[j]<array[j-1]){
				temp = array[j];
				array[j] = array[j-1];
				array[j-1] = temp;
			}
		}
	}
	return array;
}

console.log(bubbleSort([3, 7, 4, 1, 9, 10]));
console.log(bubbleSort([1, 2, 3, 4, 5, 6]));
console.log(bubbleSort([10, 4, 1, 9, 2, 7, 8]));