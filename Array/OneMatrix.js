matrix = [
	[0, 0, 0, 1],
	[0, 0, 1, 1],
	[0, 1, 1, 1],
	[1, 1, 1, 1]
];

function matrixOne(matrix){
	var count = 0;
	var i = 0;
	var j = matrix.length - 1;
	var col = matrix.length - 1;
	
	while(i < matrix.length){
		if(matrix[i][j] == 0 || j == 0){
			if(j == 0 && matrix[i][j] == 1){
				count += matrix.length;
			} else{
				count += col - j;
			}
			i++;
		} else{
			j--;
		}
	}

	return count;
}

console.log(matrixOne(matrix));