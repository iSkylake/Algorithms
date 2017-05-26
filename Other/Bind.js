let llorch = {
	name: "Llorch",
	shout: function(){
		console.log(this.name);
	}
};

function myBind(method, obj){
	return function(){
		return method.call(obj);
	}
};

let llorchShout = myBind(llorch.shout, llorch);
let hanaShout = myBind(llorch.shout, {name: "Hana"});

llorchShout();
hanaShout();