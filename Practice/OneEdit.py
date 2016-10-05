def one_edit(str1, str2):
	str_1_len = len(str1)
	str_2_len = len(str2)

	# Verify if there's more than 1 extra character
	if str_1_len - str_2_len > 1 or str_1_len - str_2_len < -1:
		return False

	edit = 0
	# Looking for 1 character extra
	if str_1_len > str_2_len or str_2_len > str_1_len:
		edit += 1

	i, j = 0, 0

	while i < str_1_len and j < str_2_len:
		print(edit)
		print("%s %s"%(str1[i], str2[j]))
		if str1[i] != str2[j]:
			edit += 1
			if str_1_len < str_2_len:
					j += 1
			elif str_2_len < str_1_len:
					i += 1
			else:
					i += 1
					j += 1
		else:
				i += 1
				j += 1
		if edit > 1:
			print(edit)
			return False

	if edit == 1:
		return True
	else:
		return False


print(one_edit('table', 'tablet'))
print(one_edit('table', 'tale'))
print(one_edit('table', 'cables'))
