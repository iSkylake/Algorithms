def binary_search(arr, target):
	if len(arr) > 0:
		mid = len(arr)//2
		print(arr[mid])
		if arr[mid] == target:
			return True
		if target < arr[mid]:
			return binary_search(arr[:mid], target)
		else:
			return binary_search(arr[mid+1:], target)
	else:
		return False

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 1))

