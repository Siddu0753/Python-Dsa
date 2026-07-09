
nums = [0]

ml=0
for num in nums:
    
    if num - 1 not in set(nums):
        l=1
        
        while num+l in set(nums):
            l+=1
        if l>ml:
            ml=l
    l=0

print(ml)


        
        

    

        






        