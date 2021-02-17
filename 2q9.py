l=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
	elements=int(input())
	l.append(elements)
print(l)

a=filter(lambda s:s<5,l)
print(list(a))

b=map(lambda s:s>3,l)
print(list(b))


from functools import reduce
def add(x,y):
	return x+y
print(reduce(add,l))