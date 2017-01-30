def staircase(n):
	for i in range(1, n+1):
		stair = " "*(n-i)
		stair += "#"*i
		print(stair)

staircase(6)
staircase(3)
staircase(10)