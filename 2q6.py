l=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
	elements=int(input())
	l.append(elements)
print(l)
from functools import reduce
def add(x,y):
	return x+y
print(reduce(add,l))