num=[3,4,6,7,9,2,11,21,54,67,98]
i=0
l=len(num)
prime_no=[]
while i<l:
    list_element=num[i]
    j=2
    while list_element>j:
        if list_element%j==0:
            break
        j+=1
    else:
        prime_no.append (list_element)
    i+=1
print(prime_no)