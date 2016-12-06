def solution(A):
	left = 0
	result = []
	for i in range(1, len(A)):
		left += A[i-1]
		total = 0
		for j in range(i+1, len(A)):
			total += A[j]
		print("%s %s" %(total, left))
		if total == left:
			result.append(i)
	print(result)

solution([-1, 3, -4, 5, 1, -6, 2, 1])