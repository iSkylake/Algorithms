from nose.tools import assert_equal

def power_set(string):
	setList = []

	# Helper traverse method
	def traverse(sets, level):
		nonlocal setList

		# Onces it gets to the input's length level, it will append the resulting set
		if level == len(string):
			setList.append(sets)
			return

		# Goes to the left side
		traverse(sets, level+1)

		# Goes to the right side
		traverse(sets+string[level], level+1)

	traverse("", 0)
	return setList

class Power_Set_Test:
	def test(self, func):
		assert_equal(func('ab'), ['', 'b', 'a', 'ab'])
		assert_equal(func('abc'), ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc'])
		print('TESTS PASSED')

t = Power_Set_Test()
t.test(power_set)