def kth_large_in_array(arr, k):
	if k > len(arr):
		return False
	new_k = len(arr) - k
	first = 0
	last = len(arr) - 1
	found = False
	while not found:
		mid = (first + last)//2
		left = first
		right = last
		pivot = arr[mid]
		while left < right:
			while arr[left] < pivot:
				left += 1
			while arr[right] > pivot:
				right -= 1
			if arr[left] > arr[right]:
				arr[left], arr[right] = arr[right], arr[left]
		if arr.index(pivot) == new_k:
			return pivot
		elif new_k > arr.index(pivot):
			first = arr.index(pivot) + 1
		else:
			last = arr.index(pivot) - 1

print(kth_large_in_array([3, 1, 6, 4, 9, 8], 1))
print(kth_large_in_array([1, 9, 5, 3], 5))