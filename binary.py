def binary_search(num, alist):
	low = 0
	high = len(alist) + 1
	while low <= high:
		mid = (low + high) // 2
		guess = alist[mid]
		if guess == num:
			return num
		elif guess > num:
			high = mid - 1
		else:
			low = mid + 1
	return None
