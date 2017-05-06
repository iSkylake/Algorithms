from sets import Set

def long_cons_sum(arr):
	n = len(arr)
	hash_list = Set()
	long_sum = 0

	for num in arr:
		hash_list.add(num)

	for i in range(n):
		if arr[i]-1 not in hash_list:
			j = arr[i]
			while(j in hash_list):
				j+=1
			long_sum = max(long_sum, j-arr[i])

	return long_sum

print(long_cons_sum([1, 9, 3, 10, 4, 20, 2]))