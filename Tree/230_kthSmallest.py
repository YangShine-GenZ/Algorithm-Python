'''
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

由于是二叉搜索树，所以使用中序遍历可以得到最小元素

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:


        def MidorderGet(root,k,l):
            if root == None:
                return

            if len(l) == k:
                return
            MidorderGet(root.left,k,l)

            if len(l) == k:
                return

            l.append(root.val)
            if len(l) == k:
                return

            MidorderGet(root.right, k, l)


        l = []
        MidorderGet(root,k,l)
        return l[k-1]

