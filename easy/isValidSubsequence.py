# On time O1 space
def isValidSubsequence(array, sequence):
	seq=0
	i = 0
	while i < len(array) and seq < len(sequence):
		if array[i] == sequence[seq]:
			seq += 1
		i +=1

    return seq == len(sequence)
	
'''
O(n) time | O(1) space
def isValidSubsequence(array, sequence):
	seqIdx=0
	for value in array:
		if seqIdx == len(sequence):
			break;
		if sequence[seqIdx] == value:
		seqIdx +=1

    return seqIdx == len(sequence)
'''