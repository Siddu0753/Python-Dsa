#Merge 2 Sorted Arrays Without Duplicates 

n1=[1,1,1,2,3,4,7,8]
n2=[1,2,3,5,9,10,11,12]

result=[]
i=0
j=0
n=len(n1)
m=len(n2)
while i<n and j<m:
    if n1[i]<=n2[j]:
        if len(result)==0 or result[-1]!=n1[i]:
            result.append(n1[i])
        i+=1
    else:
        if len(result)==0 or result[-1]!=n2[j]:
            result.append(n2[j])
        j+=1
while i<n:
    if len(result)==0 or result[-1]!=n1[i]:
            result.append(n1[i])
    i+=1
while j<m:
    if len(result)==0 or result[-1]!=n2[j]:
            result.append(n2[j])
    j+=1
print(result)