# def add_balance(A):
# 	left = 0
# 	result = []
# 	for i in range(1, len(A)):
# 		left += A[i-1]
# 		total = 0
# 		for j in range(i+1, len(A)):
# 			total += A[j]
# 		if total == left:
# 			result.append(i)
# 	print(result)

# add_balance([-1, 3, -4, 5, 1, -6, 2, 1])



def add_balance(A):
	left = 0
	right = sum(A[1:])
	result = []
	for i in range(1, len(A)):
		left += A[i-1]
		right -= A[i]
		if left == right:
			result.append(i)
	print(result)

add_balance([-1, 3, -4, 5, 1, -6, 2, 1])