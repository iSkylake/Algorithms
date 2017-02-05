function additionBalance(arr){
	var left = 0;
	var right = 0;
	for(var i=1; i<arr.length;i++){
		right += arr[i];
	}
	for(var i=0; i<arr.length;i++){
		if(left === right){
			return true;
		}
		left += arr[i];
		if(i<arr.length-1){
			right -= arr[i+1];
		}
	}
	return false;
}

console.log(additionBalance([1, 2, 3, 3]));
console.log(additionBalance([1, 2, 3]));
console.log(additionBalance([0]));