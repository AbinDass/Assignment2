b={"a":1,"b":2,"c":3,"d":4,"e":5}
#print(a)
def sum(a):
	s=0
	for i in a:
		s=s+a[i]
	return s
print("sum of dictonary values is:",sum(b))

