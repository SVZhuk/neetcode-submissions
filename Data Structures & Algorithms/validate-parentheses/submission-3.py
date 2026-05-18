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
                if len(self.stack) == 0 or letter != brackets[self.stack.pop()]:
                    return False
        
        return True if len(self.stack) == 0 else False