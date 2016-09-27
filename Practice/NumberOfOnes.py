def number_of_ones(arr):
	first = 0
	last = len(arr) - 1
	while first <= last:
		mid = (last + first)//2
		if arr[mid] == 1 and arr[mid-1] == 0:
			return len(arr) - mid
		if arr[mid] == 0:
			first = mid + 1
		else:
			last = mid - 1
	return 0
