# def longestPalindrome(n, s):
	max_lenght = 0

	for i in range(n):
		left = i
		right = i + 1
		count = 0
		while left >= 0 and right < n:
			print('ENTER')
			if s[left] == s[right]:
				left += 1
				right += 1
				count += 2
				max_lenght = max(count, max_lenght)
				print(max_lenght)
			else:
				left = -1

def longestPalindrome(n, s):
	max_lenght = 0

	for i in range(n):
		left = i-1
		right = i+1
		count = 1
		print('NEW')
		while left >= 0 and right < n:
			if s[left] == s[right]:
				left -= 1
				right += 1
				count += 2
				max_lenght = max(count, max_lenght)
				print(max_lenght)
			else:
				left = -1
	return max_lenght

print(longestPalindrome(6, "banana"))
