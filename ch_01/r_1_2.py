def is_even(k: int) -> int:
	"""
		if k is even then return True
		But in here we can use * or / or %
	"""
	while k > 2:
		k = k - 2

	if k == 2 :
		return True
	else:
		return False

if __name__ == '__main__':
	print(is_even(10))
	print(is_even(7))
	print(is_even(28))
	print(is_even(43))