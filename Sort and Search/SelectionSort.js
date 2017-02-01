function selectionSort(array){
	var len = array.length;
	for(var i=0;i<len;i++){
		var max = 0;
		for(var j=0;j<len-i;j++){
			if(array[j]>array[max]){
				max = j;
			}
		}
		var temp = array[len-1-i];
		array[len-i-1] = array[max];
		array[max] = temp;
	}
	return array;
}

console.log(selectionSort([6,2,4,1,9]));
console.log(selectionSort([1,2,3,4]));
console.log(selectionSort([9,8,7,6,5,4,3,2,1]));