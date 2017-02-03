function mostVowel(arr){
	var vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
	var maxVowel = 0;
	var maxCount = 0;
	for(var i=0;i<arr.length;i++){
		var vowelCount = 0;
		for(var j=0;j<arr[i].length;j++){
			if(arr[i][j].match(/[aeiouAEIOU]/g)){
				vowelCount++;
			}
		}
		if(vowelCount > maxCount){
			maxCount = vowelCount;
			maxVowel = i;
		}
	}
	console.log(maxVowel);
}

mostVowel(["Hello", "World", "aeoiu"]);