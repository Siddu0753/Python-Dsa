
# nums=[3,1,-2,-5,2,-4]
nums = [2, -3, -1, 4]


def rearr(nums):
    
    n=len(nums)
    result=[0]*n
    pv=0
    nv=1
    for i in range(0,n):  
        if nums[i]>0 and pv<n:
            result[i]=nums[pv]
            pv+=2
        elif nums[i]<0 and nv<n:
            result[i]=nums[nv]
            nv+=2
            
    return result
print(rearr(nums))



    