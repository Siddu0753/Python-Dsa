# reverse a linkedlist


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverse(self, head):
        current=head 
        prev=None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
        



values = list(map(int, input("Enter values: ").split()))

head = ListNode(values[0])
current = head

for val in values[1:]:
    current.next = ListNode(val)
    current = current.next
sol = Solution()
reverse = sol.reverse(head)

while reverse:
    print(reverse.val, end=" ")
    reverse = reverse.next



