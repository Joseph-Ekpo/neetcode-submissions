class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        j, n = 0, len(nums)
        ans = [0] * (2 * n)
        for i in range(2 * n):
            if i >= n:
                j = i - n
                ans[i] = nums[j]
            else:
                ans[i] = nums[j]
                j += 1
        
        return ans
                

        