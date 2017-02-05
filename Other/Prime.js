function prime(n){
	var count = 0;
	var nums = [2, 3, 5, 7];
	nums.forEach(function(num){
		if(n%num==0){
			count ++;
		}
	});
	if(count == 0 || n == 1 || n === 2 || n === 3 || n === 5 || n === 7){
		console.log("Is a prime");
	} else{
		console.log("Not a prime");
	}
}

prime(1);
prime(5);
prime(20);
prime(50);
prime(17);