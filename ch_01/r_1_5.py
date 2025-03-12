def sum_of_squares(k: int)->int:
	return sum([x*x for x in range(k)])

if __name__ == '__main__':
	print(sum_of_squares(3))
	print(sum_of_squares(10))
	print(sum_of_squares(20))