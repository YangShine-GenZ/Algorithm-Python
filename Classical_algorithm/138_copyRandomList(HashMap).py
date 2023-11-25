'''
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
构造这个链表的深拷贝。 深拷贝应该正好由 n 个 全新 节点组成
其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，
并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。


'''


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        d = {}
        p1 = head
        if p1 == None:
            return None

        while p1 != None:
            if p1 not in d:
                d[p1] = Node(p1.val, None, None)

            p1 = p1.next

        p1 = head

        while p1 != None:
            if p1.next == None:
                d[p1].next == None
            else:
                d[p1].next = d[p1.next]

            if p1.random == None:
                d[p1].random == None
            else:
                d[p1].random = d[p1.random]
            p1 = p1.next

        return d[head]