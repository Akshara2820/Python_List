rupees=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
l=len(rupees)
i=0
Crorepati=0
Lakhpati=0
Dilwale=0

while i<l:
    if rupees[i]>=10000000:
        Crorepati+=1
    elif rupees[i]>100000:
        Lakhpati+=1
    else:
        Dilwale+=1
    i+=1
print(Crorepati,"croepati hai")
print(Lakhpati,"Lakhpati hai")
print(Dilwale,"Dilwale hai")