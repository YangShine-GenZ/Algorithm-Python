'''
O(1) 时间插入、删除和获取随机元素

实现RandomizedSet 类：

RandomizedSet() 初始化 RandomizedSet 对象
bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。

'''

from random import  choice


class RandomizedSet:

    def __init__(self):
        self.rlist = []
        self.rdict = {}
        self.len = 0


    def insert(self, val: int) -> bool:
        if val in self.rdict:
            print("No inserting! The val in Set!")
            return False
        else:
            self.rlist.append(val)
            self.rdict[val] = len(self.rlist)-1
            print("Insert the Set:",val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.rdict:
            print("No removing! The val not in Set!")
            return False
        else:
            index = self.rdict[val]
            self.rlist[index] = self.rlist[-1]
            self.rdict[self.rlist[index]] = index
            self.rlist.pop()
            del self.rdict[val]
            print("removing the val:",val)
            return True


    def getRandom(self) -> int:
        x = choice(self.rlist)
        print("Getting random:",x)
        return x




'''
randomizedSet = RandomizedSet()
randomizedSet.insert(1) # 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomizedSet.remove(2) # 返回 false ，表示集合中不存在 2 。
randomizedSet.insert(2) # 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomizedSet.getRandom() # getRandom 应随机返回 1 或 2 。
randomizedSet.remove(1) # 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomizedSet.insert(2) # 2 已在集合中，所以返回 false 。
randomizedSet.getRandom() # 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
'''

randomizedSet = RandomizedSet()
randomizedSet.remove(0)
randomizedSet.remove(0)
randomizedSet.insert(0)
randomizedSet.getRandom()
randomizedSet.remove(0)
randomizedSet.insert(0)

