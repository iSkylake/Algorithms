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
	# 		self.size += 1
	# 	else:
	# 		add = False
	# 		node = self.root
	# 		while not add:
	# 			if val < node.val and not node.left:
	# 				node.left = new_node
	# 				self.size += 1
	# 				add = True
	# 			elif val > node.val and not node.right:
	# 				node.right = new_node
	# 				self.size += 1
	# 				add = True
	# 			elif val < node.val:
	# 				node = node.left
	# 			else:
	# 				node = node.right

	def insert(self, val):
		new_node = Node(val)
		if not self.root:
			self.root = new_node
		else:
			self._insert(self.root, new_node)

	def _insert(self, node, new_node):
		if new_node.val < node.val:
			if not node.left:
				node.left = new_node
			else:
				self._insert(node.left, new_node)
		else:
			if not node.right:
				node.right = new_node
			else:
				self._insert(node.right, new_node)

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

#Using Array
# def kth_large_BST(root, k):
#
# 	inorder = []
#
# 	def traverse(node):
# 		nonlocal inorder
#
# 		if not node:
# 			return
# 		traverse(node.right)
# 		inorder.append(node.val)
# 		traverse(node.left)
#
# 	traverse(root)
# 	return inorder[k-1]

# a = Node(5)
# b = Node(4)
# c = Node(2)
# d = Node(7)
# e = Node(6)
# f = Node(9)

# a.left = b
# b.left = c
# a.right = d
# d.left = e
# d.right = f

bst = BST()
bst.insert(5)
bst.insert(4)
bst.insert(2)
bst.insert(7)
bst.insert(6)
bst.insert(9)

print(kth_large_BST(bst.root, 3))
print(kth_large_BST(bst.root, 5))