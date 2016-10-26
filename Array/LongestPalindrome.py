# def longestPalindrome(n, s):
	# max_lenght = 0

	# for i in range(n):
	# 	left = i
	# 	right = i + 1
	# 	count = 0
	# 	while left >= 0 and right < n:
	# 		print('ENTER')
	# 		if s[left] == s[right]:
	# 			left += 1
	# 			right += 1
	# 			count += 2
	# 			max_lenght = max(count, max_lenght)
	# 			print(max_lenght)
	# 		else:
	# 			left = -1

def longestPalindrome(string):
	max_odd = 0
	s = string.lower()
	n = len(s)
	for i in range(n):
		left = i-1
		right = i+1
		count = 1
		while left >= 0 and right < n:
			if s[left] == s[right]:
				left -= 1
				right += 1
				count += 2
				max_odd = max(count, max_odd)
			else:
				left = -1

	max_even = 0
	for i in range(n):
		left = i
		right = i + 1
		count = 0
		while left >= 0 and right < n:
			if s[left] == s[right]:
				left -= 1
				right += 1
				count += 2
				max_even = max(count, max_even)
			else:
				left = -1	

	return max(max_odd, max_even)

print(longestPalindrome("monkeybananacarsaibohphobialoool"))
print(longestPalindrome("bananaAButTuba"))