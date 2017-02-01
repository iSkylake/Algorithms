function selectionSort(array){
	var len = array.length;
	for(var i=0;i<len;i++){
		var max = 0;
		for(var j=0;j<len-i;j++){
			if(array[j]>array[max]){
				max = j;
			}
		}
	}
}