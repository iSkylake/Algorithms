# Implementation of a Binary Search

from nose.tools import assert_equal

# Using recursion
def binary_search_recursion(arr, target):
	if len(arr) > 0:
		mid = len(arr)//2
		print(arr[mid])
		if arr[mid] == target:
			return True
		if target < arr[mid]:
			return binary_search_recursion(arr[:mid], target)
		else:
			return binary_search_recursion(arr[mid+1:], target)
	else:
		return False

# Using iteration
def binary_search_iteration(arr, target):
	first = 0
	last = len(arr) - 1
	while first <= last:
		mid = first + last
		if arr[mid] == target:
			return True
		else:
			if target < arr[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return False

# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 1))

class Binary_Search(object):
	def test(self, func):
		assert_equal(func([1, 2, 3, 4, 5, 6, 7, 8], 1), True)
		assert_equal(func([1, 2, 3, 4, 5, 6, 7, 8], 4), True)
		assert_equal(func([1, 2, 3, 4, 5, 6, 7, 8], 0), False)
		assert_equal(func([1, 2, 3, 4, 5, 6, 7, 8], 9), False)
		assert_equal(func([1, 2, 3, 4, 6, 7, 8], 5), False)
		print('TESTS PASSED')

t = Binary_Search()
t.test(binary_search_recursion)
t.test(binary_search_iteration)