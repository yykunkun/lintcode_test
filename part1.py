import heapq  # 丑数那个题用的,堆
from collections import deque  #


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

    # 6合并两个有序升序的整数数组A和B变成一个新的数组。新数组也要有序。
    # 直接写就行了，没啥技术含量
    def mergeSortedArray(self, A, B):
        if len(A) == 0:
            return B
        if len(B) == 0:
            return A
        ret = A + B
        return (sorted(ret))


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


# 二叉树，不过这个没啥用，根题目不相关，二叉树写的很好，lintcode第7题，人家不让用，要按着人家写好的去遍历
class BinaryTree(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # 前序遍历，根→左→右
    def preorder(self):
        if self.data:
            print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    # 中序遍历,左→根→右
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        if self.data is not None:
            print(self.data)
        if self.right is not None:
            self.right.inorder()

    # 后序遍历，左→右→根
    def postorder(self):

        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.data is not None:
            print(self.data, end=' ')

    # 层序遍历
    def levelorder(self):
        # 返回某个节点的左孩子
        def LChild_Of_Node(node):
            return node.left if node.left else None

        # 返回某个节点的右孩子
        def RChild_Of_Node(node):
            return node.right if node.right else None

        # 层序遍历列表
        level_order = []
        # 是否添加根节点中的数据
        if self.data:
            level_order.append([self])

        # 二叉树的高度
        height = self.height()
        if height >= 1:
            # 对第二层及其以后的层数进行操作, 在level_order中添加节点而不是数据
            for _ in range(2, height + 1):
                level = []  # 该层的节点
                for node in level_order[-1]:
                    # 如果左孩子非空，则添加左孩子
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    # 如果右孩子非空，则添加右孩子
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                # 如果该层非空，则添加该层
                if level:
                    level_order.append(level)

            # 取出每层中的数据
            for i in range(0, height):  # 层数
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].data

        return level_order

    # 二叉树的高度
    def height(self):
        # 空的树高度为0, 只有root节点的树高度为1
        if self.data is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    # 二叉树的叶子节点
    def leaves(self):

        if self.data is None:
            return None
        elif self.left is None and self.right is None:
            print(self.data, end=' ')
        elif self.left is None and self.right is not None:
            self.right.leaves()
        elif self.right is None and self.left is not None:
            self.left.leaves()
        else:
            self.left.leaves()
            self.right.leaves()


ss = Solution()

# while (True):
#     try:
#         n = input('input your number\n')
#         print(ss.nthUglyNumber(n))
#     except:
#         break
