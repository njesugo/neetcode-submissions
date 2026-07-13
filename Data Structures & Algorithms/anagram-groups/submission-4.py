class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            sign = [0] * 26
            for w in word:
                sign[ord(w) - ord('a')] += 1
            sign = tuple(sign)
            if sign not in result:
                result[sign] = []
            result[sign].append(word)
        return list(result.values())