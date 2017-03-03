function reverseString(s){
	if(s.length < 1){
		return s;
	}

	return reverseString(s.substr(1)) + s.substring(0, 1);
}

console.log(reverseString("String"));
console.log(reverseString("abcde"));
console.log(reverseString("racercar"));