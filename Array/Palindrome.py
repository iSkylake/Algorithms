from nose.tools import assert_equal

def palindrome(s):
	s = s.lower()
	size = len(s)
	mid = size//2
	left = mid - 1
	if size%2 == 0:
		right = mid
	else:
		right = mid + 1

	while left >= 0 and right < size:
		if s[left] != s[right]:
			return False
		left -= 1
		right += 1

	return True

class Palindrome_Test(object):
	def test(self, func):
		assert_equal(func("Palindrome"), False)
		assert_equal(func("AbcCba"), True)
		assert_equal(func("abcba"), True)
		print("TEST PASSED")

t = Palindrome_Test()
t.test(palindrome)