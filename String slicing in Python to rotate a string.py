def rotate(input,d):

	
	Lfirst = input[0 : d]
	Lsecond = input[d :]
	Rfirst = input[0 : len(input)-d]
	Rsecond = input[len(input)-d : ]

	
	print ("Left Rotation : ", (Lsecond + Lfirst) )
	print ("Right Rotation : ", (Rsecond + Rfirst))


if __name__ == "__main__":
	input = 'GeeksforGeeks'
	d=2
	rotate(input,d)
