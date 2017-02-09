from nose.tools import assert_equal

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

def valid_circular_LL(node):
	slow = node
	fast = node
	while fast.next.next != None and fast.next != None:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			return True
	return False

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

x = Node(1)
y = Node(2)
z = Node(3)

x.next = y
y.next = z


class Valid_Circular:
	def test(self, func):
		assert_equal(func(a), True)
		assert_equal(func(x), False)
	print("TESTS PASSED")

t = Valid_Circular()
t.test(valid_circular_LL)