# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# total_marks=0
# l=len(marks)
# i=0
# a=0
# while i<l:
#     j=0
    
#     while j<len(marks[a]):
#         total_marks+=marks[a][j]
#         j+=1 
#     i+=1
#     a+=1      
# print(total_marks)





# average question 

marks = [78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]
total_marks=0
l=len(marks)
i=0
a=0
count=0
while i<l:
    j=0
    
    while j<len(marks[a]):
        total_marks+=marks[a][j]
        j+=1 
        count+=1
    print(total_marks//count)
    
    i+=1
    a+=1 

print(total_marks)


