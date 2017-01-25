def prime(num):
	primes = [2, 3, 5, 7]
	count = 0
	if num in primes:
		return True
	for n in primes:
		if num%n == 0:
			count += 1
	if count == 0:
		return True
	else:
		return False

print(prime(2))
print(prime(7))
print(prime(11))
print(prime(41))
print(prime(4))
print(prime(50))