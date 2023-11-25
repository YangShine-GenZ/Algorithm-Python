#快速Pow(x,n)

'''

输入：x = 2.00000, n = 10
输出：1024.00000
x^n

n>0 n偶数-> pow(x,n) = pow(x,n/2)*pow(x,n/2)  x奇数-> pow(x,n) = pow(x,n-1)*x
n = 0  pow(x,n) = 1
n<0 n偶数 ->pow(x,n) = pow(x,n/2)*pow(x,n/2)  x奇数 -> pow(x,n) = pow(x,n+1)/x


'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            if n % 2 == 0:
                return self.myPow(x,int(n/2))*self.myPow(x,int(n/2))
            else:
                return self.myPow(x,int(n/2))*self.myPow(x,int(n/2))*x
        if n < 0:
            if n % 2 == 0:
                return self.myPow(x,int(n/2))*self.myPow(x,int(n/2))
            else:
                return self.myPow(x,int(n/2))*self.myPow(x,int(n/2))/x
'''



class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def func(n):
            if n == 0:
                return 1
            if abs(n) == 1:
                return x ** n
            res = func(n//2)
            res *= res
            if n % 2 == 1:
                res *= x
            return res
        return func(n)
'''





print(int(-5/2))
s  = Solution()
x = 2
n = -4
print(s.myPow(x,n))