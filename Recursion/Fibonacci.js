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

function fiboRec(n){
	if(n <= 1){
		return n;
	}
	return fiboRec(n-1) + fiboRec(n-2);
}

var mem = {};

function fiboMem(n){	
	if(n <= 1){
		return n;
	}
	if(n in mem){
		return mem[n];
	}
	mem[n] = fiboMem(n-1) + fiboMem(n-2)
	return mem[n];
}

console.log(fibonacci(6));
console.log(fibonacci(1));
console.log(fibonacci(30));

console.log(fiboRec(6));
console.log(fiboRec(1));
console.log(fiboRec(30));

console.log(fiboMem(6));
console.log(fiboMem(1));
console.log(fiboMem(30));