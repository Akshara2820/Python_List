

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
l=len(elements)
i=0
count_even=0
count_odd=0
x=elements[i]
while i<l:
    if elements[i]%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
    i+=1
print(count_even)
print(count_odd)












