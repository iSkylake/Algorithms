class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

def valid_circular_LL(node):
	slow = node
	fast = node
	while fast.value != None and fast.next != None:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			return True
	return False

