a=["a","k",2,1,"s",5,"i",3]
print(a)
i=0
l=len(a)
n1=int(input("enter no--"))
while i<l:
    print(a[i-n1:])
    break
    i+=1

# --------------------


a=["a","k",2,1,"s",5,"i",3]
print(a)
i=0
n1=int(input("enter no--"))
list1=a[-n1:]
l=len(list1)
while i<l:
    print(list1[i])
    i+=1

# ------------------------


a=["a","k",2,1,"s",5,"i",3]
print(a)
i=0
l=len(a)
r=0
n1=int(input("enter no--"))
while i<n1:
    print(a[i-n1])
    i+=1

# ----------------------------


a=["a","k",2,"s",4,6,"r",3]
print(a)
n=int(input("enter no.--"))
r=a[-n:]
print(r)
