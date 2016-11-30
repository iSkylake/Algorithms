def sorted_2_sum(arr, target):
	left = 0
	right = len(arr) - 1
	while left < right:
		sum_num = arr[left] + arr[right]
		if sum_num == target:
			return [left, right]
		if sum_num > target:
			right -= 1
		else:
			left -= 1
	return [-1, -1]