
# for loop



# num=[50,40,23,70,56,12,18,7]
# s=0
# min=num[s]
# for i in num:
#     if i<=min:
#         min=i
# print(min)


# while loop



num=[50,40,23,70,56,12,18,7]
l=len(num)
a=0
s=num[a]
i=0
x=num
while i<l:
    if x[i]<=s:
        s=x[i]
    i+=1
print(s)