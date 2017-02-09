function Node(value){
	this.value = value;
	this.next = null;
}

function validCirLL(node){
	var slow = node;
	var fast = node;
	while(fast.next.next != null && fast.next != null){
		slow = slow.next;
		fast = fast.next.next;
		if(slow.value === fast.value){
			return true;
		}
	}
	return false;
}

var a = new Node(1);
var b = new Node(2);
var c = new Node(3);
var d = new Node(4);

a.next = b;
b.next = c;
c.next = d;

var v = new Node(0);
var x = new Node(1);
var y = new Node(2);
var z = new Node(3);

v.next = x;
x.next = y;
y.next = z;
z.next = v;

console.log(validCirLL(a));
console.log(validCirLL(x));