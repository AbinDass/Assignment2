l=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
	elements=int(input())
	l.append(elements)
	large=max(l)
	minimum=min(l)
print("largest of the list is:",large)
print("minimum of the list is:",minimum)