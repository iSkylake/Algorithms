from nose.tools import assert_equal

# def coin_change(change, coins):
# 	min_coins = change
# 	if change in coins:
# 		return 1
# 	else:
# 		for i in [c for c in coins if c <= change]:
# 			num_coins = 1 + coin_change(change-i, coins)
# 			if num_coins < min_coins:
# 				min_coins = num_coins
# 	return min_coins

# print(coin_change(25, [1, 5, 10]))

def coin_change(change, coins):
	memo = [0]*(change+1)

	def dyn_coin_change(change, coins, memo):
		if memo[change] != 0:
			return memo[change]
		elif change in coins:
			memo[change] = 1
			return 1

		min_coins = change

		for i in [c for c in coins if c <= change]:
			num_coins = 1 + dyn_coin_change(change-i, coins, memo)
			if num_coins < min_coins:
				min_coins = num_coins
				memo[change] = min_coins

		return min_coins

	return dyn_coin_change(change, coins, memo)

class Coin_Change_Test:
	def test(self, func):
		assert_equal(func(63, [1, 5, 10, 25]), 6)
		assert_equal(func(25, [1, 5, 10]), 3)
		assert_equal(func(10, [1, 5, 10]), 1)
		assert_equal(func(20, [1]), 20)
		print('TESTS PASSED')

t = Coin_Change_Test()
t.test(coin_change)