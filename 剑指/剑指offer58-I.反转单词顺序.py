"""
你在与一位习惯从右往左阅读的朋友发消息，他发出的文字顺序都与正常相反但单词内容正确，为了和他顺利交流你决定写一个转换程序，把他所发的消息 message 转换为正常语序。

注意：输入字符串 message 中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

 

示例 1：

输入: message = "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: message = "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: message = "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。'
"""

# 思路：将str.split去掉所有的空格，反向输出即可
class Solution:
    def reverseMessage(self, message: str) -> str:
        words = message.split()  # 去除多余空格，分割单词
        return " ".join(words[::-1])  # 反转单词顺序并拼接
            
