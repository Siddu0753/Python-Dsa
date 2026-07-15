#4 sum
#########################################################################
# brute force solution
# nums = [1,0,-1,0,-2,2]
# n=len(nums)
# if n<4:print([])
# my_set=set()
# target=1
# for i in range(0,n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             for l in range(k+1,n):
#                 total=nums[i]+nums[j]+nums[k]+nums[l]
#                 if total==target:
#                     temp=[nums[i],nums[j],nums[k],nums[l]]
#                     temp.sort()
#                     my_set.add(tuple(temp))
# result=[]
# for ans in my_set:
#     result.append(list(ans))

# print(result)

# tc-O(n^4),sc-O(n)


##########################################################################

# better solution 3loop

# nums = [1,0,-1,0,-2,2]
# n=len(nums)
# my_set=set()
# target=1

# for i in range(0,n):
#     for j in range(i+1,n):
#         hash_set=set()
#         for k in range(j+1,n):
#             forth=target-(nums[i]+nums[j]+nums[k])
#             if forth in hash_set:
#                 temp=[nums[i],nums[j],nums[k],forth]
#                 temp.sort()
#                 my_set.add(tuple(temp))
#             hash_set.add(nums[k])
# result=[]
# for ans in my_set:
#     result.append(list(ans))


# print(result)
# tc:O(n^3) sc:O(n)

#########################################################################

nums=[1,1,1,1,2,2,3,3,3,4,4,4,5,5]
n=len(nums)
target=8
ans=[]
nums.sort()
for i in range(0,n):
    
    if i>0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1,n):
        if j >i+1 and nums[j]==nums[j-1]:
            continue
        k=j+1
        l=n-1
        while k<l:
            total=nums[i]+nums[j]+nums[k]+nums[l]
            if total==target:
                ans.append([nums[i],nums[j],nums[k],nums[l]])
                k+=1
                l-=1
                while k<l and nums[k]==nums[k-1]:
                    k+=1
                while l>k and nums[l]==nums[l+1]:
                    l-=1
            elif total<target:
                k+=1
            else:
                l-=1
print(ans)

# O(n^2*n)~O(n^3), sc:O(1)or O(no of ans)


