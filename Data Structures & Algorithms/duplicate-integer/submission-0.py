class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            hashset.add(n)
            if n in hashset:
                return True 
            else: 
                return False 
         

