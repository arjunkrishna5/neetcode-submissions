class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            #if already sorted 
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            #for rotated array
            m = (l + r) // 2
            res = min(res, nums[m])
            #if val ar mid>left portion , set left pntr to m +1 (search right )
            if nums[m] >= nums[l]: 
                l = m + 1
            else:
                r = m - 1
        return res