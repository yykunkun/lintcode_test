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
        Xab, Yab = XB - XA, YB - YA  # 向量AB坐标
        Xap, Yap = XP - XA, YP - YA  # 向量AP坐标
        Xpa, Ypa = XA - XP, YA - YP  # 向量PA坐标
        Xpb, Ypb = XB - XP, YB - YP  # 向量PB坐标
        cosBAP = Xab * Xap + Yab * Yap
        cosBPA = Xpa * Xpb + Ypa * Ypb
        # 直线AB的方程
        # (XB-XA)y=(YB-YA)x+XBYA-XAYB
        # (YB-YA)x+(XA-XB)y+XBYA-XAYB=0
        # P到AB距离记作d,d的平方记作dd
        dd = (((YB - YA) * XP + (XA - XB) * YP + XB * YA - XA * YB) ** 2) / ((YB - YA) ** 2 + (XA - XB) ** 2)
        # 线段AB的平方记作ABAB
        ABAB = (XB - XA) ** 2 + (YB - YA) ** 2
        print('ABAB '+str(ABAB))
        # 线段BP的平方记作BPBP
        BPBP = (XP - XB) ** 2 + (YP - YB) ** 2
        print('BPBP '+str(BPBP))
        R = rA if rA >= rB else rB
        r = rB if rA >= rB else rA
        print('R= ' + str(R))
        print('r= ' + str(r))
        print('(R+r)平方 ' + str((R + r) ** 2))
        print('(R-r)平方 ' + str((R - r) ** 2))
        if cosBPA * cosBPA < 0:
            # 小于零，一钝一锐，AP在B的同侧，比两个端点
            print('钝角')
            longer = ABAB if ABAB > BPBP else BPBP
            shorter = BPBP if ABAB > BPBP else ABAB
            print('最大距离平方 '+str(longer))
            print('最小距离平方 '+str(shorter))
            if (R + r) ** 2 >= shorter and longer >= (R - r) ** 2:
                return 1
            else:
                return -1
        if cosBPA * cosBPA > 0:
            # 两个锐角，比长的那个端点，和垂线段距离
            print('锐角')
            longer = ABAB if ABAB >= BPBP else BPBP
            shorter = dd
            print('最大距离平方 '+str(longer))
            print('最小距离平方 '+str(shorter))
            if (R + r) ** 2 >= shorter and longer >= (R - r) ** 2:
                return 1
            else:
                return -1
        if cosBPA * cosBPA == 0:
            print('直角')
            longer = ABAB if ABAB > BPBP else BPBP
            shorter = BPBP if ABAB > BPBP else ABAB
            print('最大距离平方 '+str(longer))
            print('最小距离平方 '+str(shorter))
            if (R + r) ** 2 >= shorter and longer >= (R - r) ** 2:
                return 1
            else:
                return -1
