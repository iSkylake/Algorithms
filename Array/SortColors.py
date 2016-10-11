def sort_colors(arr):
	colors = [0, 0, 0]
	for num in arr:
		colors[num] += 1

	j = 0
	for i in range(len(colors)):
		while colors[i] > 0:
			arr[j] = i
			j += 1
			colors[i] -= 1
	return arr