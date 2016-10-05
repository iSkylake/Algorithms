class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None
		self.size = 0

	# def insert(self, val):
	# 	new_node = Node(val)
	# 	if self.size < 1:
	# 		self.root = new_node
	# 	else:
	# 		found = False
	# 		node = self.root
	# 		while not found:
	# 			if val < node.val:


def kth_large_BST(root, k):
	count = 0
	val = 0
	def traverse(node, k):
		nonlocal count, val
		if not node:
			return
		traverse(node.right, k)
		count += 1
		if count == k:
			val = node.val
		traverse(node.left, k)

	traverse(root, k)
	return val

a = Node(5)
b = Node(4)
c = Node(2)
d = Node(7)
e = Node(6)
f = Node(9)

a.left = b
b.left = c
a.right = d
d.left = e
d.right = f

print(kth_large_BST(a, 3))
print(kth_large_BST(a, 5))