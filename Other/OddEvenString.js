function oddEvenString(str){
	var odd = "";
	var even = "";
	for(var i=0; i<str.length; i++){
		if(i%2==0){
			even += str[i];
		} else{
			odd += str[i];
		}
	}
	console.log(even + " " + odd);
}

oddEvenString("Hello");
oddEvenString("World");