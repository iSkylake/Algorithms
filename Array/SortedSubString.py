def sort_sub_string(arr):
	left, max_val = 0, arr[0]
	right, min_val = len(arr) - 1, arr[len(arr) - 1]

	for i in range(len(arr)):
		if arr[i] > max_val:
			max_val = arr[i]

		if max_val < arr[i]:
			right = i

	for i in range(len(arr)-1, -1, -1):
		if arr[i] < min_val:
			min_val = arr[i]

		if min_val < arr[i]:
			left = i

	return [left, right]

# [3,4,8,7,10,6,17]
# [3,4,8,7,20,6,17]