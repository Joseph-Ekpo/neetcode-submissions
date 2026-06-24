class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        elif len(arr) == 2:
            return [max(arr), -1]

        res = [0] * len(arr)
        max_element = -1
        
        for i in range(len(arr)-1, -1, -1):
            res[i] = max_element
            max_element = max(arr[i], max_element)

        return res
