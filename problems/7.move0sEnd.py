nums=[1,0,2,4,3,0,0,3,5,1]

print("by swaping inside the arry with out any external storage")
n=len(nums)
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i]==0 and nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]

print(nums)



#####################################################################
print("by using another list temp")
n1=[1,0,2,4,3,0,0,3,5,1]
n=len(n1)
temp=[]
for i in range(0,n):
    if n1[i]!=0:
        temp.append(n1[i])
print("temp values:",temp)

nt=len(temp)
print("length of temp",nt)

for j in range(0,nt):
    n1[j]=temp[j]

for i in range(nt,n):
    n1[i]=0
print(n1)



##############################################
print("using conditional statement")
n2=[1,0,2,4,3,0,0,3,5,1]

n=len(n2)
def mve(n2):
    if n==1:
        return
    i=0 
    while i<n:
        if n2[i]==0:
            break
        i+=1
    if i==n:
        return
    j=i+1
    while j<n:
        if n2[j]!=0:
            n2[i],n2[j]=n2[j],n2[i]
            i+=1
        j+=1
    return n2

print(mve(n2))







    