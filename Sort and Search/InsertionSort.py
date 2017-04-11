from nose.tools import assert_equal

def insertion_sort(arr):
	for i in range(len(arr)):
		k = i
		while(k > 0 and arr[k] < arr[k-1]):
			arr[k], arr[k-1] = arr[k-1], arr[k]
			k -= 1
	return arr

class Sort_Test:
	def test(self, func):
		assert_equal(func([5, 4, 1, 9, 7, 6]), [1, 4, 5, 6, 7, 9])
		assert_equal(func([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
		assert_equal(func([9, 7, 5, 3, 2, 1]), [1, 2, 3, 5, 7, 9])
		print('TESTS PASSED')

t = Sort_Test()
t.test(insertion_sort)