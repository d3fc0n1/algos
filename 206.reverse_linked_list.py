# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
#     # recursive--------------------------------
#     return_head = ListNode()
    
#     def reverse_ll(self, curr):
#         if curr == None:
#             return
        
#         if curr.next == None:
#             self.return_head = curr
#             return
        
#         self.reverse_ll(curr.next)
#         curr.next.next = curr
#         curr.next = None
        
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        
        # stack--------------------------------
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
            
        dummy = ListNode(-1)
        head = dummy
        while stack:
            head.next = ListNode(stack.pop())
            head = head.next
            
        return dummy.next

#         # iterative----------------------------
#         prev = None
#         curr = head
        
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
        
#         return prev
        
        # # recursive----------------------------
        # self.reverse_ll(head)
        # return self.return_head
    
        
            