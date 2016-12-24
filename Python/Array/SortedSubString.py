from nose.tools import assert_equal

def sort_sub_string(arr):
	left, max_val = 0, arr[0]
	right, min_val = len(arr) - 1, arr[len(arr) - 1]

	for i in range(len(arr)):
		if arr[i] > max_val:
			max_val = arr[i]

		if arr[i] < max_val:
			right = i

	for i in range(len(arr)-1, -1, -1):
		if arr[i] < min_val:
			min_val = arr[i]

		if arr[i] > min_val:
			left = i

	return [left, right]

# [3,4,8,7,10,6,17]
# [3,4,8,7,20,6,17]

class Sort_Sub_String(object):
	def test(self, func):
		assert_equal(func([3, 4, 8, 7, 10, 6, 17]), [2, 5])
		assert_equal(func([3, 4, 8, 7, 20, 6, 17]), [2, 6])
		print('TEST PASSED')

t = Sort_Sub_String()
t.test(sort_sub_string)