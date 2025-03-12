def sum_of_odd_squares(k: int)->int:
	return sum([x*x for x in range(k) if x%2 == 1])

if __name__ == '__main__':
	print(sum_of_odd_squares(4))
	print(sum_of_odd_squares(10))