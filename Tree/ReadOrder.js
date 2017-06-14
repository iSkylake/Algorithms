function Node(value){
	this.value = value;
	this.left = null;
	this.right = null;
}

function readOrder(node){
	let queue = [node];
	while(queue.length > 0){
		let currentNode = queue.shift();
		console.log(currentNode.value);
		if(currentNode.left !== null){
			queue.push(currentNode.left);
		}
		if(currentNode.right !== null){
			queue.push(currentNode.right);
		}
	}
}

let a = new Node(8);
let b = new Node(1);
let c = new Node(5);
let d = new Node(2);
let e = new Node(3);
let f = new Node(6);
let g = new Node(4);
let h = new Node(7);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
d.left = f;
c.left = g;
g.right = h;

readOrder(a);