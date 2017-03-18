class Node:
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

def tree_height(root):
	height = 0

	def traverse(node, level):
		if node == None:
			return

		nonlocal height 
		height = max(height, level)

		traverse(node.left, level+1)
		traverse(node.right, level+1)

	traverse(root, height+1)

	return height

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)

a.left = b
b.left = c
a.right = d
d.left = e
d.right = f
f.right = g

print(tree_height(a))