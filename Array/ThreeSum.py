from nose.tools import assert_equal

def threeSum(arr):
	arr = sorted(arr)
	l = len(arr)
	for i in range(l):
		j = i+1
		k = l-1
		while j < k:
			total = arr[i] + arr[j] + arr[k]
			if total == 0:
				return True
			elif total < 0:
				j += 1
			else:
				k -= 1
	return False

class ThreeSum(object):
	def test(self, func):
		assert_equal(func([9, 2, 1, 7, -5, -2, 8]), True)
		assert_equal(func([5, 2, 1, 0, 4]), False)
		assert_equal(func([5, 0, 6, 1, -6, 2]), True)
		print("TESTS PASSED")

t = ThreeSum()
t.test(threeSum)