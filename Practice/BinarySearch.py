def binary_search(arr, target):
	mid = len(arr)//2
	print(mid)
	if arr[mid] == target:
		return True
	else:
		if arr[mid] < target:
			binary_search(arr[mid:], target)
		else:
			binary_search(arr[:mid], target)
	return False

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 5))