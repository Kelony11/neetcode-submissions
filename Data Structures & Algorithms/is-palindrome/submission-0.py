class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:

            if not s[l].isalnum():
                l += 1
                # print("l++", l)
            elif not s[r].isalnum():
                r -= 1
                # print("r--", r)
            elif s[l].lower() == s[r].lower():
                l += 1
                # print("matched!", "l++", l)
                r -= 1
                # print("matched!", "r--", r)
            else:
                return False

        return True
        