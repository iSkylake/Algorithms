from nose.tools import assert_equal

class Palindrome:
	def __init__(self):
		self.stack = []
		self.queue = []

	def enqueue(self, s):
		for char in s:
			self.queue.append(char)

	def pushStack(self, s):
		for char in s:
			self.stack.append(char)

	def dequeue(self):
		return self.queue.pop(0)

	def popStack(self):
		return self.stack.pop()

	def check(self, s):
		s = s.lower()
		self.enqueue(s)
		self.pushStack(s)
		for i in range(len(s)):
			if self.dequeue() != self.popStack():
				self.stack = []
				self.queue = []
				return False
		return True

pal = Palindrome()

class Palindrome_Test(object):
	def test(self, func):
		assert_equal(func("Palindrome"), False)
		assert_equal(func("aBccba"), True)
		assert_equal(func("abcba"), True)
		print("TEST PASSED")

t = Palindrome_Test()
t.test(pal.check)