#checking if a number is palindrome or not

# def palin(n):
#     num=n
#     rev=0
#     l=0
#     while n>0:
#         l=n%10
#         rev=(rev*10)+l
#         n=n//10
#     if rev==num:
#         print("palin")
#     else:
#         print("not palin")
        
# palin(1221)


#======================================================
#checking if a string is palindrome or not using loop

# def palin(s):
#     n=len(s)
#     r=n-1
#     l=0
#     while l<r:
#         if s[l]!=s[r]:
#             return "not plain"
#         l+=1
#         r-=1
#     return "palin"
        
# print(palin("saab"))


#>>>>>>>>>>>>>>>>using recursion

def func(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return func(s,l+1,r-1)

print(func("saas",0,3))
    
    