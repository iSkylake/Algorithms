class Node:
	def __init__(self, val=0):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def insert(self, val):
		new_node = Node(val)
		if self.length == 0:
			self.head = new_node
		self.tail = new_node
		self.length += 1

def reverse_list(node):
	previous = None
	current = node
	next_node = node.next
	