function coinChange(change, coins){
	var minChange = 0;
	var i = coins.length - 1;

	while(change > 0){
		if(coins[i] <= change){
			change -= coins[i];
			minChange++;
		} else {
			i--;
		}
	}

	return minChange;
}

console.log(coinChange(63, [1, 5, 10, 25]));