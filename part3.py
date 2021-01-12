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
        print(inputNums)
        ret = []
        for num in inputNums:
            if len(num) > 0:
                ret.append(int(num))
        return ret


# 24LFU是一个著名的缓存算法对于容量为k的缓存，如果缓存已满，并且需要逐出其中的密钥，
# 则最少使用的密钥将被踢出。实现LFU中的set 和 get

class LinkedNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next


class LFUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        pass

    def set(self, key, value):
        pass

    def get(self, key):
        pass


ss = Solution()
inputData = [[], []]
ss.flatten(inputData)
