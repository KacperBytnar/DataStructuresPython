class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}        

        if len(s)==len(t):
            for x in range(len(s)):
                if s[x] not in dictS.keys():
                    dictS[s[x]] = 1
                else:
                    dictS[s[x]] += 1

        for char in range(len(t)):
            if t[char] not in dictS.keys() or dictS[t[char]]==0:
                return False
            else:
                dictS[t[char]]-=1
        return True# -*- coding: utf-8 -*-

sol = Solution()

print(sol.isAnagram("rat", "tar"))
print(sol.isAnagram("mad", "mace"))
print(sol.isAnagram("duffy", "fufdy"))

