def one_edit(str1, str2):
	if len(str1) - len(str2) > 1 or len(str2) - len(str1) > 1:
		return False

	i, j, edit = 0, 0, 0

	while i < len(str1)-1 or j < len(str2)-1:
		if str1[i] != str2[j]:
			edit += 1
			if str1[i+1] == str2[j] or str2[j+1] == str1[i]:
				if len(str1) > len(str2):
					if i < len(str1)-1:
						i += 1
				else:
					if j < len(str2)-1:
						j += 1
			else:
				if i < len(str1)-1:
					i += 1
				if j < len(str2)-1:
					j += 1
		else:
			if i < len(str1)-1:
				i += 1
			if j < len(str2)-1:
				j += 1

	if str1[i] != str2[j]:
		edit += 1

	if edit > 1:
		return False
	else:
		return True



print(one_edit('table', 'tablet'))
print(one_edit('table', 'tale'))
print(one_edit('table', 'cables'))
