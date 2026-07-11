matrix = [[1,2,3],[4,5,6],[7,8,9]]

# r=len(matrix)
# c=len(matrix[0])
# res=[[0]*r for _ in range(c)]

# for i in range(r-1,-1,-1):

#     for j in range(c-1,-1,-1):
#         res[i][j]=matrix[j][i]
# for i in range(len(res)):
#     res[i] = res[i][::-1]


# print(res)

###########################################3

# r=len(matrix)
# c=len(matrix[0])
# res=[[0]*r for _ in range(c)]

# for i in range(r-1,-1,-1):

#     for j in range(c-1,-1,-1):
#         res[j][(r-1)-i]=matrix[i][j]



# print(res)

###############################################################

# n=len(matrix)

# for i in range(0,n):

#     for j in range(i+1,n):
#         matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
# for i in range(n):
#     matrix[i] = matrix[i][::-1]


# print(matrix)


################################################################
n=len(matrix)

for i in range(0,n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for i in range(n):
    matrix[i].reverse()


print(matrix)