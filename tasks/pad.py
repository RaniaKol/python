import sys
import numpy as np


def pad(input_list):
	"""
input_list = [[1,2,3], [1,2,3,4,5], [1,2], [1,2,3,4,5,6,7,8]]
return a matrix where
1) matrix[i][:len(input_list[i])] == input_list[i]
and
2) matrix[i][len(input_list[i]):] == [0,0, ..., 0]
... 
"""

	input_list = [[1,2,3], [1,2,3,4,5], [1,2], [1,2,3,4,5,6,7,8]]
	y=np.matrix(input_list)
	length = 2*max(map(len, input_list))
	matrix = np.matrix([x+[0]*(length-len(x)) for x in input_list], dtype="int")

	#matrix1= np.split(matrix,4)
	#for i in range(len(input_list)):
	#	if np.any(matrix1[i][:len(input_list[i])]) == np.any(input_list[i]):
	#		print(True)
	return matrix
	
					



    #pass





if __name__ == '__main__':
	pad(sys.argv[1:])