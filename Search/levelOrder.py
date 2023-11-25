'''

给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List

class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        l = []
        res = []
        if root == None:
            return []

        l.append((root,0))

        while len(l)>0:
            p,level = l.pop(0)
            if len(res) < level+1:
                res_t = []
                res_t.append(p.val)
                res.append(res_t)
            else:
                res[level].append(p.val)

            if p.left != None:
                l.append((p.left,level+1))

            if p.right != None:
                l.append((p.right,level+1))


        return res







