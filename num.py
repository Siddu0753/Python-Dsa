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

#tc:O(log10(n))
#sc:O(1)


#================================================
#prime factors in a list
# def primef(num):
#     c=num
#     list=[]
#     for i in range (1,num+1):
#         if c%i==0:
#             list.append(i)
#     return list
# print(primef(10))

#tc:O(n)
#sc:O(k) k should be total number of factors

#>>>>>>>>>>>>>>>>better solution
# def primef(num):
#     c=num
#     list=[]
#     for i in range (1,num//2):
#         if c%i==0:
#             list.append(i)
#     list.append(num)
#     return list
# print(primef(20))

# tc:O(n/2)~~O(n)
# sc:O(k) k should be total number of factors


#>>>>>>>>>>>>optimal solution
# from math import sqrt
# def primef(num):
#     c=num
#     list=[]
#     for i in range (1,int(sqrt(num))+1):
#         if c%i==0:
#             list.append(i)
#             if c//i!=i:
#                 list.append(c//i)
#     list.sort()#O(nlog(n)
#     return list
# print(primef(10))

#tc:O(nlog(n))+O(√n)
#sc:O(k) k should be total number of factors




#==================================================



        