function islandCount(matrix){
	var island = 0;
	for(i=0; i<matrix.length; i++){
		for(j=0; j<matrix[i].length; j++){
			if(matrix[i][j] === 1){
				if(i === matrix.length-1 && j === matrix[i].length-1 || i === matrix.length-1 && matrix[i][j+1] == 0 || j === matrix[i].length-1 && matrix[i+1][j] == 0 || matrix[i][j+1] === 0 && matrix[i+1][j] === 0 || matrix[i+1][j] === 0 && matrix[i][j+1] === 0){
					island++;
				}
			}
		}
	}
	return island;
}
	

var map = [	[1, 1, 0, 1],
			[1, 1, 0, 1],
			[0, 0, 1, 0],
			[0, 0, 1, 0] ]

console.log(islandCount(map));