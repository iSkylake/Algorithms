function vacation(arr){
	let index = 1;

	// Check the left side
	while(index < arr.length){
		if(arr[0] === arr[index]){
			arr.shift();
		}
		index++;
	}

	// Check the right side
	index = arr.length - 2;
	while(index >= 0){
		if(arr[arr.length-1] === arr[index]){
			arr.pop();
		}
		index--;
	}

	return arr.length;
}

console.log(vacation([7, 3, 7, 3, 1, 3, 4, 1])) // 5