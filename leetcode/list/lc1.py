
# nums = [2,7,11,15], target = 9
# def twoSum(nums, target):
#         n=len(nums)
#         result=[]
#         for i in range(0,n):
#             for j in range(i+1,n):
#                 if target==nums[i]+nums[j]:
#                     result.append(i)
#                     result.append(j)


#         return result
# print(twoSum(nums, target))
# # tc:O(n^2),sc:O(1)


############################################################
print("optimized solution")
nums = [2,7,11,15]
target = 9
def twoSum(nums, target):
      n=len(nums)
      result={}
      need=0
      
      for i in range(0,n):  
            need=target-nums[i]
            if need not in result:
                  result[nums[i]]=i
            else:
                  return [result[need],i]
                
       
print(twoSum(nums, target))
# tc:O(n),sc:O(n)