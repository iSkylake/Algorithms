class Dynamic_Array:
	def __init__(self):
		self.array = [None for i in range(2)]
		self.capacity = 2
		self.fill = 0

	def incrementSize(self):
		tempArray = self.array
		self.capacity *= 2
		self.array = [None for i in range(self.capacity)]
		for i in range(self.fill):
			self.array[i] = tempArray[i]

	def push(self, value):
		if self.fill >= len(self.array):
			self.incrementSize()
		self.array[self.fill] = value
		self.fill += 1

dynArray = Dynamic_Array()

dynArray.push(1)
print(dynArray.array)

dynArray.push(2)
print(dynArray.array)

dynArray.push(3)
dynArray.push(4)
print(dynArray.array)

dynArray.push(5)
print(dynArray.array)