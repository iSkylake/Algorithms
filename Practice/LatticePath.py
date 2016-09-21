def latticePath(x, y):
	if x == 0 and y == 0:
		return 1
	elif x < 0 or y < 0:
		return 0

	return latticePath(x-1, y) + latticePath(x, y-1)