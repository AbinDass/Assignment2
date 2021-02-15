x=[["a","b"],["c","d"],["e","f"]]
y=[[0,0,0],[0,0,0]]
for i in range (len(x)):
	for j in range (len(x[0])):
		y[j][i]=x[i][j]
for r in y:
	print(r)