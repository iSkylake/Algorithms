matrix = [
	[0, 0, 0, 1],
	[0, 0, 1, 1],
	[0, 1, 1, 1],
	[0, 1, 1, 1]
]

def oneMatrix(matrix):
	count = 0
	i = 0;
	j = len(matrix[0]) - 1
	col = len(matrix[0]) - 1

	while i < len(matrix):
		if matrix[i][j] == 0 or j == 0:
			if matrix[i][j] == 1 and j == 0:
				count += col + 1
			else:
				count += col - j
			i += 1
		elif matrix[i][j] == 1:
			j -= 1

	return count

print(oneMatrix(matrix))