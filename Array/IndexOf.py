from nose.tools import assert_equal

def indexOf(target, string):
	target = target.lower()
	string = string.lower()

	for i in range(len(string)):

		if(string[i] == target[0]):
			index = i
			subIndex = 0

			while string[index] == target[subIndex]:
				index += 1
				subIndex += 1
				if subIndex == len(target):
					return i

	return "-1"

string = "Pirate Warrior so OP, just go face SMORC."

class indexOf_test:
	def test(self, func):
		assert_equal(func("Pirate", string), 0)
		assert_equal(func(",", string), 20)
		assert_equal(func(" War", string), 6)
		assert_equal(func(".", string), 40)
		assert_equal(func(" Edwin", string), "-1")
		print("TESTS PASSED")

t = indexOf_test()
t.test(indexOf)