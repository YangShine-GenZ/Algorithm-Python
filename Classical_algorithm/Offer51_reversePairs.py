'''

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

输入: [7,5,6,4]
输出: 5

'''

from typing import List


def Merge(nums,l,m,r) ->int:
    '''
               Merge(l,m,r):

               left = l
               right = m+1
               temp = []

               for i in range(m+1,r+1):
                   while nums[left]<=nums[i] and left<=m:
                       temp.append(nums[left])
                       left+=1
                   n = FindPair(nums[i]) // compared with nums[left]
                   count += n
                   temp.append(nums[i])

               swap(nums[l:r+1],temp)
    '''
    count = 0
    left = l
    right = m+1
    temp = []
    for i in range(m+1,r+1):
        while nums[left] <= nums[i] and left <= m:
            temp.append(nums[left])
            left += 1
        temp.append(nums[i])
        if left>m:
            continue
        else:
            for j in range(left,m+1):
                if nums[j] > nums[i]:
                    count+=1

    while left<=m:
        temp.append(nums[left])
        left+=1
    print(temp)

    for m in range(l,r+1):
        nums[m] = temp[m-l]


    print(nums)

    return count


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''
        def DC(l,r):
            if (l>=r):
                return
            DC(l,(l+r)/2)
            DC((l+r)/2+1,r)
            
            Congrue(l,(l+r)/2,(l+r)/2+1,r)
        
        
        '''

        count = 0

        def MergeSort(l,r):
            if l>=r:
                return 0
            if r-l == 1:
                if nums[l]>nums[r]:
                    nums[r],nums[l] = nums[l],nums[r]
                    return 1
                else:
                    return 0

            mid = (l+r)//2
            count = MergeSort(l,mid)+MergeSort(mid+1,r)

            left = l
            m = (l+r)//2
            right = m + 1
            temp = []
            for i in range(m + 1, r + 1):
                while nums[left] <= nums[i] and left <= m:
                    temp.append(nums[left])
                    left += 1
                temp.append(nums[i])
                if left > m:
                    continue
                else:
                    count += (m-left+1)

            while left <= m:
                temp.append(nums[left])
                left += 1
            print(temp)

            for m in range(l, r + 1):
                nums[m] = temp[m - l]

            return count

        return MergeSort(0,len(nums)-1)




s = Solution()
l = [1,3,2,3,1]
#l = [7,5,8]

l1 = [1,3,2,3,1]
#print(Merge(l1,0,(len(l1)-1)//2,len(l1)-1))

print(s.reversePairs(l))
