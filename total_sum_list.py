
n=30
n1=[10, 11, 12, 13, 14, 17, 18, 19]
s1=[]
i=0
c=0
l=len(n1)
while i<l:
    j=0
    while j<l:
        if n1[j]+n1[i]==n and n1[i]<n1[j]:
            s1.append([n1[i],n1[j]])
        j+=1
    i+=1
   	
print(s1)