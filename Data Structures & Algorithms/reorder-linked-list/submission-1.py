# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,head):
        prev,curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def mergeList(self,list1,list2):
        if not list2:
            return list1
        if not list1:
            return list2
        next1 = list1.next
        next2 = list2.next
        list1.next = list2
        list2.next = self.mergeList(next1,next2)
        return list1
    
    def length(self,head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count

    def reorderList(self, head: Optional[ListNode]) -> None:
        length = self.length(head)
        if length<=1:
            return
        prev = None
        fast = slow = head
        while fast and fast.next and slow:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = None
        list1 = head
        list2 = slow
        list2 = self.reverseList(slow)
        self.mergeList(list1,list2)


