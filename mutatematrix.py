def reflect_matrix_along_prim_diag(arr, row, col):
	#Reflect matrix along primary diagonal
	#@author - Abhik Dey

	resprim = [[0 for x in range(col)] for y in range(row)]
	print ("1111111111111111111111111111111111111111111111111")
	print (resprim)


	for i in range(row):
		for j in range(col):
			resprim[i][j] = arr[j][i]

	print ("Final matrix : ")
	print (resprim)

	return resprim

def reflect_matrix_along_sec_diag(arr, row, col):
	#Reflect matrix along secondary diagonal
	#@author - Abhik Dey
	ressec = [[0 for x in range(col)] for y in range(row)]
	print ("2222222222222222222222222222222222222222222222222")
	for i in range(row):
		for j in range(col):
			ressec [i][j] = arr[(col-1)-j][(col-1)-i]

	print ("Final matrix : ")
	print (ressec)

	return ressec

def rotatematrixclockwise(arr, row, col):
	#Reflect matrix clockwise
	#@author - Abhik Dey
	retarr = [[0 for x in range(col)] for y in range(row)]
	print ("0000000000000000000000000000000000000000000000000")
	for i in range(row):
		for j in range(col):

			retarr[i][j] = arr[(col - 1)-j][i]

	return retarr


def main ():
	arr = [[1,2,3],
		   [4,5,6],
		   [7,8,9]]

	print ("Before matrix rotate:")
	print (arr)

	q = [2,1,0]

	row = len(arr)
	col = len(arr[0])

	for qiter in q:
		if qiter == 0:
			arr = rotatematrixclockwise(arr,row,col)
		elif qiter == 1:
			arr = reflect_matrix_along_prim_diag(arr,row,col)
		elif qiter == 2:
			arr = reflect_matrix_along_sec_diag(arr,row,col)

	print (arr)
if __name__ == '__main__':
	main()