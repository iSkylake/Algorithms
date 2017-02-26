function longPalindrome(s){
	var palIndex = [];
	var maxPal = 0;
	for(i=1; i<s.length; i++){
		var l = i--;
		var r = i++;
		while(l >= 0){
			var current = 0;
			if(s[l] === s[r] && current >= palIndex){
				palIndex = [l, r];
				console.log(palIndex);
				maxPal = current;
				
			}
			l--;
			r++;
		}
	}
	maxPal++;
	return s.substring(palIndex[0], palIndex[1]+1);
}

console.log(longPalindrome("becauseabbcbbanot"));