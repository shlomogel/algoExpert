def twoNumberSum(array, targetSum):
    ans = []
	for i, number in enumerate(array):
		if targetSum-number in array[i+1:]:
			return [number, targetSum-number]
    return ans
	
# AlgoExpert Solutions:
'''
O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    ans = []
	for i, number in enumerate(array):
		if targetSum-number in array[i+1:]:
			return [number, targetSum-number]
    return ans

O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    ans = []
	for i, number in enumerate(array):
		if targetSum-number in array[i+1:]:
			return [number, targetSum-number]
    return ans

O(nlog(n) time | O(1) space
def twoNumberSum(array, targetSum):
    ans = []
	for i, number in enumerate(array):
		if targetSum-number in array[i+1:]:
			return [number, targetSum-number]
    return ans
'''