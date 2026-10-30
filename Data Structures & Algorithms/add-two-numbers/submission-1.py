# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0

        cur = ListNode(None, None)

        dummy = ListNode(0, cur)

        prev = dummy

        while l1 or l2:
            if l1 and l2:
                cur.val = (l1.val + l2.val + carry) % 10
                carry = ((l1.val + l2.val + carry) >= 10)
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                cur.val = (l2.val + carry) % 10
                carry = ((l2.val + carry) >= 10)
                l2 = l2.next
            elif not l2:
                cur.val = (l1.val + carry) % 10
                carry = ((l1.val + carry) >= 10)
                l1 = l1.next
            nxt = ListNode(None, None)
            cur.next = nxt
            prev = cur
            cur = cur.next

        if carry:
            cur.val = 1
        else:
            prev.next = None
        

        return dummy.next