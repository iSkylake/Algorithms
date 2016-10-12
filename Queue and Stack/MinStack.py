class MinStack:
	def __init__(self):
		self.stack = []
		self.min = []
		self.length = 0

	def push(self, val):
		self.stack = self.stack + [val]
		if self.length < 1:
			self.min = self.min + [val]
		elif val < self.min[self.length-1]:
			self.min = self.min + [val]
		else:
			self.min = self.min + [self.min[self.length-1]]
		self.length += 1

	def pop(self):
		self.min.pop()
		pop_ele = self.stack.pop()
		self.length -= 1
		return pop_ele

	def peek(self):
		peek_ele = self.stack[self.length-1]
		return peek_ele

	def minVal(self):
		min_ele = self.min[self.length-1]
		return min_ele
