class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

# Step 1: Clean up the data.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 0

# Step 2: Overwrite to mark presence using a marker (n + 1).
        for i in range(n):
            original_val = nums[i] % (n + 1)
            if 1 <= original_val <= n:
                target_idx = original_val - 1
                nums[target_idx] = nums[target_idx] + (n + 1)

# Step 3: Find the first untouched slot.
        for i in range(n):
            if nums[i] < (n + 1):
                return i + 1

# Step 4: If all slots 1 to n were marked.
        return n + 1