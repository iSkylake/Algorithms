class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Binary_Tree:
	def __init__(self):
		self.root = None
		self.size = 0

def invert_BT(node):
	if not node:
		return
	node.left, node.right = node.right, node.left
	invert_BT(node.left)
	invert_BT(node.right)

bt = Binary_Tree()
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.left = b
a.right = c
c.left = d
c.right = e

print(a.val)
print(a.left.val)
print(a.right.val)
print(a.right.left.val)
print(a.right.right.val)

invert_BT(a)

print(a.val)
print(a.left.val)
print(a.right.val)
print(a.left.left.val)
print(a.left.right.val)