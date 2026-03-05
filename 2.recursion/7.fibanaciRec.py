

# def fun(sum,i,n):
#     a=[]
#     if(i>n):
#         print(sum,a)
#         return
#     fun(sum+i,i+1,n)
#     a.append[sum]
    
    
# fun(0,1,5)
    
#=================================================
# fibunacci 
# def fun(n):
#     a=[]
#     for i in range(0,9):
#         if i==0:
#             a.append(0)
            
#         elif i==1:
#             a.append(1)
            
#         elif i>1:
#             b=a[i-1]+a[i-2]
#             a.append(b)
            
        
#     return a[n]
    
# print(fun(7))


#>>>>>>>>>recursion
def fun(n):
    
    if n<=1:
        return n
    return fun(n-1)+fun(n-2)
    
            
        
    
    
print(fun(7))
