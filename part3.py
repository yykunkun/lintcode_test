class Solution:
    # 21题目将给出两个圆A和B的圆心坐标(x,y)和半径r，现给你一个点P,使圆A圆心沿直线运动至点P。
    # 请问圆A在运动过程中是否会与圆B相交？（运动过程包括起点和终点）
    # 若会相交返回1，否则返回-1。
    # position是个[],里边有8个值
    # 这个题就转化成了，圆心A移动前后，到圆心B的最小距离，是不是大于两个圆半径的和

    def IfIntersect(self, position):
        centerAFormer = [position[0], position[1]]
        rA = position[2]
        centerB = [position[3], position[4]]
        rB = position[5]
        centerALatter = [position[6], position[7]]
