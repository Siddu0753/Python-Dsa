                           #DSA HERE WE GO
#=====================================================
#printing last digit
# n=5469
# while n>0:
#     last=n%10
#     print(last)
#     n=n//10


#-------------------------------------------------------
#counting no of numb in digit
# n=4567
# num=n
# count=0
# while num>0:
#     num=num//10
#     count+=1
    
# print(count)


#==========================================================
#counting no of digitds using log
# from math import *
# def count(num):
#     if num==0:
#         return 1
#     n=int(log10(num)+1)
#     return n

# print(count(3452))


#================================================================
#reversing a number and also checking if it is palindrome
# def rev(num):
#     n=num
#     rev=0
#     l=0
#     while num>0:
#         l=num%10
#         rev=(rev*10)+l
#         num=num//10
        
#     if n==rev:
#         print('palindrome')
#     else:
#         print('not palin') 
               
# rev(121)
#tc:O(log10(n))
#sc:O(1)
    
    

#=====================================================
#checking whether a number is armstrong 
# def armst(num):
#     nod=len(str(num))
#     c=num
#     total=0
#     while num>0:
#         n=num%10
#         total=total+(n**nod)
#         num=num//10
#     if total==c:
#         print("its a armstrong")
#     else:
#         print("not armstrong")
        
# armst(153)

#tc:
#sc: