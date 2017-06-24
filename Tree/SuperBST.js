function BST(){
	this.root = null;
	this.size = 0;
}

function Node(value){
	this.value = value;
	this.left = null;
	this.right = null;
}

BST.prototype.add = function(value){
	let newNode = new Node(value);
	if(this.size < 1){
		this.root = newNode;
	} else {
		let currentNode = this.root;
		let prevNode = this.root;
		while(currentNode !== null){
			prevNode = currentNode;
			if(value < currentNode.value){
				currentNode = currentNode.left;
			} else {
				currentNode = currentNode.right;
			}
		}
		if(value < prevNode.value){
			prevNode.left = newNode;
		} else {
			prevNode.right = newNode;
		}
	}
	this.size++;
};

function superBST(root){
	let prev = 0;
	function traverse(node){
		if(node !== null){
			traverse(node.right);
			node.value += prev;
			prev = node.value;
			traverse(node.left);
		}
	}
	traverse(root);
};

let bst = new BST();
bst.add(10);
bst.add(5);
bst.add(1);
bst.add(15);

console.log(bst.root);
superBST(bst.root);
console.log(bst.root);