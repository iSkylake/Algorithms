def missing_element(arr):
	arr_sum = 0
	min_val, max_val = arr[0], arr[0]
	for num in arr:
		arr_sum += num
		if num < min_val:
			min_val = num
		elif num > max_val:
			max_val = num

	real_sum = (max_val*(max_val+1)//2) - (min_val-1)
	return real_sum - arr_sum