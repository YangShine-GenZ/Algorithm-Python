'''
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

输入：deck = [1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

'''

from typing import List
from math import  gcd



class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        R_dict = {}
        for i in range(len(deck)):
            if deck[i] not in R_dict:
                R_dict[deck[i]] = 1
            else:
                R_dict[deck[i]]+=1

        #debug
        print(R_dict)
        first = 1
        for j in R_dict.values():
            if first == 1:
                val = gcd(j,j)
                first = 0
            else:
                val = gcd(j,val)

        #debug
        print(val)
        if val>=2:
            return True
        return  False

s = Solution()
#l = [1,2,3,4,4,3,2,1]
l= [1,1,1,2,2,2,3,3]
s.hasGroupsSizeX(l)








