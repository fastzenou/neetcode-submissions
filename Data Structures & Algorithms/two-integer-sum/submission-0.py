class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}
        for x in range(len(nums)):
            tmp = nums[x]
            if target - tmp in history:
                return [history[target-tmp],x]
            else:
                history[tmp] = x