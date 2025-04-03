class CountToFive:
	def __init__(self):
		self.num = 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.num <= 5:
			current = self.num
			self.num += 1
			return current

		else:
			raise StopIteration


for i in CountToFive():
	print(i)
