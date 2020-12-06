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
    # 这个题实属傻逼，没有为什么
    def rotateString(self, s, offset):
        length = len(s)
        s = s + s
        s = s[length - offset:length - offset + length]
        return s


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
ss = Solution()
strr = 'abcdefg'
input = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
offset = 3
print(ss.rotateString(input, offset))
