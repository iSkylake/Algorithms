def powerSet(string):
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

print(powerSet("abc"))