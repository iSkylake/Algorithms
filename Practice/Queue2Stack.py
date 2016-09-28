class Queue2Stack:
	def __init__(self):
		self.in_stack = []
		self.out_stack = []
		self.lenght = 0

	def push(self, value):
		self.in_stack.append(value)
		self.lenght += 1

	def pop(self):
		if not self.out_stack:
			for i in range(len(self.in_stack)):
				self.out_stack.append(self.in_stack.pop())
			self.lenght -= 1
			return self.out_stack.pop()
		else:
			self.lenght -= 1
			return self.out_stack.pop()