
list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
n = len(list1) 
m = len(list2) 
for i in range(n): 
    for j in range(m): 
        if (list1[i] == list2[j]): 
            break
        if (j == m - 1): 
            print(list1[i]) 





list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
n = len(list1) 
m = len(list2) 
for i in list1: 
	
	if i not in list2:
		print(i)