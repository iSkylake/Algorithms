function BigNumber(value){
	this.value = value;
};

BigNumber.prototype.add = function(value){
	let a = this.value.split("").reverse().map(Number);
	let b = value.split("").reverse().map(Number);
	let maxLen = Math.max(a.length, b.length);
	let sum = [];
	let extra = 0;
	for(let i=0; i<maxLen; i++){
		a[i] = a[i] || 0;
		b[i] = b[i] || 0;
		let ab = a[i] + b[i] + extra;
		if(ab > 9){
			extra = 1;
			ab -= 10;
		} else {
			extra = 0;
		}
		sum.push(ab);
	}
	if(extra > 0){
		sum.push(1);
	}
	sum = sum.reverse().join("");
	return sum;
};

BigNumber.prototype.substract = function(value){
	let a = this.value.split("").reverse().map(Number);
	let b = value.split("").reverse().map(Number);
	let maxLen = Math.max(a.length, b.length);
	let sub = [];
	for(let i=0; i<maxLen; i++){
		a[i] = a[i] || 0;
		b[i] = b[i] || 0;
		if(a[i]<b[i]){
			a[i]+=10;
			a[i+1] -= 1;
		}
		sub.push(a[i]-b[i]);
	}
	let index = sub.length-1;
	while(sub[index]===0){
		sub.pop();
		index--;
	}
	if(sub.length === 0){
		return "0";
	} else {
		sub = sub.reverse().join("");	
	}
	
	return sub;
}

let bigNum = new BigNumber('6537');

console.log(bigNum.add('9856'));
console.log(bigNum.substract('4671'));
console.log(bigNum.substract('5671'));
console.log(bigNum.substract('6537'));