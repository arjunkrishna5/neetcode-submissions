class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        # Initialize two pointers at the ends of the array
        l, r = 0, len(height) - 1
        
        # Track the maximum bar height seen so far from both directions
        leftMax, rightMax = height[l], height[r]
        
        # Variable to store the total trapped rain water
        res = 0
        
        # Loop until the two pointers meet
        while l < r:
            # If the left boundary is smaller, the left side is the bottleneck
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            # Otherwise, the right boundary is smaller or equal (right side is the bottleneck)
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                
        return res