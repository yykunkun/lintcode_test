class Solution:
    # 21题目将给出两个圆A和B的圆心坐标(x,y)和半径r，现给你一个点P,使圆A圆心沿直线运动至点P。
    # 请问圆A在运动过程中是否会与圆B相交？（运动过程包括起点和终点）
    # 若会相交返回1，否则返回-1。
    # position是个[],里边有8个值
    # 这个题就转化成了，圆心A移动前后，到圆心B的最小距离，是不是大于两个圆半径的和

    def IfIntersect(self, position):
        XA, YA = position[0], position[1]
        print('圆A的圆心 ' + str(XA) + ' ' + str(YA))
        rA = position[2]
        print('圆A半径 ' + str(rA))
        XB, YB = position[3], position[4]
        print('圆B的圆心 ' + str(XB) + ' ' + str(YB))
        rB = position[5]
        print('圆B半径 ' + str(rB))
        XP, YP = position[6], position[7]
        print('P点坐标 ' + str(XP) + ' ' + str(YP))
        R = rA if rA >= rB else rB
        r = rB if rA >= rB else rA
        print('R= ' + str(R))
        print('r= ' + str(r))
        print('(R+r)平方 ' + str((R + r) ** 2))
        print('(R-r)平方 ' + str((R - r) ** 2))

        if XA == XP and YA == YP:
            if ((XA - XB) ** 2 + (YA - YB) ** 2 >= (R - r) ** 2) and ((XA - XB) ** 2 + (YA - YB) ** 2 <= (R + r) ** 2):
                return 1
            else:
                return -1
        else:
            Xab, Yab = XB - XA, YB - YA  # 向量AB坐标
            Xap, Yap = XP - XA, YP - YA  # 向量AP坐标
            Xpa, Ypa = XA - XP, YA - YP  # 向量PA坐标
            Xpb, Ypb = XB - XP, YB - YP  # 向量PB坐标
            cosBAP = Xab * Xap + Yab * Yap
            cosBPA = Xpa * Xpb + Ypa * Ypb
            # 直线AP的方程
            # (XP-XA)y=(YP-YA)x+XPYA-XAYP
            # (YP-YA)x+(XA-XP)y+XPYA-XAYP=0
            # P到AB距离记作d,d的平方记作dd
            dd = (((YP - YA) * XB + (XA - XP) * YB + XP * YA - XA * YP) ** 2) / ((YP - YA) ** 2 + (XA - XP) ** 2)
            print('dd ' + str(dd))
            # 线段AB的平方记作ABAB
            ABAB = (XB - XA) ** 2 + (YB - YA) ** 2
            print('ABAB ' + str(ABAB))
            # 线段BP的平方记作BPBP
            BPBP = (XP - XB) ** 2 + (YP - YB) ** 2
            print('BPBP ' + str(BPBP))

            if cosBPA * cosBAP < 0:
                # 小于零，一钝一锐，AP在B的同侧，比两个端点
                print('钝角')
                longer = ABAB if ABAB > BPBP else BPBP
                shorter = BPBP if ABAB > BPBP else ABAB
                print('最大距离平方 ' + str(longer))
                print('最小距离平方 ' + str(shorter))
                if ((R + r) ** 2 >= shorter and shorter >= (R - r) ** 2) or (
                        (R + r) ** 2 >= longer and longer >= (R - r) ** 2):
                    return 1
                else:
                    return -1
            if cosBPA * cosBAP > 0:
                # 两个锐角，比长的那个端点，和垂线段距离
                print('锐角')
                longer = ABAB if ABAB >= BPBP else BPBP
                shorter = dd
                print('最大距离平方 ' + str(longer))
                print('最小距离平方 ' + str(shorter))
                if ((R + r) ** 2 >= shorter and shorter >= (R - r) ** 2) or (
                        (R + r) ** 2 >= longer and longer >= (R - r) ** 2):
                    return 1
                else:
                    return -1
            if cosBPA * cosBAP == 0:
                print('直角')
                longer = ABAB if ABAB > BPBP else BPBP
                shorter = BPBP if ABAB > BPBP else ABAB
                print('最大距离平方 ' + str(longer))
                print('最小距离平方 ' + str(shorter))
                if ((R + r) ** 2 >= shorter and shorter >= (R - r) ** 2) or (
                        (R + r) ** 2 >= longer and longer >= (R - r) ** 2):
                    return 1
                else:
                    return -1

    # 22给定一个列表，该列表中的每个元素要么是个列表，要么是整数。将其变成一个只包含整数的简单列表。
    def flatten(self, nestedList):
        inputStr1 = str(nestedList)
        inputStr2 = ''
        for ch in inputStr1:
            if ch != '[' and ch != ']':
                inputStr2 += ch
            if ch == ' ':
                print('有个空格！！！')
        # 明天问问傻六这个空格咋出来的
        inputStr3 = inputStr2.replace(' ', '')
        inputNums = list(inputStr3.split(','))
        ret = []
        for num in inputNums:
            if len(num) > 0:
                ret.append(int(num))
        return ret


