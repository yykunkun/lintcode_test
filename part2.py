# 7设计一个算法，并编写代码来序列化和反序列化二叉树。将树写入一个文件被称为“序列化”，读取文件后重建同样的二叉树被称为“反序列化”。
# 如何反序列化或序列化二叉树是没有限制的，你只需要确保可以将二叉树序列化为一个字符串，并且可以将字符串反序列化为原来的树结构。
# 第七题写在solution类外边了，单独的类

# 这个TreeNode是题目给定的已知，就按着人家这个tree去写
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # 序列化，这步是BFS广度优先遍历，层序遍历，一层一层来
    # 这个傻叉题。。题目要的return是{}包着的str，不是set
    # 树转字符串
    def serialize(self, root):
        if root is None:
            return "{}"
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        while queue[-1] is None:
            queue.pop()
        ret = '{%s}' % ','.join([str(node.val) if node is not None else '#'
                                 for node in queue])
        print(ret)
        return ret

    # 字符串转树
    def deserialize(self, data):
        data = data.strip('\n')
        if data == '{}':
            return None
        vals = data[1:-1].split(',')
        root = TreeNode(int(vals[0]))
        queue = [root]
        isLeftChild = True
        index = 0
        for val in vals[1:]:
            if val != '#':
                node = TreeNode(int(val))
                if isLeftChild:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)

            if not isLeftChild:
                index += 1
            isLeftChild = not isLeftChild
        return root

    # 8给定一个字符串（以字符数组的形式给出）和一个偏移量，根据偏移量原地旋转字符串(从左向右旋转)。
    # 这题也傻逼，输入是An array of char
    # 这题是个形参实参的问题
    def rotateString(self, s, offset):
        if len(s) > 0:
            offset = offset % len(s)
            temp = (s + s)[len(s) - offset:len(s) - offset + len(s)]
            for i in range(len(temp)):
                s[i] = temp[i]

    # 11给定一个二叉查找树和范围[k1, k2]。按照升序返回给定范围内的节点值。
    # 先遍历，BFS顺序排列，拿到排序树的顺序序列，然后筛选正确值，排序输出
    def searchRange(self, root, k1, k2):
        ret = []
        totalOrder = []
        queue = []
        if root is None:
            return ret
        queue.append(root)
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        while queue[-1] is None:
            queue.pop()
        for i in range(len(queue)):
            if queue[i] is not None:
                totalOrder.append(queue[i].val)
        for i in range(len(totalOrder)):
            if totalOrder[i] >= k1 and totalOrder[i] <= k2:
                ret.append(totalOrder[i])
        ret.sort()
        return ret

    # 13对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target
    # 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。
    def strStr(self, source, target):
        if len(source) is None or target is None:
            return -1
        elif len(source) < len(target):
            return -1
        elif len(source) == 0 or len(target) == 0:
            return 0
        index = 0
        start = 0
        while (start + index) < len(source):
            print('start ' + str(start) + ' index ' + str(index))
            if source[start + index] == target[index]:
                index += 1
                if index == len(target):
                    return start
            else:
                index = 0
                start += 1
        return -1


# 12实现一个栈, 支持以下操作:
# push(val) 将 val 压入栈
# pop() 将栈顶元素弹出, 并返回这个弹出的元素
# min() 返回栈中元素的最小值
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, number):
        self.stack.append(number)
        if not self.min_stack or self.min_stack[-1] >= number:
            self.min_stack.append(number)

    def pop(self):
        num = self.stack.pop()
        if num == self.min_stack[-1]:
            self.min_stack.pop()
        return num

    def min(self):
        return self.min_stack[-1]


ss = Solution()
print(ss.strStr('abe', 'e'))
