def hashlist(n,m):
    hash_list={}
    for num in range(0,len(n)):
        hash_list[n[num]]=hash_list.get(n[num],0)+1
    for num in m:
        if num<0 or num>10:
            print(num,0)
        else:
            print(num,hash_list[num])
    

    
    
    
    
hashlist([1,2,3,4,5,6,7,8,9,9,5,7,10],[2,3,4,22,7,5,6,8,9])