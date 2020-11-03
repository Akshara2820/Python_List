num=[50,40,23,70,56,5,18,7]
l=len(num)
i=0
max1=num[i]
while i<l:
    if num[i]>max1:
        max1=num[i]
    i+=1
print(max1)
v=0
max2=num[v]
j=0
while j<l:
    if max2<num[j]<max1:
    	max2 = num[j]
    j+=1
print(max2)


