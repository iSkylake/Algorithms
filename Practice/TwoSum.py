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