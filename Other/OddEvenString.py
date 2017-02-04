def oddEvenString(string):
	odd = ""
	even = ""
	for i in range(len(string)):
		if i%2 == 0:
			even += string[i]
		else:
			odd += string[i]
	print(even + " " + odd)

oddEvenString("Hello")
oddEvenString("Darkness")
oddEvenString("My")
oddEvenString("Old")
oddEvenString("Friend")
