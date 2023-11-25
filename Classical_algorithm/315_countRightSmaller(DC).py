'''

给你一个整数数组 nums ，按要求返回一个新数组counts 。数组 counts 有该性质： counts[i] 的值是 nums[i] 右侧小于nums[i] 的元素的数量。


输入：nums = [5,2,6,1]
输出：[2,1,1,0]
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素


'''

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        '''
        DC(l,m)
        DC(m+1,r)

        Merge(l,m,r)

        '''
        count = [0]*(len(nums))
        index = [0]*len(nums)
        for i in range(len(nums)):
            index[i] = i

        def DivideSort(count,l,r):
            if l>=r:
                return
            if r-l==1:
                if nums[l]>nums[r]:
                    count[index[l]]+=1
                    return
                else:
                    nums[l],nums[r] = nums[r],nums[l]
                    index[l],index[r] = index[r],index[l]
                    return
            mid = (l+r)//2
            DivideSort(count,mid+1,r)
            DivideSort(count,l,mid)

            #merge
            temp = []
            temp1 = []
            left = l
            mid = (l+r)//2
            right = mid + 1
            for i in range(l,mid+1):
                '''
                while nums[right]>=nums[i] and right<=r:
                    temp.append(nums[right])
                    temp1.append(index[right])
                    right+=1
                '''
                while right<=r:
                    if nums[right]>=nums[i]:
                        temp.append(nums[right])
                        temp1.append(index[right])
                        right += 1
                    else:
                        break

                temp.append(nums[i])
                temp1.append(index[i])
                count[index[i]]+= r-right+1
            while right<=r:
                temp.append(nums[right])
                temp1.append(index[right])
                right+=1

            #debug
            print(temp)
            for j in range(l,r+1):
                nums[j] = temp[j-l]
                index[j] = temp1[j-l]

        DivideSort(count,0,len(nums)-1)


        return count





s = Solution()
l = [0,1,2]
#[1,2,5,2,2,1,1,0]
print(s.countSmaller(l))