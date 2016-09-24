def selectionSort(arr):
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			minIndex = i
			if arr[j] < arr[i]:
				minIndex = j
			arr[i], arr[minIndex] = arr[minIndex], arr[i]
			print(arr)
	return arr