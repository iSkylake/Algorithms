def coin_change(change, coins):
	min_coins = change
	if change in coins:
		return 1
	else:
		for i in [c for c in coins if c <= change]:
			num_coins = 1 + coin_change(change-i, coins)
			if num_coins < min_coins:
				min_coins = num_coins
	return min_coins

print(coin_change(25, [1, 5, 10]))