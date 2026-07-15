matrix = [[1,2,3],[4,5,6],[7,8,9]]
if not matrix or not matrix[0]:
    print([])

r=len(matrix[0])-1
l=0
t=0
b=len(matrix)-1
result=[]

while t<=b and l<=r:
    for i in range(l,r+1):
        result.append(matrix[t][i])
    t+=1
    for i in range(t,b+1):
        result.append(matrix[i][r])
    r-=1
    if t<=b:
        for i in range(r,l-1,-1):
            result.append(matrix[b][i])
        b-=1
    if l<=r:
        for i in range(b,t-1,-1):
            result.append(matrix[i][l])
        l+=1
    


print(result)




      


        
         
        
        