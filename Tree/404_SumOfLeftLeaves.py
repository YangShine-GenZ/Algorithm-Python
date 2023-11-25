'''
给定二叉树的根节点 root ，返回所有左叶子之和。

输入: root = [3,9,20,null,null,15,7]
输出: 24
解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self,root) -> int:
        isLeaveNode = lambda node: node.left==None and node.right==None

        def dfs(root):
            if root == None:
                return 0
            ans = 0
            if root.left:
                if isLeaveNode(root.left):
                    ans += root.left.val
                else:
                    ans+=dfs(root.left)
            ans+=dfs(root.right)
            return ans

        return dfs(root)


