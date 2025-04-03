my_list = list([x for x in range(10)])

iteration = iter(my_list)

# print(next(iteration))
# print(next(iteration))
# print(next(iteration))

while True:
	try:
		i = next(iteration)
		print(i)

	except StopIteration:
		break