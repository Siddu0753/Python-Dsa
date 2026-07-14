# #3 sum problem
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

###################################################
#first approach brute force solution
# nums = [-1,0,1,2,-1,-4]
# n=len(nums)
# my_set=set()

# for i in range(0,n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if nums[i]+nums[j]+nums[k]==0:
#                 temp=[nums[i],nums[j],nums[k]]
#                 temp.sort()
#                 my_set.add(tuple(temp))

# print([list(ans) for ans in my_set])
#O(n^3)-tc,O(no of triplets)-sc

####################################################
#little optimal
# nums = [-1,0,1,2,-1,-4]
# n=len(nums)
# result=set()
# for i in range(0,n):
#     my_set=set()
#     for j in range(i+1,n):
#         third=-(nums[i]+nums[j]) 
#         if third in my_set:
#             temp=[nums[i],nums[j],third]
#             temp.sort()
#             result.add(tuple(temp))
#         my_set.add(nums[j])
# print([list(ans) for ans in result])

# tc-O(n^2),sc-O(n)+O(no of triplets)

####################################################
#optimal solution

nums = [-1,0,1,2,-1,-4]
ans=[]
n=len(nums)
nums.sort()
for i in range (n):
    if i!=0 and nums[i]==nums[i-1]:
        continue
    #2pointers
    j=i+1
    k=n-1
    while j<k:
        total_sum=nums[i]+nums[j]+nums[k]
        if total_sum<0:
            j+=1
        elif total_sum>0:
            k-=1
        else:
            temp=[nums[i],nums[j],nums[k]]
            ans.append(temp)
            j+=1
            k-=1
            while j<k and nums[j]==nums[j-1]:
                j+=1
            while j<k and nums[k]==nums[k+1]:
                k-=1

print(ans)






        

    








