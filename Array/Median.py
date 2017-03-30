from nose.tools import assert_equal

def median(arr1, arr2):
	i = j = k = 0

	while i < len(arr1) and j < len(arr2) and k < len(arr1) + 1:
		if k > 0:
			before = current
		if arr1[i] < arr2[j]:
			current = arr1[i]
			i += 1
		else:
			current = arr2[j]
			j += 1
		k += 1;

	while k < len(arr1) + 1:
		before = current
		if i < len(arr1):
			current = arr1[i]
			i += 1
		else:
			current = arr2[j]
			j += 1
		k += 1

	return (before + current)/2

class medianTest:
	def test(self, func):
		assert_equal(func([1, 12, 15, 26, 38], [2, 13, 17, 30, 45]), 16)
		assert_equal(func([1, 10, 13, 15], [2, 4, 6, 7]), 6.5)
		assert_equal(func([1], [5]), 3)
		print("TESTS PASSED")

t = medianTest()
t.test(median)