def sort_sub_string(arr):
	left = 0
	right = len(arr) - 1
	minIndex = 0
	maxIndex = len(arr)-1
	while left < right :
		if arr[left] > arr[left+1] and arr[left] >= arr[minIndex]:
			sub_left = left
			print(left)
		else:
			sub_left = minIndex
		if arr[right] < arr[right-1] and arr[right] <= arr[maxIndex]:
			sub_right = right
			print(right)
		else:
			sub_right = maxIndex
			print("WAHT!? ", right)
		left += 1
		right -= 1
	return [sub_left, sub_right]
