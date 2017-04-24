var matrix = [
	[0, 1, 1, 1, 1, 0],
	[0, 1, 0, 0, 1, 0],
	[1, 1, 0, 0, 1, 1],
	[0, 1, 1, 1, 1, 0],
	[0, 1, 0, 0, 1, 0],
]

function islandCoordinate(matrix){
	var coordinate = [];
	for(var i=0; i<matrix.length; i++){
		for(var j=0; j<matrix[i].length; j++){
			if(matrix[i][j] === 0){
				var row = i;
				var col = j;
				if(i === 0 && j === 0 || i === 0 && matrix[i][j-1] === 1 || j === 0 && matrix[i-1][j] === 1 || matrix[i-1][j] === 1 && matrix[i][j-1] === 1){
					coordinate.push(i.toString() + j.toString());
					while(col !== matrix[row].length-1 && matrix[row][col+1] !== 1){
						col++;
					}
					while(row !== matrix.length-1 && matrix[row+1][col] !== 1){
						row++;
					}
					coordinate.push(row.toString() + col.toString());
				}
			}
		}
	}
	return coordinate;
}

console.log(islandCoordinate(matrix));