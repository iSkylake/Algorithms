function waterFall(arr){
	let left = 0;
	let right = arr.length-1;
	let water = [];
	for(let i=0; i< arr.length; i++){
		water.push(0);
	}
	let wall = 0;
	let current = 0;
	let direction = "";
	while(left < right){
		if(arr[left] < arr[right]){
			wall = left;
			current = wall + 1;
			direction = "left";
		} else {
			wall = right;
			current = wall - 1;
			direction = "right";
		}
		while(arr[current] < arr[wall]){
			water[current] = arr[wall] - arr[current];
			if(direction === "left"){
				current++;
			} else {
				current--;
			}
		}		
		if(direction === "left"){
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