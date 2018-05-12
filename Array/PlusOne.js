function addOne(arr){
	let i = arr.length - 1;
	if(arr[i] < 9){
		arr[i] += 1;
	} else {
		while(arr[i] === 9 && i >= 0){
			arr[i] = 0;
			i--;
		}
		if(i === -1){
			arr.unshift(1);
		} else {
			arr[i] += 1;
		}
	}
	return arr;
}

// INPUT
let input = [[1, 2], [1, 9], [1, 2, 9], [9], [9, 9, 9]];
let correctOutput = [[1, 3], [2, 0], [1, 3, 0], [1, 0], [1, 0, 0, 0]];

// TESTING
for(let i=0; i<input.length; i++){
	let result = "";
	let output = addOne(input[i]).toString();
	if(correctOutput[i].toString() === output.toString()){
		result = "PASSED";
	} else {
		result = "FAILED";
	}
	console.log(`${input[i]} => ${output} ${result}`);
};