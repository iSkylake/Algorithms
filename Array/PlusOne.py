# Given an array of integers that represents an integer, add one to that number

# Example:
#	[1, 2, 3] => [1, 2, 4]
#	[9] => [1, 0]

# Suggestion: 
#	Time: O(n)
#	Space: O(1)

from nose.tools import assert_equal

def plus_one(arr):
	index = len(arr) - 1
	while index >= 0:
		if arr[index] < 9:
			arr[index] += 1
			return arr
		else:
			arr[index] = 0
			index -= 1
	arr.insert(0, 1)
	return arr

class Plus_One(object):
	def test(self, func):
		assert_equal(func([1, 0, 0]), [1, 0, 1])
		assert_equal(func([1, 0, 9]), [1, 1, 0])
		assert_equal(func([9]), [1, 0])
		print('TESTS PASSED')

t = Plus_One()
t.test(plus_one)