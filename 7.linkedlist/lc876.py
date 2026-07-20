class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow


values = list(map(int, input("Enter values: ").split()))

head = ListNode(values[0])
current = head

for val in values[1:]:
    current.next = ListNode(val)
    current = current.next

sol = Solution()
middle = sol.middleNode(head)

print("Middle node:", middle.val)