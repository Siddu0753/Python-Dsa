# print("missing number in the array")


nums=[9,6,4,2,3,5,7,0,1]

def mis(nums):
    n=len(nums)
    for i in range(0,n+1):
        if i not in nums:
            return i
       
print(mis(nums))
# # time complexity :0(n^2)   ,sc:O(1)


###################################################
print("optimal approaches")
def mis(nums):
    n=len(nums)
    freq={}
    for i in range(0,n+1):
        freq[i]=0
    for num in nums:
        freq[num]=1
    for k,v in freq.items():
        if v==0:
            return k
       
print(mis(nums))
#tc:O(3n)~O(n), sc:O(n)
###################################################

def mis(nums):
    n=len(nums)
    t1=0
    t2=0
    for i in range(0,n):
        t1+=nums[i]
    for j in range(0,n+1):
        t2+=j
    return t2-t1
       
print(mis(nums))

###################################################
def mis(nums):
    n=len(nums)
    t1=0
    t=(n*(n+1))//2
    for i in range(0,n):
        t1+=nums[i]
    
    return t-t1
       
print(mis(nums))
# tc:O(n),sc:O(1)



