from nose.tools import assert_equal

def latticePath(x, y):
	if x == 0 and y == 0:
		return 1
	elif x < 0 or y < 0:
		return 0

	return latticePath(x-1, y) + latticePath(x, y-1)

class LatticePathTest:
	def test(self, func):
		assert_equal(func(2, 2), 6)
		assert_equal(func(0, 0), 1)
		assert_equal(func(3, 2), 10)
		print('TESTS PASSED')

t = LatticePathTest()
t.test(latticePath)