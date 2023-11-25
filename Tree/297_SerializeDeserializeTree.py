'''
序列化和反序列化树
采用前序遍历
'''




# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

#Preorder
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        _str = ''
        if root == None:
            return 'None'
        else:
            return str(root.val)+' '+self.serialize(root.left)+' '+self.serialize(root.right)



    def deserialize(self, data):

        def delete(root):
            if root == None:
                return

            if root.left != None:
                if root.left.val == 'x':
                    root.left = None

            if root.right != None:
                if root.right.val == 'x':
                    root.right = None

            delete(root.left)
            delete(root.right)
            return


        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        s = data.split(' ')
        #debug
        print('split result:',s)
        print("s.length",len(s))
        '''
        if p = data.head() == 'None':
            return 
        else:
            new node = node(new = p)
            deserilize(p.left)
            deserilize(p.right)
        
        '''

        if len(s) == 1:
            if s[0] == 'None':
                return None
            else:
                return TreeNode(s[0])


        head = TreeNode('x')
        stack = []
        stack.append(head)
        for k in range(len(s)):
            #print("now_K:",k)
            top = stack.pop()
            if s[k] == 'None':
                top = None
                continue
            else:
                top.val = s[k]
                top.left = TreeNode('x')
                top.right = TreeNode('x')
                stack.append(top.right)
                stack.append(top.left)

        delete(head)

        return head













# Your Codec object will be instantiated and called as such:

#PreOrder 1,2,3,None,None,4,None,None,5,None,None,
# (<LEFT_SUB_TREE>)CUR_NUM(RIGHT_SUB_TREE)
root = TreeNode(1)
l2 = TreeNode(2)
l3 =TreeNode(3)
l4 = TreeNode(4)
l5 = TreeNode(5)

root.left = l2
root.right = l5
l2.left = l3
l2.right = l4



'''
ser = Codec()
des = ser.serialize(root)
print(des)
ans = ser.deserialize(des)
print(ser.serialize(ans))
'''

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(None))
print(deser.serialize(ans))




