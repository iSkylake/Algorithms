def most_vowel_array(array):
	vowels = ['a', 'e', 'i', 'o', 'u']
	max_vowel = [0, 0]
	for string in range(len(array)):
		vowel_count = 0
		for letter in array[string]:
			if letter in vowels:
				vowel_count += 1
		if vowel_count > max_vowel[1]:
			max_vowel[0] = string
			max_vowel[1] = vowel_count

	return str(max_vowel[0])

def most_vowel_string(array):
	vowels = 'aeiou'
	max_vowel = [0, 0]
	for string in range(len(array)):
		vowel_count = 0
		for letter in array[string]:
			if letter in vowels:
				vowel_count += 1
		if vowel_count > max_vowel[1]:
			max_vowel[0] = string
			max_vowel[1] = vowel_count

	return str(max_vowel[0])

print("The word with more vowels is in the position " + most_vowel_array(['hello', 'hello world', 'python']))
print("The word with more vowels is in the position " + most_vowel_string(['hello', 'hello world', 'aeiou']))