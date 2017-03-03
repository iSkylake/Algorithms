function colorSort(arr){
	var colors = {0:0, 1:0, 2:0};
	var order = [];
	for(i=0; i<arr.length; i++){
		colors[arr[i]] += 1;
	}

	for(i=0; i<3; i++){
		while(colors[i] > 0){
			order.push(i);
			colors[i]--;
		}
	}
	console.log(order);
}

colorSort([0, 2, 0, 1, 2, 1]);