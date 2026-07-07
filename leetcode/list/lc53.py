print("maximum subarry sum")

nums=[-2,1,-3,4,-1,2,1,-5,4]

def subsum(nums):
    n=len(nums)
    csum=0
    msum=nums[0]
    for i in range(0,n):
        csum+=nums[i]
        if csum>msum:
            msum=csum
        if csum<0:
            csum=0

    return msum

print(subsum(nums))
        



        


            
