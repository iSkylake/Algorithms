class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def lowest(root, first_value, second_value):
	first_search = []
	second_search = []
	found1 = False
	found2 = False
	
	def traverse(node, first_value):
		nonlocal first_search
		nonlocal found1
		if node == None or found1:
			return
		
		first_search.append(node.value)
		if node.value == first_value:
			found1 = True
		traverse(node.left, first_value)
		traverse(node.right, first_value)
		if not found1:
			first_search.pop()
	traverse(root, first_value)
	# print(first_search)

	def traverse(node, second_value):
		nonlocal second_search
		nonlocal found2
		if node == None or found2:
			return
		
		second_search.append(node.value)
		if node.value == second_value:
			found2 = True
		traverse(node.left, second_value)
		traverse(node.right, second_value)
		if not found2:
			second_search.pop()
	traverse(root, second_value)

	for i in range(len(second_search)):
		if second_search[i] in first_search:
			lowest_common_ancestor = second_search[i]

	return lowest_common_ancestor

a = Node(5)
b = Node(2)
c = Node(7)
d = Node(4)
e = Node(8)
f = Node(9)

a.left = b
a.right = c
c.left = d
c.right = e
e.right = f

print(lowest(a, 4, 9))