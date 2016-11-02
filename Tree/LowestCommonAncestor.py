class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def lowest_common_ancestor(root, node1, node2):

	node_list_1, node_list_2 = [], []

	def traverse(node, node1):
		nonlocal node_list_1
		if node == None:
			return
		else:
			node_list_1.append(node.value)
			if node.value == node1:
				return
			traverse(node.left, node1)
			traverse(node.right, node1)
			node_list_1.pop()

	traverse(root, node1)

	print(node_list_1)