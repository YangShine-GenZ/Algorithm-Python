#给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        p1 = head
        p2 = head

        for i in range(n):
            if p1==None:
                return head
            p1 = p1.next

        while(p1.next!=None):
            p1 = p1.next
            p2 = p2.next

        #delete p2.next
        p2.next = p2.next.next

        return head