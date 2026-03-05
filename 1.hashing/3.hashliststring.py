s="abcdefghiAjklmnAA@@opqB@rstuvwxyz"
q=["a","t","y","e","A","B","@"]

#>>>>>>>>>>>#for small leters
# def hashingstr(s,q):
#     hash_list=[0]*26
#     for ch in s:
#         asci_val=ord(ch)
#         index=asci_val-97
#         hash_list[index]+=1
#     for ch in q:
#         asci_val=ord(ch)
#         index=asci_val-97
#         print(ch,hash_list[index])
            
    
# hashingstr(s,q)


#tc:O(n+m)

#sc:O(26)~O(1)


#>>>>>>>>>>>>>>>>>>>>if chaptial or small or symbols
def hashingstr(s,q):
    hash_list=[0]*127
    for ch in s:
        asci_val=ord(ch)
        index=asci_val
        hash_list[index]+=1
    for ch in q:
        asci_val=ord(ch)
        index=asci_val
        print(ch,hash_list[index])
        
        
hashingstr(s,q)

            
# ch=ord("A")   
# print(ch) 
