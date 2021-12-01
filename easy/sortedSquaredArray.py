# On time O1 space
def sortedSquaredArray(array):
	a = []
	for i in range(len(array)):
		a.append(array[i] * array[i])
	
	a.sort()
    return a

	
'''
O(nlogn) time | O(n) space
def sortedSquaredArray(array):
	sortedSquares = [0 for _ in array]
	for idx in range(len(array)):
		value = array[idx]
		sortedSquares[idx] = value * value
	
	sortedSquares.sort()
    return sortedSquares
'''