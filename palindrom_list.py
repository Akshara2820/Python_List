
Name=input("enter the name ")
l=len(Name)
s=""

while l>0:
	s+=Name[l-1]
	l-=1
if s==Name:
	print(" Name Plindrome "+Name)
else:
	print("Name not Plindrome  "+Name)