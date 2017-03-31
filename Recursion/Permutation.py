def permutation(arr):
	if len(arr) <= 1:
		return arr

	perms = []

	for i in range(len(arr)):
		ele = arr[i]

		rem = arr[:i] + arr[i+1:]

		for p in permutation(rem):
			perms.append(ele+p)

	return perms

print(permutation('123'))