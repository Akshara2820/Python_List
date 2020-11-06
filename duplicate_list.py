
number= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
l=len(number)
i=0
num=number
Duplicates=[]
while i<l:
    j=0
    while j<l:
        if num[i] == num[j]:
           if num[i]not in Duplicates:
               Duplicates.append(num[i])
        j+=1
    i+=1
print(Duplicates)





number= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
l=len(number)
Duplicates = [] 
i=0
while i<l: 
    j = i+1
    while j<l:
        if number[i] == number[j]:
        	if number[i] not in Duplicates: 
        		Duplicates.append(number[i])
        j+=1

    i+=1
print(Duplicates)