# memore O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

sol = Solution()

print(sol.isAnagram("rat", "tar"))
print(sol.isAnagram("mad", "mace"))
print(sol.isAnagram("duffy", "fufdy"))

