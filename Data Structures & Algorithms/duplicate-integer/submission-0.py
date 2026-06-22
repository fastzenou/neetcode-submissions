class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp = set(nums)
        return len(tmp) < len(nums)