'''
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List


class Solution:
    def binaryTreePaths(self, root) -> List[str]:

        def PrintStack(l):
            s = ''
            for i in range(len(l) - 1):
                s = s + str(l[i].val) + '->'
            s = s + str(l[len(l) - 1].val)
            return s
        '''
        if root == None:
            return None
        res = []
        l = []
        prev = None
        tmp = root
        while tmp != None:
            l.append(tmp)
            tmp = tmp.left

        while len(l) > 0:
            p = l[-1]
            if p.left == None and p.right == None:
                res.append(PrintStack(l))
            if prev != p.right and p.right != None:
                tmp = p.right
                while tmp != None:
                    l.append(tmp)
                    tmp = tmp.left
            else:
                prev = p
                l.pop()
        print(res)
        return res
        '''

        def construct_path(root,path):
            if root == None:
                return
            path = path + str(root.val)
            if root.left == None and root.right == None:
                paths.append(path)
                return
            else:
                path = path+'->'
                construct_path(root.left,path)
                construct_path(root.right,path)


        paths = []
        construct_path(root,'')
        return paths





