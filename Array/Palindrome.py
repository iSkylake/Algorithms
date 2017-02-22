def palindrome(s):
	size = len(s)
	mid = size//2
	if size%2 == 0:
		left = mid - 1
		right = mid
	else:
		left = mid - 1
		right = mid + 1

	while left >= 0 and right < size:
		if s[left] != s[right]:
			return False
		left -= 1
		right += 1

	return True

print(palindrome("palindrome"))
print(palindrome("abccba"))
print(palindrome("abcba"))