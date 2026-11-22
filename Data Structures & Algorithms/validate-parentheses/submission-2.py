class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '{': '}',
            '(': ')',
            '[': ']'
                }
        for ch in s:
            if ch in ['{','(','[']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if pairs[top] == ch:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
                
                