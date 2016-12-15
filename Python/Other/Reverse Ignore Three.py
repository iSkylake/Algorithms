from nose.tools import assert_equal

def reverse_ignore_three(input):
	index = len(input) - 1
	output = ''
	while index >= 0:
		if input[index-2:index+1] == input[index]*3:
			index -= 3
		else:
			output += input[index]
			index -= 1
	return output

	print(output)

reverse_ignore_three('abcccaabbbcabc')

class Reverse_Ignore_Three(object):
	def test(self, func):
		assert_equal(func('abcccaabbbcabc'), 'cbacaaba')
		print("TEST PASSED")

t = Reverse_Ignore_Three()
t.test(reverse_ignore_three)