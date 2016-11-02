def most_vowel(array):
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

	return max_vowel[0]