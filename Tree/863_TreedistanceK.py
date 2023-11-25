'''

给定一个二叉树（具有根结点root），一个目标结点 target ，和一个整数值 k 。

返回到目标结点 target 距离为 k 的所有结点的值的列表。 答案可以以 任何顺序 返回


输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
输出：[7,4,1]
解释：所求结点为与目标结点（值为 5）距离为 2 的结点，值分别为 7，4，以及 1


'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List


class Solution:
    def distanceK(self, root, target, k: int) -> List[int]:



        def MakeParent(root,target):
            if root == None:
                return
            if root.val == target:
                l_target.append(root)
            if root.left:
                d[root.left] = root
                MakeParent(root.left,target)
            if root.right:
                d[root.right] = root
                MakeParent(root.right,target)

        def Dfs_k(root,k):
            if root == None or k<0:
                return None
            visited = {}
            s = []
            s.append((root,k))
            visited[root] = k
            while len(s)>0:
                p,i = s.pop()
                if i==0:
                    res.append(p.val)
                    continue
                if i<0:
                    continue
                if p.left and p.left not in visited:
                    s.append((p.left,i-1))
                    visited[p.left] = i-1
                if p.right and p.right not in visited:
                    s.append((p.right,i-1))
                    visited[p.right] = i-1
                if p in d and d[p] not in visited:
                    s.append((d[p],i-1))
                    visited[d[p]] = i-1


        l_target = []
        d = {}
        res = []
        MakeParent(root,target)
        print(d)
        print(l_target[0])
        Dfs_k(l_target[0],k)
        print(res)
        return res


#Test
l = []
for i in range(9):
     l.append(TreeNode(i))

l[3].left = l[5]
l[3].right = l[1]
l[5].left = l[6]
l[5].right = l[2]
l[2].left = l[7]
l[2].right = l[4]
l[1].left = l[0]
l[1].right = l[8]
s = Solution()
s.distanceK(l[3],5,2)