
number= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
l=len(number)
i=0
num=number
Duplicates=[]
k=[]
while i<l:
    j=0
    # k=[]
    while j<l:
        if num[i] == num[j]:
           if num[i]not in Duplicates:
               Duplicates.append(num[i])
        j+=1
    i+=1
print(Duplicates)