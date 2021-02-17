string=input("enter the string:")

td=0
tl=0
for i in string:
	if i.isnumeric():
		td=td+1
	else:
		tl=1
		tl=tl+1
print(" the digits found:",td)
print(" the letters found:",tl)

