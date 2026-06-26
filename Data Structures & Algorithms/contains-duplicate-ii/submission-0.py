class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
            mp = {} #hash map

            for i in range(len(nums)):
                if nums[i] in mp and i - mp[nums[i]] <= k:
                    return True
                mp[nums[i]] = i # use to add it to mp if not there

            return False