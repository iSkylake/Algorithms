def threeSum(arr):
	arr = sorted(arr)
	l = len(arr)
	for i in range(l):
		j = i+1
		k = l-1
		while j < k:
			total = arr[i] + arr[j] + arr[k]
			if total == 0:
				return True
			elif total < 0:
				j += 1
			else:
				k -= 1
	return False