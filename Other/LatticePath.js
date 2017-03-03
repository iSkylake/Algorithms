function latticePath(x, y){
	if(x === 0 && y === 0){
		return 1;
	}

	if(x < 0 || y < 0){
		return 0;
	}

	return latticePath(x-1, y) + latticePath(x, y-1);
}

console.log(latticePath(2, 2));
console.log(latticePath(0, 0));
console.log(latticePath(2, 3));