class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for item in nums:
            freq[item] = freq.get(item,0) + 1

        for i in nums:
            if freq[i] > 1:
                return True

        return False 
        