def linear_recurion(data, n):
	if n == 0:
		return 0
	else:
		return linear_recurion(data, n-1) + data[n-1]

if __name__ == '__main__':
	data = list([x for x in range(1, 11)])
	print(linear_recurion(data, 10))