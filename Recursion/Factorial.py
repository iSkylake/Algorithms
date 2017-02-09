from nose.tools import assert_equal

def factorial(n):
	if n < 1:
		return 1
	return n*factorial(n-1)

class Factorial(object):
	def test(self, func):
		assert_equal(func(1), 1)
		assert_equal(func(5), 120)
		assert_equal(func(10), 3628800)
		assert_equal(func(7), 5040)
		print("TESTS PASSED")

t = Factorial()
t.test(factorial)