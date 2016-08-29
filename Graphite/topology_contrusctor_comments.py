num=64

"""making array of 0s"""
arr = [list for x in range(num)]

for i in range(num):
	arr[i] = [0 for x in range(num)]

"""tracking the line"""
loop=1
"""'i' is the number it's jumping by. e.g. line 1-3-5-7-1 is jumping by 2, 1-5-1 is jumping by 4"""
for i in range(1,num):
	#
	"""lines is the number of lines for this 'i'. 
	if i is 2, there will be a line starting with 0 and a line starting with 1, so lines = 2
	if i is 3, there will be lines starting with 0,1,2. lines=3
	if i is greater than half of the size of the cluster (e.g. 5,6,7 if there are 8 nodes) then each line will only have one connection, so lines needs to be equal to the size of the cluster
	"""
	if i>num/2:
		lines = num
	else:
		lines = i

	for j in range(lines):
		"""'loop' only increases if something has been added to 'arr' (a connection was made)"""
		changed = False
		"""j: starting number, num+j: the overlap point, i:jump val"""
		for m in range(j,num+j,i):
			"""maps m values to values in the range of the cluster.
			in a cluster of 8, 8 will map to 0, 9 will map to 1, etc"""
			l = m%num

			"""if the node that will be connected to is past the overlap point OR this point in the array already has something (the nodes are already connected): do not make a connection."""
			"""e.g. 1-6-3. the overlap point is 1, and 3 is past that, so the 6-3 connection will not be made."""
			if not (m + i > num + j) and arr[l][(l+i)%num] == 0:
				"""otherwise, make a connection"""
				arr[l][(l+i)%num] = loop
				#print("from "+str(j)+" to "+str(num+j-1) + " by "+str(i) + ", at "+ str(l) + "," + str((l+i)%num))
				changed = True
		"""if a connection was made"""
		if changed:
			loop+=1
			changed = False
			#print(loop)

		"""make reverse connections"""
		"""NOTE: sometimes this makes the connections in an unexpected order, but it doesn't seem to be wrong in any way"""
		for m in range(num+j,j-1,-i):
			l = m%num
			if not (m + i > num + j) and arr[l][(l+num-i)%num] == 0:
				arr[l][(l+num-i)%num] = loop
				#print("from "+str(num+j-1)+" to "+str(j) + " by "+str(-i) + ", at "+ str(l) + "," + str((l+num-i)%num))
				changed = True

		if changed:
			loop+=1
			#print(loop)

"""printing"""
for i in arr:
	row = ""
	for j in i:
		row+=str(j)+" "
	print(row)