function Node(value){
	this.value = value;
	this.left = null;
	this.right = null;
}

function treeHeight(root){

	var height = 0;

	function traverse(node, level){
		if(node === null){
			return;
		}

		height = Math.max(level, height);

		traverse(node.left, level+1);
		traverse(node.right, level+1);
	}

	traverse(root, height+1)

	return height;
}

var a = new Node(1);
var b = new Node(2);
var c = new Node(3);
var d = new Node(4);
var e = new Node(5);

a.left = b;
a.right = c;
b.left = d;
d.right = e;

console.log(treeHeight(a));