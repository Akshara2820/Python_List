# enter how many you want element-5
# enter no.1
# enter no.2
# enter no.3
# enter no.4
# enter no.5
# true


n=int(input("enter how many you want element-"))
s1=[]
i=0
for i in range(n):
    a=int(input("enter no."))
    s1.append(a)
    
b=list(range(min(s1), max(s1)+1))
if s1==b:
    print("true")
else:
    print("false")


