from nose.tools import assert_equal

def bubbleSort(arr):
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[j] < arr[i]:
				arr[i], arr[j] = arr[j], arr[i]
	return arr

class Bubble_Sort(object):
	def test(self, func):
		assert_equal(func([1, 7, 4, 2, 10, 8, 20, 3]), [1, 2, 3, 4, 7, 8, 10, 20])
		assert_equal(func([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
		print('TESTS PASSED')

t = Bubble_Sort()
t.test(bubbleSort)