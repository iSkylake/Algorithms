def number_of_ones(arr):
	first = 0
	last = len(arr)
	mid = 0
	while first <= last:
		mid = mid + (last - first)//2
		if arr[mid] == 1 and arr[mid-1] == 0:
			return len(arr) - mid
		if arr[mid] == 0:
			first = mid
		else:
			last = mid
	return 0