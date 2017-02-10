function Node(value){
	this.value = value;
	this.left = null;
	this.right = null;
}

function BST(){
	this.head = null;
	this.size = 0;
}

BST.prototype.insert = function(value){
	var newNode = new Node(value);
	if(this.size < 1){
		this.head = newNode;
	} else{
		var currentNode = this.head;
		var prevNode = null;
		while(currentNode !== null && currentNode !== null){
			prevNode = currentNode;
			if(value < currentNode.value){
				currentNode = currentNode.left;
			} else{
				currentNode = currentNode.right;
			}
		}
		if(value < prevNode.value){
			prevNode.left = newNode;
		} else{
			prevNode.right = newNode;
		}
	}
	this.size++;
}

var tree = new BST();
tree.insert(20);
tree.insert(10);
tree.insert(5);
tree.insert(15);
tree.insert(30);
