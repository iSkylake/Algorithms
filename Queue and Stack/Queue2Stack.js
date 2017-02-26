function Queue(){
	this.fill = [];
	this.drop = [];
}

Queue.prototype.enqueue = function(val){
	this.fill.push(val);
}

Queue.prototype.dequeue = function(){
	if(this.drop.length === 0){
		var len = this.fill.length;
		for(var i=0; i<len; i++){
			this.drop.push(this.fill.pop());
		}
	}
	return this.drop.pop();
}

var queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);
queue.enqueue(4);

console.log(queue.dequeue());
console.log(queue.dequeue());

queue.enqueue(5);
queue.enqueue(6);
console.log(queue.dequeue());
console.log(queue.dequeue());
console.log(queue.dequeue());
console.log(queue.dequeue());