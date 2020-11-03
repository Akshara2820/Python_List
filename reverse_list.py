place=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
l=len(place)
for i in range(int(l/2)):
    num=place[i]
    place[i]= place[l-i-1]
    place[l-i-1]=num
print(place)





place=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
length=(len(place))
index=0
while index<length:
	s=place[length-1]
	length-=1

	print(s)