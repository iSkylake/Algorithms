from nose.tools import assert_equal

def mergeSort(arr):
	if len(arr) == 1:
		return arr
	else:
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]

		mergeSort(left)
		mergeSort(right)

		i, j, k = 0, 0, 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1

		while j < len(left):
			arr[k] = right[j]
			j += 1
			k += 1

	return arr

class Merge_Sort(object):
	def test(self, func):
		assert_equal(func([1, 7, 4, 2, 10, 8, 20, 3]), [1, 2, 3, 4, 7, 8, 10, 20])
		assert_equal(func([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
		print('TESTS PASSED')

t = Merge_Sort()
t.test(mergeSort)