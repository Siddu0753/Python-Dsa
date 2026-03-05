# parameterized recursion
# def fun(sum,i,n):
#     if i>n:
#         print(sum)
#         return
#     fun(sum+i,i+1,n)
#     print(sum)
    
# fun(0,1,4)

def fib(sum,i,n):
    if i>n:
        print(sum)
        return
    fib(sum+i,i+1,n)
    print(sum)
fib(0,1,4)
