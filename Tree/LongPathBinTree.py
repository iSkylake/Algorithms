class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


class Binary_Tree:
	def __init__(self):
		self.root = None
		self.size = 0

# First attempt
# def long_path(root):
#     count = 0
#     max_path = 0

#     def _long_path(node, count):
#         nonlocal max_path
#         if node == None:
#             if count >= max_path:
#                 max_path = count
#             return
#         count += 1
#         _long_path(node.left, count)
#         _long_path(node.right, count)
#         count -= 1

#     _long_path(root, count)
#     print(max_path)


# Cleaner version
def long_path(root):
	max_path = 0
	def traverse(node, length):
		if not node:
			return
		nonlocal max_path
		max_path = max(max_path, length)
		traverse(node.left, length+1)
		traverse(node.right, length+1)
	traverse(root, 1)
	print(max_path)

bin_tree = Binary_Tree()
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
j = Node('j')
k = Node('k')

bin_tree.root = a
a.left = b
a.right = c
b.left = d
b.right = e
e.right = f
f.left = h
c.right = g
d.left = i
i.left = j
j.right = k

long_path(a)
