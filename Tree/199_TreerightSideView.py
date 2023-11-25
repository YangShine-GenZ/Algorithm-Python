'''
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

输入: [1,2,3,null,5,null,4]
输出: [1,3,4]


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import  List


class Solution:
    def rightSideView(self, root) -> List[int]:
        '''
        stack(root,0)
        res[0] = root
        while(!empty(stack)):
            (top,i) = stack.pop()
            if i not in res[]:
                res[i] = top->val
            if top->left:
                stack.push(top->left,i+1)
            if top->right:
                stack.push(top->right,i+1)

        '''
        if root == None:
            return []
        stack = []
        resdict = {}
        res = []
        length = 0
        stack.append((root, 0))
        while len(stack) > 0:
            top, i = stack.pop()
            if i not in resdict:
                length += 1
                resdict[i] = top.val
            if top.left != None:
                stack.append((top.left, i + 1))
            if top.right != None:
                stack.append((top.right, i + 1))

        for i in range(length):
            res.append(resdict[i])

        return res