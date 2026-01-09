# Problem link: https://leetcode.com/problems/valid-palindrome/?envType=problem-list-v2&envId=string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True
        if len(s.strip()) != 0:
            s = "".join([x for x in s.replace(" ","").lower() if x.isalnum()])
            i = 0
            j = -1
            while i < len(s):
                if s[i] != s[j]:
                    result = False
                    break

                i += 1
                j -= 1
        return result