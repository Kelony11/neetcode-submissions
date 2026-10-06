class Solution:
    def isValid(self, s: str) -> bool:

        pairs = { ")": "(", "}": "{", "]" : "[" }

        stack = []

        for c in s:
            print("c", c)
            if c not in pairs:
                stack.append(c) # opening bracket

            elif not stack or stack[-1] != pairs[c]:
                return False
            else:
                stack.pop() # match

            print("stack", stack)

        return not stack
        