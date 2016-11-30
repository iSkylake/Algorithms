# Function that reverse a Singly Linked List

class Node:
	def __init__(self, val=0):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def append(self, val):
		new_node = Node(val)
		if self.length == 0:
			self.head = new_node
		else:
			self.tail.next = new_node
		self.tail = new_node
		self.length += 1

# First Attempt
def reverse_list(node):
	previous = None
	current = node
	next_node = node.next
	while current != None:
		current.next = previous
		previous = current
		current = next_node
		if current != None:
			next_node = current.next

# Cleaner
def reverse_list(node):
	previous = None
	current = node
	next_node = node.next
	while current != None:
		next_node = current.next
		current.next = previous
		previous = current
		current = next_node