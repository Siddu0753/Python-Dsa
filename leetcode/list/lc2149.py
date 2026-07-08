
# nums=[3,1,-2,-5,2,-4]
nums = [2, -3, -1, 4]


def rearr(nums):
    
    
    result=[0]*len(nums)
    pv=0
    nv=1
    for num in nums:  
        if num>0:
            result[pv]=num
            pv+=2
        elif num<0 :
            result[nv]=num
            nv+=2
            
    return result
print(rearr(nums))



    