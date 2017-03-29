function Node(value){
	this.value = value;
	this.left = null;
	this.right = null;
}

function invertBT(node){
	if(node !== null){
		var temp = node.left;
		node.left = node.right;
		node.right = temp;
		invertBT(node.left);
		invertBT(node.right);
	}
}

var a = new Node(10);
var b = new Node(5);
var c = new Node(15);
var d = new Node(3);
var e = new Node(7);
var f = new Node(13);
var g = new Node(17);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.left = f;
c.right = g;

function traverseBT(node){
	if(node !== null){
		console.log(node.value);
		traverseBT(node.left);
		traverseBT(node.right);
	}
}

traverseBT(a);
invertBT(a);
traverseBT(a);