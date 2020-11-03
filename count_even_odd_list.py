elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
l=len(elements)
i=0
even=[]
odd=[]
x=elements[i]
while i<l:
    if elements[i]%2==0:
        even.append(elements[i])
    else:
        odd.append(elements[i])
    i+=1
print(even)
print(odd)
