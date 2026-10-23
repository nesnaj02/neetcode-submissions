class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        newdict = dict(Counter(nums))
        n = len(nums)
        for key in newdict:
            if newdict[key] > n/2: 
                return key