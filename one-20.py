import heapq
# 1.给出两个整数 aa 和 bb , 求他们的和。



class Solution:
    # 2设计一个算法，计算出n阶乘中尾部零的个数
    # 计算n的阶乘中总共有多少个5
    def trailingZeros(self, n):
        ret = 0
        while (n != 0):
            ret += n // 5
            n = n // 5
        return ret

    # 计算阶乘
    def jiecheng(self, n):
        if n == 1:
            return 1
        else:
            return n * self.jiecheng(n - 1)

    # 3计算数字 k 在 0 到 n 中的出现的次数，k 可能是 0~9 的一个值。
    # 照着写就行了
    def digitCounts(self, k, n):
        ret = 0
        for i in range(int(n) + 1):

            for ch in str(i):
                print('#   ' + ch + '    ' + str(k))
                if ch == str(k):
                    ret += 1
        return ret

    # 4设计一个算法，找出只含素因子2，3，5 的第 n 小的数。
    # 如果已知丑数ugly，那么ugly * 2，ugly * 3和ugly * 5也都是丑数。
    # 求第n小的丑数，用最小堆解决。每次弹出堆中最小的丑数，然后检查它分别乘以2、3
    # 和5后的数是否生成过，如果是第一次生成，那么就放入堆中。第n个弹出的数即为第n小的丑数。
    # 后边数字间隔增大，用递增验证时间就超了
    def nthUglyNumber(self, n):
        heap = [1]
        visited = set([1])
        val = None
        for i in range(n):
            val = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if val * factor not in visited:
                    visited.add(val * factor)
                    heapq.heappush(heap, val * factor)
        return val

    # 5在数组中找到第k大的元素
    # 直接排序求就行了
    def kthLargestElement(self, n, nums):
        sortednums = sorted(nums, reverse=True)
        return sortednums[n - 1]

    # 517写一个程序来检测一个整数是不是丑数。丑数的定义是，只包含质因子2, 3, 5的正整数。比如6, 8就是丑数，但是14不是丑数因为他包含了质因子7。
    # 先求丑数，再求第n个
    def isUgly(self, n):
        m = int(n)
        if m <= 0:
            return False
        else:
            while (m >= 2 and m % 2 == 0):
                m = m // 2
            while (m >= 3 and m % 3 == 0):
                m = m // 3
            while (m >= 5 and m % 5 == 0):
                m = m // 5
            return m == 1


ss = Solution()
n = 1
m = [1, 3, 2, 4]
print(ss.kthLargestElement(n, m))
# while (True):
#     try:
#         n = input('input your number\n')
#         print(ss.nthUglyNumber(n))
#     except:
#         break
