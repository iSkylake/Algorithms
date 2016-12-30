from nose.tools import assert_equal

def selectionSort(arr):
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			minIndex = i
			if arr[j] < arr[i]:
				minIndex = j
			arr[i], arr[minIndex] = arr[minIndex], arr[i]
			print(arr)
	return arr

class Selection_Sort(object):
	def test(self, func):
		assert_equal(func([1, 7, 4, 2, 10, 8, 20, 3]), [1, 2, 3, 4, 7, 8, 10, 20])
		assert_equal(func([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
		print('TESTS PASSED')

t = Selection_Sort()
t.test(selectionSort)