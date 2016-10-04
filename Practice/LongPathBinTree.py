class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Binary_Tree:
	def __init__(self):
		self.root = None
		self.size = 0

def long_path(root):
	count = 0
	def _long_path(node, count):
		if node == None:
			print(count)
			return
		count += 1
		_long_path(node.left, count)
		count -= 1
		_long_path(node.right, count)

	_long_path(root, count)

bin_tree = Binary_Tree()
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

bin_tree.root = a
a.left = b
a.right = c
b.left = d
b.right = e
e.right = f
f.left = h
c.right = g

long_path(a)