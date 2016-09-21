class Node:
	def __init__(self, value=0):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def append(self, value):
		new_node = Node(value)
		if self.length == 0:
			self.head = new_node
		else:
			self.tail.next = new_node
		self.tail = new_node
		self.length += 1

	def search(self, value):
		current = self.head
		found = False
		while not found and current != None:
			if current.value == value:
				found = True
			else:
				current = current.next
		return current

	def insert(self, value, searchVal):
		new_node = Node(value)
		currentNode = self.search(searchVal)
		if currentNode == None:
			return "Value not found"
		else:
			new_node.next = currentNode.next
			currentNode.next = new_node
			self.length += 1

			if new_node.next == None:
				self.tail = new_node

	def contain(self, value):
		currentNode = self.search(value)
		if currentNode == None:
			return False
		else:
			return True

	def delete(self, value):
		current = self.head
		previous = None
		found = False
		while not found and current != None:
			if current.value == value:
				found = True
			else:
				previous = current
				current = current.next

		if previous == None:
			self.head = current.next
			current.next = None
		elif current.next == None:
			self.tail = previous
			previous.next = None
		else:
			previous.next = current.next
			current.next = None
		

		self.length -= 1
