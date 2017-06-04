function elevator(arrW, arrF, floor, maxCap, maxWeight){
	let move = 0;
	while(arrW.length > 0){
		let elevator = [];
		let weight = 0;
		let cap = 0;
		do{
			weight += arrW[0];
			cap += 1;	
			if(weight <= maxWeight && cap <= maxCap){
				if(!elevator.includes(arrF[0])){
					elevator.push(arrF[0]);
				}
				arrF.shift();
				arrW.shift();
			}		
		}while(weight <= maxWeight && cap <= maxCap)
		move = move + elevator.length + 1;
	}
	return move;
};

console.log(elevator([60, 80, 40], [2, 3, 5], 5, 2, 200)); //5
console.log(elevator([40, 40, 100, 80, 20], [3, 3, 2, 2, 3], 3, 5, 200)); //6