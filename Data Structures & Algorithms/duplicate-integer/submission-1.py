class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=[]
        for i in range(len(nums)):
            if nums[i] not in d:
                d.append(nums[i])
            else:
                return True
                break
        return False    