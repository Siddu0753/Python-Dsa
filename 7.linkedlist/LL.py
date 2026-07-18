


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

# node1=Node(5)
# node2=Node(10)
# node3=Node(34)
# node4=Node(3)


# node1.next=node2
# node2.next=node3
# node3.next=node4

# print(node1)
# print(node1.val)


class singleLL:
    def __init__(self)->None:
        self.head=None
    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node


    def traverse(self):
        if self.head is None:
            print("sll is empty")
        else:
            current=self.head
            while current is not None:
                print(current.val,end=" ")
                current=current.next
            print()

        def delete(self,val):
            temp=self.head
            if temp.next is not None:
                if temp.val==val:
                    self.head=temp.next
                    return
                else:
                    found=False
                    prev=None
                    while temp is not None:
                        if temp.val==val:
                            found=True
                            break
                        prev=temp
                        temp=temp.next

                    if found:
                        prev.next=temp.next
                        return
                    else:
                        print("node not found")


sll=singleLL()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

sll.traverse()
    
