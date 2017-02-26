function MinStack(){
	this.stack = [];
	this.min = [];
	this.len = 0;
}

MinStack.prototype.add = function(val){
	this.stack.push(val);
	if(this.len < 1){
		this.min.push(val);
	} else{
		this.min.push(Math.min(val, this.min[this.len-1]));
	}
	this.len++;
}

MinStack.prototype.delete = function(){
	this.stack.pop();
	this.min.pop();
	this.len--;
}

MinStack.prototype.minVal = function(){
	return this.min[this.len-1];
}

var ms = new MinStack();
ms.add(2);
ms.add(3);
ms.add(4);
ms.add(5);

console.log(ms.minVal());
ms.delete();
ms.delete();
ms.add(1);
console.log(ms.minVal());
ms.add(0);
console.log(ms.minVal());
ms.delete();
console.log(ms.minVal());
ms.delete();
console.log(ms.minVal());
ms.delete();
ms.delete();