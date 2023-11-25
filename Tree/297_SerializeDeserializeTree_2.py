'''
序列化和反序列化树
采用形式语言 BNF

T -> (T)num(T) | N
num-> MX
M->x
X->xX|null


'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Preorder
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root == None:
            return 'N'
        else:
            return '('+self.serialize(root.left)+')'+str(root.val)+'('+self.serialize(root.right)+')'


    def deserialize(self, data):

        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        '''
        parse(data,ptr):
            n= data[ptr]
            if n=='N':
                return None
                
                
            if n=='(':
                ptr0 = FindFisrt(')')
                ptr1 = FindSecond('(')
                t = TreeNode(MakeVal(data[ptr0:ptr1]))
                t.left = Parse(data,ptr0+1)
                t.right = Parse(data,ptr1+1)
        '''


        def parseInt(data,ptr):

            l = ''

            while data[ptr[0]]!='(' and data[ptr[0]]!=')':
                l = l + data[ptr[0]]
                ptr[0]+=1

            #print(l)
            return l



        def parse(data,ptr):
            '''

            :param data: str
            :param ptr: List[](just including one element)
            :return:
            '''


            n = data[ptr[0]]
            if n =='N':
                ptr[0]+=1
                return None

            if n == '(':
                node = TreeNode('x')
                #solve '('
                ptr[0]+=1
                node.left = parse(data,ptr)
                #solve ')'
                ptr[0]+=1
                node.val = parseInt(data,ptr)
                ptr[0] += 1
                node.right = parse(data,ptr)
                #solve ')'
                ptr[0]+=1
                return node



        ptr = [0]
        return parse(data,ptr)









# Your Codec object will be instantiated and called as such:

# (<LEFT_SUB_TREE>)CUR_NUM(RIGHT_SUB_TREE)


root = TreeNode(20)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)
l5 = TreeNode(5)

root.left = l2
root.right = l5
l2.left = l3
l2.right = l4


ser = Codec()
des = ser.serialize(root)
print(des)
ans = ser.deserialize(des)
print(ser.serialize(ans))


'''
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
print(deser.serialize(ans))
'''