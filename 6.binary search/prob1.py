###############################################
# iterative approach(prefered)

def binarysearch(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

print(binarysearch([1,2,3,4,5],5))

################################################
#recursive approach

def binarysearch(nums,low,high):
    n=len(nums)
    target=5
    if low>high:
        return -1

    mid=(low+high)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        binarysearch(nums,mid+1,high)
    else:
        return binarysearch(nums,low,mid-1)


print(binarysearch([1,2,3,4,5],5))

##################################################
# tc=log base 2 of n were n is the number of elements
# sc=O(1)
