def insertion_sort(arr):
	for i in range(len(arr)):
		k = i
		while(k > 0 and arr[k] < arr[k-1]):
			arr[k], arr[k-1] = arr[k-1], arr[k]
			k -= 1
	return arr

print(insertion_sort([5, 4, 1, 9, 7, 6]))
