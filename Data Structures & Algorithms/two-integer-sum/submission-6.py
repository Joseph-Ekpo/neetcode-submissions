class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idxs = {value: i for i, value in enumerate(nums)}
        for i in range(0, len(nums)):
            res = target - nums[i]
            if res in idxs:
                if i == idxs[res]:
                    continue
                normal_order = idxs[res] > i
                return [i, idxs[res]] if normal_order else [idxs[res], i]
        return []

        

                