from nose.tools import assert_equal

def reverseString(s):
	if len(s) < 1:
		return s
	return reverseString(s[1:]) + s[0]

class ReverseStringTest:
	def test(self, func):
		assert_equal(func("String"), "gnirtS")
		assert_equal(func("123456"), "654321")
		assert_equal(func("madam"), "madam")
		print("TESTS PASSED")

t = ReverseStringTest()
t.test(reverseString)
