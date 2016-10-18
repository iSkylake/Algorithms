# Create a function that return True if the Binary Tree is a BST or False if it isn't a BST

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def valid_BST(root):
	inorder = []
	def traverse(node):
		nonlocal inorder
		if not node:
			return
		traverse(node.left)
		inorder.append(node.val)
		traverse(node.right)

	traverse(root)
	if sorted(inorder) == inorder:
		return True
	else:
		return False

a = Node(5)
b = Node(2)
c = Node(7)
d = Node(4)
e = Node(9)

a.left = b
a.right = c
c.left = d
c.righ = e

print(valid_BST(a))

a = Node(5)
b = Node(2)
c = Node(7)
d = Node(4)
e = Node(9)

a.left = b
b.right = d
a.right = c
c.righ = e

print(valid_BST(a))