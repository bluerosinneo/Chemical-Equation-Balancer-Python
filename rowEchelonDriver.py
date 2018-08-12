from rowEchelon import rowEchelon

A = [[1,0,-3,0],
	[1,0,0,-2],
	[4,10,-4,-7],
	[0,4,-1,0]]

print ("--Before Row Echelon--")
print(rowEchelon.showMatrix(A))
rowEchelon.solveRowEchelon(A)
print ("--After Row Echelon--")
print(rowEchelon.showMatrix(A))

a = rowEchelon.gCD(350,275)

a = (350*275)/a

a = (a*65)/rowEchelon.gCD(a,65)

print (a)
