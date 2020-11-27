# enter the no--2
# enter no--1
# enter no--2
# [200]



n=int(input("enter the no--"))
s=[]
i=0
even=[]
odd=[]
while i<n:
    n1=int(input("enter no--"))
    s.append (n1)
    if s[i]%2==0:
        even.append(s[i]*100)
    else:
        odd.append(s[i]*-1)
    i+=1
print(even)
print(odd)


# --------------------------




a=[2,3,5,8,12,10,7,9]
i=0
l=len(a)
s=[]
while i<l:
	if a[i]%2==0:
		s.append(a[i])
	i+=1
print(s)