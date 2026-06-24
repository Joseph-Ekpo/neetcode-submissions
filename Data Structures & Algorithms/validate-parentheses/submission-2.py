class Solution:
    def isValid(self, s: str) -> bool:
        opened = {"(":")", "{":"}", "[":"]"}
        closed = {")":"(", "}":"{", "]":"["}
        validator = []

        for char in s:
            if char in opened:
                validator.append(opened[char])
            elif char in closed:
                if len(validator) == 0:
                    return False
                elif char != validator.pop():
                    return False
        
        return not validator

