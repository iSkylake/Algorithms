function myIndexOf(target, string){
	string = string.toLowerCase();
	target = target.toLowerCase();
	for(let i=0; i<string.length; i++){
		if(string[i] === target[0]){
			let index = i;
			let subIndex = 0;
			while(string[index] === target[subIndex] && index<string.length){
				index++;
				subIndex++;
			}
			if(subIndex === target.length){
				return i;
			}
		}
	}
	return "-1";
}

let string = "Face is the place SMORC."

console.log(myIndexOf("is", string));
console.log(myIndexOf("orc", string));
console.log(myIndexOf("F", string));