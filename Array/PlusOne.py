def plus_one(arr):
	index = len(arr) - 1
	while index >= 0:
		if arr[index] < 9:
			arr[index] += 1
			return arr
		else:
			arr[index] = 0
			index -= 1
	arr.insert(0, 1)
	return arr