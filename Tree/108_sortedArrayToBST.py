'''
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：



'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        return self.InorderSort(nums, 0, len(nums) - 1)

    def InorderSort(self, nums, i, j):
        mid = (i + j) // 2
        if i == j:
            return TreeNode(nums[i])
        if i > j:
            return None
        node = TreeNode(nums[mid])
        node.left = self.InorderSort(nums, i, mid - 1)
        node.right = self.InorderSort(nums, mid + 1, j)
        return node
