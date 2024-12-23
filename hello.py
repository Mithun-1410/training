total=0
while True:
	n=input("Enter numbers : ")
	if not n.isdigit():
		break
	total+=int(n)
		
print(total)

