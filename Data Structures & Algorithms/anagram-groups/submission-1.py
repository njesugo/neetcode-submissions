class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            sign = [0] * 26

            for letter in word:
                sign[ord(letter) - ord('a')] += 1
            signature = tuple(sign)

            if signature not in result:
                result[signature] = []
            result[signature].append(word)
        
        return list(result.values())