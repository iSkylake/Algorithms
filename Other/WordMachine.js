function wordMachine(s){
	// Add operations into an array
	let op = s.split(" ");
	let arr = [];

	// Operation list except for add number
	let opList = {
		"POP": function(){
			if(arr.length < 1){
				return "-1";	
			} else {
				arr.pop();
			}
		},
		"DUP": function(){
			if(arr.length < 1){
				return "-1";
			} else {
				arr.push(arr[arr.length-1]);
			}
		},
		"+": function(){
			if(arr.length < 2){
				return "-1";
			} else {
				let temp1 = arr.pop();
				let temp2 = arr.pop();
				let sum = temp1 + temp2;
				arr.push(sum);
			}
		},
		"-": function(){
			if(arr.length < 2){
				return "-1";
			} else {
				let temp1 = arr.pop();
				let temp2 = arr.pop();
				let sub = temp1 - temp2;
				if(sub < 0){
					return "-1";
				} else{
					arr.push(sub);
				}
			}
		}
	};

	// Iterate array of operations
	for(let i=0; i<op.length; i++){
		let num = parseInt(op[i]);
		// Verify if the operation is an number
		if(isNaN(num)){
			// If is an number look for the operation in obj
			let result = opList[op[i]]();
			// Verify and return error
			if(result === "-1"){
				return result;
			}
		} else {
			// Add number to array
			arr.push(num);
		}
	}

	// Return last number
	return arr.pop();
}

console.log(wordMachine("13 DUP 4 POP 5 DUP + DUP + -"));
console.log(wordMachine("5 6 + -"));
console.log(wordMachine("3 DUP 5 - -"));