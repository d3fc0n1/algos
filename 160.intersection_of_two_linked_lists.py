# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a  = set()
        while headA:
            if headA:
                a.add(headA)
                headA = headA.next
        
        while headB:
            if headB in a:
                return headB
            else:
                headB = headB.next
        
#         # two-pointer approach
#         pa = headA
#         pb = headB
#         while pa != pb:
#             pa = pa.next if pa != None else headB
#             pb = pb.next if pb != None else headA
        
#         return pa
                

