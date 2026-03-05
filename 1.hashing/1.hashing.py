

def hashing(n,m):
    for num in m:
        count=0
        for x in n:
            if x==num:
                count+=1
        print(count)
        
hashing([1,2,3,4,5,6,7,8,9,9,5,7,10],[2,3,4,22,7,5,6,8,9])