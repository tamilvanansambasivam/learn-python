class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len({x for x in nums}) == len(nums)
