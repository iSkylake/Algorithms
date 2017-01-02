from nose.tools import assert_equal

def two_sum(arr, target):
	dict_sum = {}
	for i in range(len(arr)):
		if arr[i] not in dict_sum:
			total = target - arr[i]
			dict_sum[total] = i
		else:
			result = [dict_sum[arr[i]], i]
			return result
	result = [-1, -1]
	return result

class Two_Sum(object):
	def test(self, func):
		assert_equal(func([1, 6, -5, 7, 3], -2), [2, 4])
		assert_equal(func([1, 9, 10], 8), [-1, -1])
		print("TESTS PASSED")

t = Two_Sum()
t.test(two_sum)