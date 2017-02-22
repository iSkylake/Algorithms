function palindrome(s){
	var mid = Math.floor(s.length/2);
	var left = mid - 1;
	var right = 0;
	if(s.length%2 == 0){
		right = mid;
	} else{
		right = mid + 1;
	}
	while(left >= 0 && right < s.length){
		if(s[left] !== s[right]){
			return false;
		}
		left--;
		right++;
	}
	return true;
}

console.log(palindrome("palindrome"));
console.log(palindrome("abccba"));
console.log(palindrome("abcba"));