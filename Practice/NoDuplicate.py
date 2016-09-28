def remove_duplicate(arr):
	result = []
	for num in arr:
		if num not in result:
			result.append(num)
	return len(result)