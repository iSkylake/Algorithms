function threeSum(arr){
	arr.sort();
	l = arr.length;
	for(var i=0; i<l; i++){
		j = i+1;
		k = l;
		while(j < k){
			total = arr[i]+arr[j]+arr[k];
			if(total === 0){
				return true;
			} else if(total < 0){
				j++;
			} else{
				k--;
			}
		}
	}
	return false;
}

console.log(threeSum([5, 2, 1, 7, -5, 0]));
console.log(threeSum([5, 2, 1, 7, 0]));