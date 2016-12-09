from nose.tools import assert_equal

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
	right = sum(A)
	result = []
	for i in range(0, len(A)):
		if i > 0:
			left += A[i-1]
		right -= A[i]
		if left == right:
			result.append(i)
	return result

print(add_balance([-1, 3, -4, 5, 1, -6, 2, 1]))

class Add_Balance(object):
	def test(self, func):
		assert_equal(func([-1, 3, -4, 5, 1, -6, 2, 1]), [1, 3, 7])
		print("TEST PASSED")

t = Add_Balance()
t.test(add_balance)