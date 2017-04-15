from nose.tools import assert_equal

def coin_change(change, coins):
	min_coin = 0
	i = len(coins) - 1

	while change > 0:
		if coins[i] <= change:
			change -= coins[i]
			min_coin += 1
		else:
			i -= 1

	return min_coin

print(coin_change(63, [1, 5, 10, 25]))

class Coin_Change_Test:
	def test(self, func):
		assert_equal(func(25, [1, 5, 10]), 3)
		assert_equal(func(63, [1, 5, 10, 25]), 6)
		assert_equal(func(10, [1]), 10)
		print('TESTS PASSED')

t = Coin_Change_Test()
t.test(coin_change)