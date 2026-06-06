class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums)
        
        # Line 2: Extract the top 'k' most frequent pairs
        top_pairs = frequency_map.most_common(k)
        
        # Line 3: Prepare an empty list to hold just the numbers
        result = []
        
        # Line 4: Loop through the pairs to separate numbers from their counts
        for num, count in top_pairs:
            result.append(num)
            
        return result