class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            elif c in [')',']','}']:
                if not stack:
                    return False
                top = stack[-1]
                if top == pairs[c]:
                    stack.pop()
                else:
                    return False
        return False if stack else True