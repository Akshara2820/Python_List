char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
l = []
i=0
while i<len(char_list):
    count=0
    k=[]
    j=0
    while j<len(char_list):
        if char_list[i] in char_list[j]:
            if char_list[i] not in k :
                k+=char_list[i]
            count+=1
        j+=1
    i+=1
    k.append(count)
    if k not in l:
        l.append(k)

print(l)




#   for loop 

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
l = []

for i in char_list:
	count = 0
	k=[]
	for j in char_list:
		if i in j:
			if i not in k:
				k+=i
			count+=1
	k.append(count)

	if k not in l:
		l.append(k)

print(l)
