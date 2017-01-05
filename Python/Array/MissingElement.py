# Given an array of N integers in a range [1... (N+1)], find the missing element

# Example:
#	[1, 3, 4] => 2
#	[8, 6, 7, 1, 2, 4, 3] => 5

# Suggestion:
# 	Time: O(n)
#	Space: O(1)

from nose.tools import assert_equal

def missing_element(arr):
	arr_sum = 0
	min_val, max_val = arr[0], arr[0]
	for num in arr:
		arr_sum += num
		if num < min_val:
			min_val = num
		elif num > max_val:
			max_val = num

	real_sum = (max_val*(max_val+1)//2) - (min_val-1)
	return real_sum - arr_sum

class Missing_Element(object):
	def test(self, func):
		assert_equal(func([1, 2, 3, 5, 6]), 4)
		assert_equal(func([5, 1, 4, 3]), 2)
		print('TESTS PASSED')

t = Missing_Element()
t.test(missing_element)