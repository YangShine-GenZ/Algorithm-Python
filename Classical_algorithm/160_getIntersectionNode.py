'''
对于两条链表返回相交节点

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'

'''


# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        p1 = headA
        p2 = headB
        flag1 = 0
        flag2 = 0
        '''
        for(p1!=None,p2!=None):
            if(p1==p2): break
            p1 = p1.next
            p2 = p2.next
            if (p1.over(headA)): p1 = headB
            if (p2.over(headB)): p2 = headA
        return p1
        '''
        while p1 != None and p2 != None:
            if p1 == p2:
                break
            if p1.next == None and flag1 == 0:
                p1 = headB
                flag1 = 1
                if p2.next == None and flag2 == 0:
                    p2 = headA
                    flag2 = 1
                else:
                    p2 = p2.next
                continue
            if p2.next == None and flag2 == 0:
                p2 = headA
                flag2 = 1
                if p2.next == None and flag2 == 0:
                    p1 = headB
                    flag2 = 1
                else:
                    p1 = p1.next
                continue

            p1 = p1.next
            p2 = p2.next

        return p1