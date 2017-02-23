function Palindrome(){
	this.stack = [];
	this.queue = [];
}

Palindrome.prototype.fillStackQueue = function(s){
	for(var i=0; i<s.length; i++){
		this.queue.push(s[i]);
		this.stack.push(s[i]);
	}
}

Palindrome.prototype.dequeue = function(){
	return this.queue.shift();
}

Palindrome.prototype.stackPop = function(){
	return this.stack.pop();
}

Palindrome.prototype.check = function(s){
	s = s.toLowerCase();
	this.fillStackQueue(s);
	for(var i=0; i<s.length; i++){
		if(this.dequeue() !== this.stackPop()){
			this.stack = [];
			this.queue = [];
			return false;
		}
	}
	return true;
}

var pal = new Palindrome();
console.log(pal.check("Palindrome"));
console.log(pal.check("Madam"));
console.log(pal.check("rotator"));