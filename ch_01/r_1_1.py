def is_multiple(m: int, n: int) -> bool:
	"""
		if n = mi:
			then return True
			else return False
	"""
	if(n % m == 0):
		return True
	else:
		return False

if __name__ == '__main__':
	print(is_multiple(5, 10))
	print(is_multiple(3, 10))