matrix = [
	[0, 0, 0, 1],
	[0, 0, 1, 1],
	[0, 1, 1, 1],
	[1, 1, 1, 1]
]

def oneMatrix(matrix):
	i = count = 0
	j = col = len(matrix[0]) - 1;
	while i <  len(matrix):
		if matrix[i][j] == 0 or j == 0:
			count = count + col - j
			i += 1
		else:
			j -= 1
	return count

print(oneMatrix(matrix))