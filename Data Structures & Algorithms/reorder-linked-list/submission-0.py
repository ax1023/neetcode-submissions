# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        rev = slow.next
        prev = slow.next = None

        while rev:
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp

        rev = prev
        while rev:
            temp1 = head.next
            temp2 = rev.next
            head.next = rev
            rev.next = temp1
            head = temp1
            rev = temp2
        