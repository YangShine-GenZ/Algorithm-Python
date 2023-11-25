

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def detectCycle(self, head):
        '''

        a:2 steps
        b:1 step
        while():
            a.move(2)
            b.move(1)
        p = Face(a,b)
        a:1(start = head)
        b:1(start = p)
        while():
            a.move(1)
            b.move(1)
        q = Face(a,b)
        return q

        '''

        if head == None or head.next == None or head.next.next == None:
            return None
        a = head.next.next
        b = head.next
        while a!=None and b!=None:
            if a==b:
                break
            a = a.next
            b = b.next
            if a!=None:
                a = a.next

        if a==None or b== None:
            return None
        a = head
        while(a!=b):
            a = a.next
            b = b.next

        return a



head = ListNode(3)
head1 = ListNode(2)
head2 = ListNode(0)
head3 = ListNode(-4)
head.next = head1
head1.next = head2
head2.next = head3
head3.next = head1

s = Solution()
print(s.detectCycle(head).val)