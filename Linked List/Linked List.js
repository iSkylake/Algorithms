function Node(value){
	this.value = value;
	this.next = null;
}

function LinkedList(){
	this.head = null;
	this.tail = null;
	this.size = 0;
}

LinkedList.prototype.push = function(value){
	var currentNode = this.head;
	var newNode = new Node(value);
	if(this.size === 0){
		this.head = newNode;
	} else{
		while(currentNode.next != null){
			currentNode = currentNode.next;
		}
		currentNode.next = newNode;
	}
	this.tail = newNode;
	this.size++;
}

LinkedList.prototype.delete = function(value){
	var currentNode = this.head;
	var previousNode;
	var found = false;
	if(value == this.head.value){
		this.head = this.head.next;
		this.size--;
	} else{
		while(found === false && currentNode !== null){
			if(value === currentNode.value){
				found = true;
			}
			else{
				previousNode = currentNode;
				currentNode = currentNode.next;
			}
		}
		if(found === true){
			if(currentNode.next === null){
				previousNode.next = null;
				this.tail = previousNode;
			} else{
				previousNode.next = currentNode.next;
				currentNode.next = null;
			}
			this.size--;
		}
	}
}

var ll = new LinkedList();
ll.push(1);
ll.push(2);
ll.push(3);
ll.push(4);

console.log(ll.head);
console.log(ll.tail);
console.log(ll.size);