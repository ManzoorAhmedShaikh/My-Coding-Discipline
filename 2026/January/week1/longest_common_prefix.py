# Problem link: https://leetcode.com/problems/longest-common-prefix/?envType=problem-list-v2&envId=string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        if len(strs) == 1:
            output = strs[0]

        elif any(strs):
            strs = sorted(strs, key=len, reverse=True)
            first = strs[0]
            for i, first_ch in enumerate(first):
                to_include = True
                for sh in strs[1:]:
                    if i + 1 <= len(sh):
                        if first_ch != sh[i]:
                            to_include = False
                            break
                    else:
                        to_include = False
                        break
                if to_include:
                    output += first_ch
                else:
                    break
        return output