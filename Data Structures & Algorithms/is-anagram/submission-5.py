class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and all(s.count(i) == t.count(i) for i in s)