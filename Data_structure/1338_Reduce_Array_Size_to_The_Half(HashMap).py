'''
给你一个整数数组 arr。你可以从中选出一个整数集合，并删除这些整数在数组中的每次出现。

返回 至少 能删除数组中的一半整数的整数集合的最小大小。

输入：arr = [3,3,3,3,5,5,5,2,2,7]
输出：2 : 选择数字[3,7]

'''

from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        dics = {}
        total = 0
        count = 0
        for i in range(len(arr)):
            if arr[i] not in dics:
                dics[arr[i]] = 1
            else:
                dics[arr[i]]+=1

        #debug
        print(dics)


        sorted_dics = {k:v for k,v in sorted(dics.items(),key=lambda x:x[1],reverse=True)}

        #debug
        print(sorted_dics)


        for key,value in sorted_dics.items():
            total += value
            count+=1
            if total*2 >= len(arr):
                break


        return count



s = Solution()
#l = [3,3,3,3,5,5,5,5,5,2,2,7]
#l = [1,2,3,4,5,6,7,8,9,10]

l = [1,9]
print(s.minSetSize(l))
