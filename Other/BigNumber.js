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
		let aSum = a[i] || 0;
		let bSum = b[i] || 0;
		let ab = aSum + bSum + extra;
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

let bigNum = new BigNumber('6537');

console.log(bigNum.add('9856'));