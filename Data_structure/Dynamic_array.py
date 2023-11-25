#实现动态数组


class LCArray:

    def __init__(self):
        self.array = [0]
        self.cur = 0
        self.maxsize = 1


    def push_back(self, n: int) -> None:
        #if full
        if(self.cur == self.maxsize):
            #create a new array
            self.maxsize = self.maxsize*2
            temp = [0 for i in range(self.maxsize)]
            #copy old array into new one
            # debugger print
            print("lengthen the array, the new size: ",self.maxsize)
            for i in range(self.cur):
                temp[i] = self.array[i]
            self.array = temp

        #not full
        self.array[self.cur] = n
        self.cur = self.cur+1
        #debugger print
        print("now push:",n)

    def pop_back(self) -> None:
        #print("pop:",self.array[self.cur])
        self.cur = self.cur-1


    def size(self) -> int:
        print(self.cur)
        return self.cur+1

    def index(self, idx: int) -> int:
        print("index:",self.array[idx])
        return self.array[idx]





#testLCArray
l = LCArray()
l.size() # 获取数组长度，此时数组为空，返回0
l.push_back(95) # 在数组末尾插入新元素95，返回null
l.pop_back() # 删除数组中的最后一个元素，返回null
l.size() # 获取数组长度，此时数组为空，返回0
l.push_back(37) # 在数组末尾插入新元素37，返回null
l.size() # 获取数组长度，返回1
l.index(0) # 返回数组中下标为0的元素37
l.pop_back() # 删除数组中的最后一个元素，返回null
l.push_back(28) # 在数组末尾插入新元素28，返回null



# Your LCArray object will be instantiated and called as such:
# obj = LCArray()
# obj.push_back(n)
# obj.pop_back()
# param_3 = obj.size()
# param_4 = obj.index(idx)