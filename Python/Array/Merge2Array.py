from nose.tools import assert_equal

def merge_2_array(arr1, arr2):
	result = []
	i, j = 0, 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i] <= arr2[j]:
			result.append(arr1[i])
			i += 1
		else:
			result.append(arr2[j])
			j += 1
	
	while i < len(arr1):
		result.append(arr1[i])
		i += 1

	while j < len(arr2):
		result.append(arr2[j])
		j += 1

	# if i > j:
	# 	result + arr1
	# else:
	# 	result + arr2

	return result

class Merge_2_Array(object):
	def test(self, func):
		assert_equal(func([1, 5, 7, 8], [2, 3, 4, 10]), [1, 2, 3, 4, 5, 7, 8, 10])
		print("TEST PASSED")

t = Merge_2_Array()
t.test(merge_2_array)