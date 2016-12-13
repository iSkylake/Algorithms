from nose.tools import assert_equal

def occurrence_in_string(string, sub_string):
	occurrence = 0
	# when to stop
	end = len(string) - len(sub_string) + 1
	# Ignore case
	low_str = string.lower()

	for i in range(end):
		# This is more of a Python feature, for an overall solution I can loop, concat and store it in a temp variable
		if low_str[i:i+len(sub_string)] == sub_string:
			occurrence += 1

	return occurrence

print(take_home("tewrwaBcfasaBCabcgadfasdAbcsfaSFD", "abc")) # output: 4
print(take_home("abCrwaBcfasaBCabcgadfasdAbcsfaABc", "abc")) # output: 6
print(take_home("zzzzzz", "zz")) # output: 5

class Occurrence_in_String(object):
	def test(self, func):
		assert_equal(func("tewrwaBcfasaBCabcgadfasdAbcsfaSFD"), "abc")
		assert_equal(func("abCrwaBcfasaBCabcgadfasdAbcsfaABc"), "abc")
		assert_equal(func("zzzzzz"), "zz")
		print("TEST PASSED")

t = Occurrence_in_String()
t.test(occurrence_in_string)

# I know there's a count function in Python and it can solve this example string.lower().count(sub_string) but in other cases like "zzzzzz", "zzz" it will return 2 instead of 4

# For the overall solution mentioned before it will be like:

# for i in range(end):
# 	temp = ""
# 	for j in range(i, i+len(sub_string)):
# 		temp += low_str[j]
# 	if temp == sub_string:
# 		occurrence += 1
