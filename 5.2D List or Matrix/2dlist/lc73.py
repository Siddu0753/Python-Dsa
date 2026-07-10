matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix=[[1,2,3],[4,0,6],[7,8,9]]

# r=len(matrix)
# c=len(matrix[0])


# for i in range(0,r):
#     for j in range(0,c):
#         if matrix[i][j]==0:
#             matrix[i][0]
#             matrix[0][j]

# for i in range(0,r):
#     for j in range(0,c):
#         if  matrix[i][0]==rt or matrix[0][j]==ct:
#             matrix[i][j]=0
        
# print(matrix)
########################################################
rows = len(matrix)
cols = len(matrix[0])

firstRow = False
firstCol = False

# Check first row
for j in range(cols):
    if matrix[0][j] == 0:
        firstRow = True
        break

# Check first column
for i in range(rows):
    if matrix[i][0] == 0:
        firstCol = True
        break

# Use first row and first column as markers
for i in range(1, rows):
    for j in range(1, cols):
        if matrix[i][j] == 0:
            matrix[i][0] = 0
            matrix[0][j] = 0

# Update inner matrix
for i in range(1, rows):
    for j in range(1, cols):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0

# Zero first row if needed
if firstRow:
    for j in range(cols):
        matrix[0][j] = 0

# Zero first column if needed
if firstCol:
    for i in range(rows):
        matrix[i][0] = 0
print(matrix)