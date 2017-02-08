function binarySearch(arr, n){
	var first = 0;
	var last = arr.length;
	while(first <= last){
		var mid = Math.floor((first+last)/2);
		if(n == arr[mid]){
			return true;
		} else if(n < arr[mid]){
			last = mid-1;
		} else{
			first = mid+1;
		}
	}
	return false;
}

function recBinSearch(arr, n){
	mid = Math.floor(arr.length/2);
	if(arr.length < 1){
		return false;
	}
	if(arr[mid] === n){
		return true;
	}
	if(n < arr[mid]){
		return recBinSearch(arr.slice(0, mid), n);
	} else{
		return recBinSearch(arr.slice(mid+1, arr.length), n);
	}
}

console.log(binarySearch([1, 2, 4, 5, 6, 7], 1));
console.log(binarySearch([1, 2, 4, 5, 6, 7], 2));
console.log(binarySearch([1, 2, 4, 5, 6, 7], 4));
console.log(binarySearch([1, 2, 4, 5, 6, 7], 5));
console.log(binarySearch([1, 2, 4, 5, 6, 7], 6));
console.log(binarySearch([1, 2, 4, 5, 6, 7], 7));
console.log(binarySearch([1, 2, 4, 5, 6, 7], 0));
console.log(binarySearch([1, 2, 4, 5, 6, 7], 8));
console.log(binarySearch([1, 2, 5, 6, 7], 18));

console.log(" ");

console.log(recBinSearch([1, 2, 4, 5, 6, 7], 1));
console.log(recBinSearch([1, 2, 4, 5, 6, 7], 2));
console.log(recBinSearch([1, 2, 4, 5, 6, 7], 4));
console.log(recBinSearch([1, 2, 4, 5, 6, 7], 5));
console.log(recBinSearch([1, 2, 4, 5, 6, 7], 6));
console.log(recBinSearch([1, 2, 4, 5, 6, 7], 7));
console.log(recBinSearch([1, 2, 4, 5, 6, 7], 0));
console.log(recBinSearch([1, 2, 4, 5, 6, 7], 8));
console.log(recBinSearch([1, 2, 5, 6, 7], 18));