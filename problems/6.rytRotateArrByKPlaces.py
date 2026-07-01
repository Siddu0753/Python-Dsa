
nums=[5,-2,3,9,0,6,10,7]
def rot(nums):
    n=len(nums)
    k=3
    rotations=k%n
    for i in range(0,rotations):
        temp=nums[n-1]
        for j in range(n-2,-1,-1):
            nums[j+1]=nums[j]
        nums[0]=temp
    return nums

print(rot(nums))
