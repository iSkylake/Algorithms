def staircase(n):
	for i in range(1, n+1):
		stair = " "*(n-i)
		stair += "#"*i
		print(stair)

def easyStaircase(n):
	for i in range(n):
		print('#'*(i+1))

staircase(6)
staircase(3)
staircase(10)

easyStaircase(6)
easyStaircase(10)
