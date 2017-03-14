from nose.tools import assert_equal

def checkPerm(l1, l2):

	if len(l1) != len(l2):
		return False

	dic = {}

	for val in l1:
		if val in dic:
			dic[val] += 1
		else:
			dic[val] = 1

	for val in l2:
		if val in dic:
			dic[val] -= 1
			if dic[val] < 0:
				return False
		else:
			return False

	if sum(dic.values()) == 0:
		return True
	else:
		return False

class checkPermTest:
	def test(self, func):
		assert_equal(func('abc', 'bca'), True)
		assert_equal(func('abc', 'ca'), False)
		assert_equal(func('abc', 'cca'), False)
		print('TESTS PASSED')

t = checkPermTest()
t.test(checkPerm)