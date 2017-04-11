def island(matrix):
	island_count = 0

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == 1:
				if i == len(matrix)-1 and j == len(matrix[i])-1 or j == len(matrix[i])-1 and matrix[i+1][j] == 0 or i == len(matrix)-1 and matrix[i][j+1] == 0 or matrix[i+1][j] == 0 and matrix[i][j+1] == 0:
					island_count += 1
	return island_count

map1 = [
	[1, 1, 0, 1],
	[1, 1, 0, 1],
	[0, 0, 1, 0],
	[0, 0, 1, 0]
]

print(island(map1))