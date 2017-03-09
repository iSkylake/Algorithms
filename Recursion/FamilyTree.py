family_tree = [
	{
		'name': 'Alice',
		'children': [
			{
				'name': 'Georges',
				'children': [
					{
						'name': 'Bernard',
						'children': []
					},
					{
						'name': 'Jack',
						'children': []
					}
				]
			}
		]
	},
	{
		'name': 'Bob',
		'children': [
			{
				'name': 'Mary',
				'children': []
			}
		]
	}
]

def print_tree(family_tree):

	def tranverse(member, lvl):

		if(lvl < 1):
			print(member['name'])
		else:
			print("--"*lvl + "> " + member['name'])

		for j in range(len(member['children'])):
			tranverse(member['children'][j], lvl+1)

	for i in range(len(family_tree)):
		tranverse(family_tree[i], 0)

print_tree(family_tree)