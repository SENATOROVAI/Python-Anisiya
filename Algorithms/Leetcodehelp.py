#https://leetcode.com/problems/xor-operation-in-an-array/
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0
        for i in range(n):
            xor = xor ^ start
            start+=2
        return xor


#https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/