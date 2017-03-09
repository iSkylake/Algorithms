var familyTree = [
	{
		name: 'Alice',
		children: [
			{
				name: 'Georges',
				children: [
					{
						name: 'Bernard',
						children: []
					},
					{
						name: 'Jack',
						children: []
					}
				]
			}
		]
	},
	{
		name: 'Bob',
		children: [
			{
				name: 'Mary',
				children: []
			}
		]
	}
];

// This algorithm was inspired by the preorder binary tree traversal

function printTree(familyTree){

	// Helper function to traverse the tree
	function traversal(member, lvl){

		// print the name
		if(lvl < 1){
			console.log(member['name']); // This if statement was add because of ">"
		} else{
			console.log("--".repeat(lvl) + "> " + member['name']);
		}

		// Iterates and recurse until it gets to all children 
		for(var j=0; j<member['children'].length; j++){
			traversal(member['children'][j], lvl+1);
		}
		
	}

	// First iteration and traversal
	for(var i=0; i<familyTree.length; i++){
		traversal(familyTree[i], 0);
	}

}

printTree(familyTree);