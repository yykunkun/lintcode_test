# 7设计一个算法，并编写代码来序列化和反序列化二叉树。将树写入一个文件被称为“序列化”，读取文件后重建同样的二叉树被称为“反序列化”。
# 如何反序列化或序列化二叉树是没有限制的，你只需要确保可以将二叉树序列化为一个字符串，并且可以将字符串反序列化为原来的树结构。
# 第七题写在solution类外边了，单独的类

# 这个TreeNode是题目给定的已知，就按着人家这个tree去写
class TreNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # 序列化，这步是BFS广度优先遍历，
    # 这个傻叉题。。题目要的return是{}包着的str，不是set
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

        ret = '{'
        for node in queue:
            if node is not None:
                ret += str(node.val) + ','
            else:
                ret += '#,'
        ret = ret[:-2]

        # return '{%s}' % ','.join([str(node.val) if node is not None else '#'
        #                           for node in queue])
        return ret + '}'

# write your code here
