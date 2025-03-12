def sum_of_squares(k: int)-> int:
	squares = [x*x for x in range(k)]

	addition = 0
	for x in squares:
		addition += x

	return addition


if __name__ == '__main__':
	print(sum_of_squares(5))
	print(sum_of_squares(3))
	print(sum_of_squares(10))
