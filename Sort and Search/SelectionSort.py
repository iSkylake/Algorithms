from nose.tools import assert_equal

def selectionSort(arr):
	for i in range(len(arr)):
		minIndex = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[minIndex]:
				minIndex = j
		arr[i], arr[minIndex] = arr[minIndex], arr[i]
	return arr

class Selection_Sort(object):
	def test(self, func):
		assert_equal(func([1, 7, 4, 2, 10, 8, 20, 3]), [1, 2, 3, 4, 7, 8, 10, 20])
		assert_equal(func([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
		print('TESTS PASSED')

t = Selection_Sort()
t.test(selectionSort)