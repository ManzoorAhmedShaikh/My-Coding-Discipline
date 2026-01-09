#Problem link: https://leetcode.com/problems/length-of-last-word/?envType=problem-list-v2&envId=string

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])