nums=[4,3,5,6,7,2,1,0]

def secondlargest(nums):
    largest1=float("-inf")
    largest2=float("-inf")
    n=len(nums)
    for i in range(0,n):
        if nums[i]>largest1:
            largest2=largest1
            largest1=nums[i]
            
        elif nums[i]>largest2 and nums[i]<largest1:
            largest2=nums[i]
    return largest2

print(secondlargest(nums))  


# def secondlargest(nums):
#     largest1=float("-inf")
#     largest2=float("-inf")
#     n=len(nums)
#     for i in range(0,n):
#         largest1=max(nums[i],largest1)
#     for j in range(0,n):
#         if nums[j]>largest2 and nums[j]!=largest1:
#           largest2=nums[j]

#     return largest2

# print(secondlargest(nums))


