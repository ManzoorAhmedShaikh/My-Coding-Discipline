# Problem link: https://leetcode.com/problems/excel-sheet-column-number/?envType=problem-list-v2&envId=string

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        chrs = {key.upper(): value for value, key in enumerate(start=1, iterable="abcdefghijklmnopqrstuvwxyz")}
        if len(columnTitle) == 1:
            result = chrs[columnTitle]

        else:
            for i, x in enumerate(start=1, iterable=columnTitle):
                result += chrs[x] * (26 ** (len(columnTitle) - i))

        return result