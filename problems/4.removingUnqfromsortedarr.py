
arr=[1,1,1,3,3,3,5,5,5,5,7,7,7,8,8,8,9,9]

# def fun(arr):
#     dict={}
#     n=len(arr)
#     for i in range(0,n):
#         dict[arr[i]]=0
        
#     j=0
#     for key in dict:
#         arr[j]=key
#         j+=1
#     return j

# print(fun(arr))


def fun2(arr):
    n=len(arr)
    if n==1:
        return 1
    i=0
    j=i+1
    while j<n:
        if arr[j]!=arr[i]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    return i+1

print(fun2(arr))





