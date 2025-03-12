from typing import Dict, List, Tuple

def minmax(data: List[int]) -> Dict[str, int]:
	temp_min = data[0]
	temp_max = data[0]

	for x in data:
		if x < temp_min:
			temp_min = x
		elif x > temp_max:
			temp_max = x

	return {
		"min": temp_min,
		"max": temp_max
	}


if __name__ == '__main__':
	print(minmax([4, 2, 1, 6, 7, 9]))


