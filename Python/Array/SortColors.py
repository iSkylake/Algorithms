from nose.tools import assert_equal

def sort_colors(arr):
	colors = [0, 0, 0]
	for num in arr:
		colors[num] += 1

	j = 0
	for i in range(len(colors)):
		while colors[i] > 0:
			arr[j] = i
			j += 1
			colors[i] -= 1
	return arr

class Sort_Colors(object):
	def test(self, func):
		assert_equal(func([2, 0, 1, 2, 1, 0]), [0, 0, 1, 1, 2, 2])
		assert_equal(func([1, 0, 2]), [0, 1, 2])
		print("TESTS PASSED")

t = Sort_Colors()
t.test(sort_colors)