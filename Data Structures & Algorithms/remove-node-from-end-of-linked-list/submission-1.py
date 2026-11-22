# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def length(self,head):
        count = 0
        while head:
            head = head.next
            count +=1
        return count
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = self.length(head)
        if n == len:
            return head.next
        count = 1
        curr = head
        while curr:
            if count == len - n:
                if curr.next:
                    curr.next = curr.next.next
                break
            curr = curr.next
            count +=1
        return head

                

            