class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# 1 Create a hash map to store the value and index of each element in the array.
# 2 Iterate through the array and compute the complement of the current element, which is target - nums[i].
# 3 Check if the complement exists in the hash map.
# 4 If it does, return the indices of the current element and its complement.
# 5 If no such pair is found, return an empty array.
        idxs = {value: i for i, value in enumerate(nums)}
        for i in range(0, len(nums)):
            res = target - nums[i]
            if res in idxs:
                if i == idxs[res]:
                    continue
                normal_order = idxs[res] > i
                return [i, idxs[res]] if normal_order else [idxs[res], i]
        return []

        

                