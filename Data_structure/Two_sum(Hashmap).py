#查找两数之和
#nums = [2,7,11,15], target = 9
#输出 [0,1]表述 nums[0]+nums[1] = 9
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Res_list = []
        Mem_dict = {}
        for i,num in enumerate(nums):
            #if (target-num) in dict
            if target-num in Mem_dict:
                if Mem_dict[target-num]!=i:
                    Res_list = [Mem_dict[target-num],i]
                    break
            #reserve the num in dict
            Mem_dict[num] = i
        return Res_list

nums = [3,2,4]

solution = Solution()

print(solution.twoSum(nums,target=6))