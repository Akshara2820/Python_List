
n=[[1,2,3],[4,5,6],[7,8,9]]
i=0
c=0
l=len(n)
while i<l:
    j=0
    while j<l:
        if n[c][j]==2 or n[c][j]==6 :
            print(n[c][j])
        j+=1
    c+=1
    i+=1