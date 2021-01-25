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
