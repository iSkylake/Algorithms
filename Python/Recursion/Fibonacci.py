from nose.tools import assert_equal

def fibonacci(n):
	if n <= 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

class Fibonacci:
	def test(self, func):
		assert_equal(func(6), 8)
		assert_equal(func(10), 55)
		assert_equal(func(0), 0)
		assert_equal(func(1), 1)
	print("TESTS PASSED")

t = Fibonacci()
t.test(fibonacci)