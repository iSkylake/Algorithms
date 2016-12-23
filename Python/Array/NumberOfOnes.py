from nose.tools import assert_equal

def number_of_ones(arr):
	first = 0
	last = len(arr) - 1
	while first <= last:
		mid = (last + first)//2
		if arr[mid] == 1 and arr[mid-1] == 0:
			return len(arr) - mid
		if arr[mid] == 0:
			first = mid + 1
		else:
			last = mid - 1
	return 0

class Number_of_Ones(object):
	def test(self, func):
		assert_equal(func([0, 0, 0, 1, 1, 1]), 3)
		assert_equal(func([0, 0, 0, 0, 0, 0, 0, 0]), 0)
	print('TESTS PASSED')

t = Number_of_Ones()
t.test(number_of_ones)