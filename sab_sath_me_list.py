elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
l=len(elements)
i=0
count_even=0
count_odd=0
sum_even=0
sum_odd=0
average_even=0
average_odd=0
while i<l:
    if elements[i]%2==0:
        count_even+=1
        sum_even=sum_even+elements[i]
        average_even+=1
    else:
        count_odd+=1
        sum_odd=sum_odd+elements[i]
        average_odd+=1
    i+=1
print("even no. ",count_even)
print("odd no. ",count_odd)
print("both count.",count_even+count_odd)
print("sum even ",sum_even)
print(" sum odd ",sum_odd)
print("both sum ",sum_even+sum_odd)
print("even average ",sum_even//average_even)
print("odd average ",sum_odd//average_odd)
print("both average ",sum_even//average_even+sum_odd//average_odd)


