function DynArray(){
	this.array = new Array(2);
	this.capacity = 2;
	this.fill = 0;
}

DynArray.prototype.addSpace = function(){
	this.capacity *= 2;
	let tempArray = this.array;
	this.array = new Array(this.capacity);
	for(let i=0; i<this.fill; i++){
		this.array[i] = tempArray[i];
	}
}

DynArray.prototype.pushValue = function(value){
	if(this.fill >= this.capacity/2){
		this.addSpace();
	}
	this.array[this.fill] = value;
	this.fill++;
}

DynArray.prototype.size = function(){
	return this.fill;
}

DynArray.prototype.display = function(){
	let array = [];
	for(let i=0; i<this.fill; i++){
		array[i] = this.array[i];
	}
	return array;
}

DynArray.prototype.pop = function(){
	this.fill -= 1;
	let lastItem = this.array[this.fill];
	this.array[this.fill] = undefined; 
	return lastItem;
}

let dynArray = new DynArray();

console.log(dynArray.array);

dynArray.pushValue(1);

console.log(dynArray.array);

dynArray.pushValue(2);
console.log(dynArray.array);

dynArray.pushValue(3);
dynArray.pushValue(4);
dynArray.pushValue(5);
dynArray.pushValue(6);
console.log(dynArray.array);

console.log(dynArray.display());

console.log(dynArray.size());

console.log(dynArray.pop());
console.log(dynArray.display());
console.log(dynArray.pop());
console.log(dynArray.display());

dynArray.pushValue(7);
console.log(dynArray.display());
console.log(dynArray.size());