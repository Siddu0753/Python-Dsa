#kth largest element in an array

nums = [3,2,1,5,6,4] 
k = 2
n=len(nums)

l=float("-inf")
for i in range(0,n):
    if nums[i]>l:
        l=nums[i]
        while k:
            nums.pop(i)



