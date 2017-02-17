function Node(value){
	this.value = value;
	this.left = null;
	this.right = null;
}

function validBST(head){
	var nodes = [];
	function helper(node){
		if(!node){
			return;
		}
		helper(node.left);
		nodes.push(node.value);
		helper(node.right);
	}
	helper(head);
	for(var i=1; i<nodes.length; i++){
		if(nodes[i] < nodes[i-1]){
			return false;
		}
	}
	return true;
}

var a = new Node(20);
var b = new Node(10);
var c = new Node(30);
var d = new Node(5);
var e = new Node(7);

a.left = b;
a.right = c;
b.left = d;
d.right = e;

console.log(validBST(a)); 