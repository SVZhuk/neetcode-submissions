class Solution:
    def isPalindrome(self, x: int) -> bool:
        inp_str = str(x)
        l = 0
        r = len(inp_str) - 1

        while l < r:
            if inp_str[l] != inp_str[r]:
                return False

            l += 1
            r -= 1

        return True

