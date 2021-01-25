# 23描述给出一个字符c，你需要判断它是不是一个数字字符或者字母字符。
# 如果是，返回true，如果不是返回false。
# 23题是出错了么？？？so easy
class Solution:
    """
    @param c: A character.
    @return: The character is alphanumeric or not.
    """

    def isAlphanumeric(self, c):
        try:
            inputCharacter = str(c)
            if inputCharacter.isdigit() or inputCharacter.isalpha():
                return True
            else:
                return False
        except:
            return False

    # 25输入一个正整数N， 你需要按如下方式返回一个字符串列表。
    def printX(self, n):
        ret = []
        if n == 0:
            return ret
        else:
            for i in range(n):
                tmp=''
                for j in range(n):
                    if j==i or j==n-i-1:
                        tmp+='X'
                    else:
                        tmp+=' '
                ret.append(tmp)
            return ret


ss = Solution()
print(ss.printX(1))
