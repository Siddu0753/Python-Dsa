
nums=[5,-2,3,9,0,6,10,7]
print("by loop")
def rot(nums):
    n=len(nums)
    k=3
    for i in range(0,k):
        temp=nums[n-1]
        for j in range(n-2,-1,-1):
            nums[j+1]=nums[j]
        nums[0]=temp
    return nums

print(rot(nums))

print("optimized solution")
#optimized
nums1=[5,-2,3,9,0,6,10,7]
def rot(nums1):
    n=len(nums1)
    k=3
    rotations=k%n
    for i in range(0,rotations):
        temp=nums1[n-1]
        for j in range(n-2,-1,-1):
            nums1[j+1]=nums1[j]
        nums1[0]=temp
    return nums1

print(rot(nums1))

print("without function")
#without function
nums2=[5,-2,3,9,0,6,10,7]
k=1
for _ in range(0,k):
    e=nums2.pop()
    nums2.insert(0,e)
print(nums2)

print("through slicing")
#through slicing
nums3=[5,-2,3,9,0,6,10,7]
k=5
n=len(nums)
nums3[:]=nums3[n-k:]+nums3[:n-k]
print(nums3)

print("different method same solution")
#different method same solution
nums4=[5,-2,3,9,0,6,10,7]
k=5
n=len(nums4)
def rev(nums4,left,right):
    
    while left<right:
        nums4[left],nums4[right]=nums4[right],nums4[left]
        right-=1
        left+=1
    return nums4
print(rev(nums4,n-k,n-1))
print(rev(nums4,0,n-k-1))
print(rev(nums4,0,n-1))



    