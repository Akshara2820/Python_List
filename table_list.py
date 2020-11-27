n=int(input("enter no how many you want table--"))
s=[]
i=1
while i<=n:
    j=1
    sm=[]
    while j<=10:
        sm.append(j*i)
        j+=1
    s.append(sm)
    i+=1
print(s)
