num=[50,40,23,70,56,100,18,]
l=len(num)
a=0
mini1=num[a]
i=0
x=num
while i<l:
    if x[i]<=mini1:
        mini1=x[i]
    i+=1
print(mini1)
y=0
mini2=num[y]
m=0
while m<l:
    if mini2>num[m]>mini1:
        mini2=num[m]
    m+=1
print(mini2)
