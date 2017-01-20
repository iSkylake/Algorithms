# Given an array of integers and a target, return true if there's a subarray of consecutive elements that sum up to the target value

# Example:
#	[6, 12, 1, 7, 5, 2, 3], 14 => True
#	[7, 5, 1, 10], 30 => False

# Suggestion:
# Time: O(n)
# Space: O(1)

from nose.tools import assert_equal

def consecutive_sum(arr, target):
	total = 0
	for num in arr:
		if total + num == target:
			return True
		elif total + num < target:
			total = total + num
		else:
			total = num
	return False

class Consecutive_Sum(object):
	def test(self, func):
		assert_equal(func([1, 1, 5, 8], 2), True)
		assert_equal(func([1, 1, 5, 8], 6), True)
		assert_equal(func([1, 6, 2, 10], 1), True)
		assert_equal(func([1, 6, 2, 10], 20), False)
		assert_equal(func([5, 10, 2, 9], 26), True)
		print("TESTS PASSED")

t = Consecutive_Sum()
t.test(consecutive_sum)