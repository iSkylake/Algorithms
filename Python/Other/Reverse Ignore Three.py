def reverse_ignore_three(input):
	index = len(input) - 1
	output = ''
	while index >= 0:
		if input[index-2:index+1] == input[index]*3:
			index -= 3
		else:
			output += input[index]
			index -= 1

	print(output)

reverse_ignore_three('abcccaabbbcabc')