# 24LFU是一个著名的缓存算法对于容量为k的缓存，如果缓存已满，并且需要逐出其中的密钥，
# 则最少使用的密钥将被踢出。实现LFU中的set 和 get


class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None


class LRUCache:
    def __init__(self, len):
        self.headNode = None
        self.len = len

    def getLength(self):
        if self.headNode == None:
            return 0
        else:
            current = self.headNode
            length = 1
            while current.next != None:
                length += 1
                current = current.next
            return length

    def getKeys(self):
        if self.headNode == None:
            return []
        else:
            ret = []
            current = self.headNode
            ret.append(current.key)
            while current.next != None:
                current = current.next
                ret.append(current.key)
            return ret

    def showall(self):
        if self.headNode == None:
            print('None')
        else:
            node = self.headNode
            print(str(node.key) + ': ' + str(node.value), end=', ')
            while node.next != None:
                node = node.next
                print(str(node.key) + ': ' + str(node.value), end=', ')
            print()

    def set(self, k, v):
        node = Node(k, v)
        if self.headNode == None:
            self.headNode = node
        else:
            keys = self.getKeys()

            if k not in keys:

                if self.getLength() < self.len:
                    current = self.headNode
                    while current.next != None:
                        current = current.next
                    current.next = node
                else:
                    current = self.headNode
                    if current.next == None:
                        self.headNode = node
                    else:
                        currentMinus1 = None
                        while current.next!= None:
                            currentMinus1 =current
                            current=current.next
                        else:
                            currentMinus1 .next = node

            elif k in keys:
                current = self.headNode
                if current.key == k:
                    current.value = v
                else:
                    while current.next != None:
                        current = current.next
                        if current.key == k:
                            current.value = v
                            break

            self.showall()

    def get(self, k):
        if self.headNode == None:
            print('*' * 30)
            print(' get -1')
            print('*' * 30)
            return -1
        else:
            keys = self.getKeys()
            if len(keys) == 0:
                print('*' * 30)
                print(' get -1')
                print('*' * 30)
                return -1
            else:
                if k not in keys:
                    print('*' * 30)
                    print(' get -1')
                    print('*' * 30)
                    return -1
                else:
                    if self.headNode.key == k:
                        print('*' * 30)
                        print(' get ' + str(self.headNode.value))
                        print('*' * 30)
                        return self.headNode.value
                    else:
                        ret = None
                        selectedNode = None
                        currentPlus1 = None
                        currentMinus1 = None
                        current = self.headNode
                        if current.key == k:
                            ret = current.value
                        else:
                            while current.next != None:
                                current = current.next
                                if current.key == k:
                                    selectedNode = current
                                    ret = current.value
                                    if current.next == None:
                                        currentPlus1 = None
                                    else:
                                        currentPlus1 = current.next
                                    break
                            current = self.headNode
                            while current.next != None:
                                if current.next == selectedNode:
                                    currentMinus1 = current
                                    break
                                else:
                                    current = current.next

                            temp = self.headNode
                            self.headNode = selectedNode
                            self.headNode.next = temp
                            currentMinus1.next = currentPlus1
                        print('*' * 30)
                        print(' get ' + str(ret))
                        print('*' * 30)
                        return ret


l=LRUCache(3)
l.set(1,10)
l.set(2,20)
l.set(3,30)
l.get(1)
l.showall()
l.set(4,40)
l.get(4)
l.showall()
l.get(3)
l.showall()
l.get(2)
l.showall()
l.get(1)
l.showall()
l.set(5,50)
l.get(1)
l.showall()
l.get(2)
l.showall()
l.get(3)
l.showall()
l.get(4)
l.showall()
l.get(5)
l.showall()





from collections import OrderedDict

# class LRUCache:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = OrderedDict()
#
#     def get(self, key):
#         if key not in self.cache:
#             print(self.cache, end=' ')
#             print('get ' + '-1')
#             return -1
#         value = self.cache.pop(key)
#         self.cache[key] = value
#         print(self.cache, end=' ')
#         print('get ' + str(value))
#         return value
#
#     def set(self, key, value):
#         if key in self.cache:
#             self.cache.pop(key)
#         elif len(self.cache) == self.capacity:
#             self.cache.popitem(last=False)
#         self.cache[key] = value
#         print(self.cache)

# lru = LRUCache(3)
# lru.set(2, 2)
# lru.set(1, 1)
# lru.get(2)
# lru.get(1)
# lru.get(2)
# lru.set(3, 3)
# lru.set(4, 4)
# lru.get(3)
# lru.get(2)
# lru.get(1)
# lru.get(4)
