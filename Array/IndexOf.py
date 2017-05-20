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

string = "Pirate Warrior so OP, just go face SMORC"

print(indexOf("RC", string))