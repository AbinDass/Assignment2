l=[1,2,3,4,5,6,7]
print(["element{0}".format(i) for i in l])


pass


l=[1,2,3,4,5,6,7]
str="element"
str+="{0}"
l=[str.format(i) for i in l]
print(l)