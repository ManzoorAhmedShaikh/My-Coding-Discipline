#Problem link: https://leetcode.com/problems/add-binary/?envType=problem-list-v2&envId=string

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]