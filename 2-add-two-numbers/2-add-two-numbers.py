# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ptr = ListNode(0)
        carry = 0
        
        while l1 or l2:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            ptr.next = ListNode((v1 + v2 + carry) % 10)
            ptr = ptr.next
            carry = (v1 + v2 + carry) // 10
            
        if carry:
            ptr.next = ListNode(1)
            
        return ans.next