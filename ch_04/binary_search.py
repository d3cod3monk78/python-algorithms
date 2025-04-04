def binary_search(data, target, low, high):

	if low > high:
		return False
	else:
		mid = (low + high) // 2

		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_search(data, target, low, mid - 1)
		elif target > data[mid]:
			return binary_search(data, target, mid + 1, high)

if __name__ == '__main__':
	# data = list([x for x in range(1, 11)])
	# print(binary_search(data, 7, 0, len(data) - 1))
	# print(binary_search(data, 15, 0, len(data) - 1))
	data = [1,2,3,4,5,6,7]
	print(binary_search(data, 3, 0, len(data) - 1))
	print(binary_search(data, 10, 0, len(data) - 1))
