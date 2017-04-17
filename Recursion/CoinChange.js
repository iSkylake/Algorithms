function coinChange(change, coins){
	for(var i=0; i<coins.length; i++){
		if(change === coins[i]){
			return 1;
		}
	}

	var min_coins = change;

	for(var i=0; i<coins.length; i++){
		if(i <= change){
			var num_coins = 1 + coinChange(change-i, coins);
			if(num_coins < min_coins){
				min_coins = num_coins;
			}
		}
	}
	return min_coins;
}

console.log(coinChange(25, [25]))