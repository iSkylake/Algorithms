function fibonacci(n){
	var a = 0;
	var b= 1;
	var c = 0;
	if(n===1){
		return 1;
	}
	for(var i=0;i<n-1;i++){
		c = a+b;
		a = b;
		b = c;
	}
	return c;
}

console.log(fibonacci(6));
console.log(fibonacci(1));
console.log(fibonacci(30));