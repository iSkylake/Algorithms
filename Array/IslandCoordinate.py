matrix = [
	[0, 1, 1, 1, 1, 0],
	[0, 1, 0, 0, 1, 0],
	[1, 1, 0, 0, 1, 1],
	[0, 1, 1, 1, 1, 0],
	[0, 1, 0, 0, 1, 0],
]

def islandCoordinate(matrix):
	coordinates = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			
			if matrix[i][j] == 0:
				if i == 0 and j == 0 or i == 0 and matrix[i][j-1] == 1 or j == 0 and matrix[i-1][j] == 1 or matrix[i-1][j] == 1 and matrix[i][j-1] == 1:
					coordinates.append(str(i) + str(j))
					row = i
					col = j

					while col != len(matrix[row])-1 and matrix[row][col+1] != 1:
						col += 1
					while row != len(matrix)-1 and matrix[row+1][col] != 1:
						row += 1

					coordinates.append(str(row) + str(col))

	return coordinates

print(islandCoordinate(matrix))