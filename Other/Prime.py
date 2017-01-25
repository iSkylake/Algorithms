from nose.tools import assert_equal

def prime(num):
	primes = [2, 3, 5, 7]
	count = 0
	if num in primes:
		return True
	for n in primes:
		if num%n == 0:
			count += 1
	if count == 0:
		return True
	else:
		return False

class Prime(object):
	def test(self, func):
		assert_equal(func(2), True)
		assert_equal(func(7), True)
		assert_equal(func(11), True)
		assert_equal(func(41), True)
		assert_equal(func(4), False)
		assert_equal(func(50), False)
		print("TESTS PASSED")

t = Prime()
t.test(prime)