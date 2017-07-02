function waterFall(arr){
	let left = 0;
	let right = arr.length-1;
	let water = [];
	for(let i=0; i< arr.length; i++){
		water.push(0);
	}
	let wall = 0;
	let current = 0;
	while(left < right){
		if(arr[left] < arr[right]){
			wall = left;
			current = wall + 1;
		} else {
			wall = right;
			current = wall - 1;
		}
		while(arr[current] < arr[wall]){
			water[current] = arr[wall] - arr[current];
			if(wall === left){
				current++;
			} else {
				current--;
			}
		}		
		if(wall === left){
			left = current;
		} else {
			right = current;
		}
	}
	console.log(water);
}

waterFall([3, 0, 2, 1, 4]);
waterFall([3, 1, 1, 1, 1]);
waterFall([3, 0, 5, 1, 4]);
waterFall([3, 0, 5, 1, 3]);