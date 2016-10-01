# O(n) space complexity solution
def remove_duplicate(arr):
	result = []
	for num in arr:
		if num not in result:
			result.append(num)
	return len(result)

# O(1) space complexity solution
def remove_duplicate(arr):
	lenght = 1
	for i in range(len(arr)-1):
		if arr[i] != arr[i+1]:
			lenght += 1
	return lenght