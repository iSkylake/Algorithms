def consecutive_sum(arr, target):
	total = 0
	for num in arr:
		if total + num == target:
			return True
		elif total + num < target:
			total = total + num
		else:
			total = num
	return False