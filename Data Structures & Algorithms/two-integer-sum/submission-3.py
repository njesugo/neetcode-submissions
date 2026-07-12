class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
            else:
                if nums[i] + nums[i] == target:
                    j = seen.get(nums[i],0)
                    return [j, i]

        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in seen and i != seen.get(compl):
                return [i, seen.get(compl)]