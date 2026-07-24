nums = [1,2,3,4,5,6,7]
k = 3

def fun(nums,k):
    n=len(nums)
    k=k%n
    for i in range(0,k):
        temp=nums[n-1]
        for j in range(n-2,-1,-1):
            nums[j+1]=nums[j]
        nums[0]=temp
    return nums
print(fun(nums,k))



    