function longPalindrome(s){
	var maxIndex = [];
	var maxPal = 0;
	// Check for odd palindromes
	for(i=1; i<s.length; i++){
		var palIndex = [];
		var current = 1;
		var l = i - 1;
		var r = i + 1;
		while(s[l] === s[r] && l >= 0){
			current += 2;
			palIndex = [l, r];
			l--;
			r++;
		}
		if(current > maxPal){
			maxPal = current;
			maxIndex = palIndex;
		}
	}
	// Check for even palindromes
	for(i=1; i<s.length; i++){
		var palIndex = [];
		var current = 0;
		var l = i;
		var r = i + 1;
		while(s[l] === s[r] && l >= 0){
			current += 2;
			palIndex = [l, r];
			l--;
			r++;
		}
		if(current > maxPal){
			maxPal = current;
			maxIndex = palIndex;
		}
	}
	return s.substring(maxIndex[0], maxIndex[1]+1);
}

console.log(longPalindrome("becauseabbcbbanot"));
console.log(longPalindrome("becauseabbccbbanot"));