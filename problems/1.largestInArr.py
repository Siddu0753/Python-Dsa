nums=[4,3,5,6,7,2,1,0]

# def largest(nums):
#     larg=nums[0]
#     for i in range(0,len(nums)):
#         if nums[i]>larg:
#             larg=nums[i]
#     return larg
# print(largest(nums))

# def largest(nums):
#     larg=nums[0]
#     for i in range(0,len(nums)):
#         larg=max(nums[i],larg)
#     return larg
# print(largest(nums))

def largest(nums):
    larg=float("-inf")
    for i in range(0,len(nums)):
        if nums[i]>larg:
            larg=nums[i]
    return larg
print(largest(nums))

