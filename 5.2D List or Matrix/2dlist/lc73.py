matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix=[[1,2,3],[4,0,6],[7,8,9]]

r=len(matrix)
c=len(matrix[0])


for i in range(0,r):
    for j in range(0,c):
        if matrix[i][j]==0:
            rt=matrix[i][0]
            ct=matrix[0][j]

for i in range(0,r):
    for j in range(0,c):
        if  matrix[i][0]==rt or matrix[0][j]==ct:
            matrix[i][j]=0
        





print(matrix)

