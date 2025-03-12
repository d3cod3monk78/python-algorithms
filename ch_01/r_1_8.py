def find_negative_to_positive(k: int, n: int)->int:
	"""
		k is the negative index
		n is the length of the string
		[0][1][2][3]........[n-2][n-1]
		[-n][-(n-1)][-(n-2)][-(n-3)]........[-2][-1]
		positive_index = n + k
		ex -> 1 = n + -(n-1) = n - n + 1 = 1
	"""
	return n + k

if __name__ == '__main__':
	print(find_negative_to_positive(-2, 10))