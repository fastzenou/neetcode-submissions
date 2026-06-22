class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        y = sorted(s)
        x = sorted(t)
        return x == y