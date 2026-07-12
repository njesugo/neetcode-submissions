class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i, num in enumerate(nums):
            compl = target - num
            if compl in seen and i != seen.get(compl):
                return [seen.get(compl), i]
            seen[num] = i