'''
实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。
指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
int next()将指针向右移动，然后返回指针处的数字。
注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.l = []
        self.pointer = 0
        self.Fnum = -float('inf')
        self.Inorder(root)
        return

    def Inorder(self,root):
        if root == None:
            return
        self.Inorder(root.left)
        self.l.append(root.val)
        self.Inorder(root.right)


    def next(self) -> int:
        if self.hasNext()==False:
            return None
        else:
            res = self.l[self.pointer]
            self.pointer+=1
            return res




    def hasNext(self) -> bool:
        if self.pointer == len(self.l):
            return False
        else:
            return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()