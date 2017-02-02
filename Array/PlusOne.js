function plusOne(arr){
	var len = arr.length
	if(arr[len-1] < 9){
		arr[len-1]++;
		return (arr);
	}
	var i = len-1;
	while(arr[i] === 9){
		if(i===0){
			arr[i] = 0;
			arr.unshift(1);
			return arr;
		} else if(arr[i-1] < 9){
			arr[i] = 0;
			arr[i-1]++;
		}
		arr[i] = 0;
		i--;
	}
	return arr;
}

console.log(plusOne([1, 0, 0]));
console.log(plusOne([9, 9]));
console.log(plusOne([1, 9, 9]));