class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
        brackets = {
            "{": "}",
            "[": "]",
            "(": ")",
        }
        for letter in s:
            if letter in ["{", "(", "["]:
                self.stack.append(letter)
            else: 
                if not self.stack or letter != brackets[self.stack.pop()]:
                    return False
        
        return True if not self.stack else False