def kth_large_in_array(arr, k):
	if k > len(arr) - 1:
		return False
	mid = len(arr)//2
	pivot = arr[mid]
	left = 0
	right = len(arr) - 1
	while left < right:
		while arr[left] < pivot:
			left += 1
		while arr[right] > pivot:
			right += 1
		if arr[left] > arr[right]:
			arr[left], arr[right] = arr[right], arr[left]