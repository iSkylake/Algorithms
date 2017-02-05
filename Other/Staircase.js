function staircase(n){
	for(var i=1; i<n+1; i++){
		var level = "";
		for(var j=0; j<n-i; j++){
			level += " ";
		}
		for(var k=0; k<i; k++){
			level += "#";
		}
		console.log(level);
	}
}

staircase(5);

function easyStaircase(n){
	for(var i=0; i<n+1; i++){
		var level = "";
		for(var j=0; j<i; j++){
			level += "#";
		}
		console.log(level);
	}
}

easyStaircase(5);