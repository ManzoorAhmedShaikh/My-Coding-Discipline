#Problem link: https://leetcode.com/problems/roman-to-integer/description/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        data = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total_sum = 0
        skip = False


        for i in range(len(s) - 1):
            if skip:
                skip = False
                continue

            elif s[i + 1] in ['V', "X"] and s[i] == 'I':
                total_sum += data.get(s[i + 1]) - data.get(s[i])
                skip = True

            elif s[i + 1] in ['L', "C"] and s[i] == 'X':
                total_sum += data.get(s[i + 1]) - data.get(s[i])
                skip = True

            elif s[i + 1] in ['D', "M"] and s[i] == 'C':
                total_sum += data.get(s[i + 1]) - data.get(s[i])
                skip = True

            else:
                total_sum += data.get(s[i])

        if not skip:
                total_sum += data.get(s[-1])

        return total_sum