# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        pos1 = l1
        pos2 = l2
        head = ListNode()
        signal = 0
        while pos1 or pos2:
            if not pos1:
                sum = pos2.val + carry
                pos2 = pos2.next
            elif not pos2:
                sum = pos1.val + carry
                pos1 = pos1.next
            else:
                sum = pos1.val+pos2.val + carry
                pos1 = pos1.next
                pos2 = pos2.next
            carry = 0 if sum <=9 else 1
            if signal == 0:
                head.val = sum %10
                curr = head
            else:
                curr.next = ListNode(sum%10)
                curr = curr.next
            signal = 1
        if carry !=0:
            curr.next = ListNode(carry)
        return head        
            