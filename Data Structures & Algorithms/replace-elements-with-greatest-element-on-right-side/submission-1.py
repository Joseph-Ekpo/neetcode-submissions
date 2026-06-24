class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        elif len(arr) == 2:
            return [max(arr), -1]

        greatest = max(arr)

        for i in range(len(arr)):
            if arr[i] < greatest:
                arr[i] = greatest
            elif arr[i] == greatest:
                if i+1 > len(arr) - 1:
                    arr[i] = -1
                else:
                    greatest = max(arr[i+1:])
                    arr[i] = greatest
        return arr
