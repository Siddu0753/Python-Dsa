
nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
target=3
def lowerbound(self,nums,target):
    n=len(nums)
    lb=n
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:

            low=mid+1
    return lb
def higherbound(self,nums,target):
    n=len(nums)
    hb=n
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            hb=mid
            high=mid-1
        else:

            low=mid+1
    return hb
def searchRange(self, nums, target):
    lb=self.lowerbound(nums,target)
    if lb == len(nums) or nums[lb] != target:
        return [-1, -1]
    hb=self.higherbound(nums,target)
    
    return([lb,hb-1])

        
        
        
        

        

print(fun(nums,target))


# def lowerbond(nums,target):
#     lb=-1
#     n=len(nums)
#     low=0
#     high=n-1
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]>=target:
#             lb=mid
#             high=mid-1
#         else:
#             low=mid+1
#     return lb

# print(lowerbond([1,2,3,4,5],5))


# def lowerbond(nums,target):
  
#     n=len(nums)
#     ub=n
#     low=0
#     high=n-1
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]>target:
#             ub=mid
#             high=mid-1
#         else:
#             low=mid+1
#     return ub

# print(lowerbond([1,1,1,1,2,3,4,5,5,5],1))