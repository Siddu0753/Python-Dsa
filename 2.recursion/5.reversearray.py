

# def rev(a):
#     left=0
#     right=len(a)-1
    
    # if left<right:
    #     a[left],a[right]=a[right],a[left]
    #     left+=1
    #     right-=1
            
    # print(a)
    
    
    # b=a[3:2:-1]
    # print(b)
    
def rev(a,left,right):
    if left>=right:
        return
    a[left],a[right]=a[right],a[left]
    rev(a,left+1,right-1)
    
    
def reva(a,left,right):
    rev(a,left,right)
    return a

print(reva([1,2,3,4,5,6,7],2,5))