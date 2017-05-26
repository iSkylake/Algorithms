let llorch = {
	name: "Llorch",
	shout: function(){
		console.log(this.name);
	}
};

function myBind(){
	let method = arguments[0];
	let obj = arguments[1];
	let rem = [];
	if(arguments.length > 2){
		for(let i=2; i<arguments.length; i++){
			rem.push(arguments[i]);
		}
	};

	return function(){
		if(arguments.length > 0){
			for(let i=0; i<arguments.length; i++){
				rem.push(arguments[i]);
			};
		};
		return method.apply(obj, rem);
	}
};

let llorchShout = myBind(llorch.shout, llorch);
let hanaShout = myBind(llorch.shout, {name: "Hana"});

llorchShout();
hanaShout();

function foobar(a, b){
	console.log(a+b);
};

let addFooBar = myBind(foobar, null, 'foo');
addFooBar('bar');