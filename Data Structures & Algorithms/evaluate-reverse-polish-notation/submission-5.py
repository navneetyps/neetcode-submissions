class Solution:
    def performOperation(self,int1,int2,operation) -> int:
        match operation:
            case "+":
                result = int1 + int2
            case "-":
                result = int2 - int1
            case "*":
                result = int1 * int2
            case "/":
                result = int(int2 / int1)
        return int(result)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+","-","*","/"]
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                int1 = stack[-1]
                stack.pop()
                int2 = stack[-1]
                stack.pop()
                stack.append(self.performOperation(int(int1),int(int2),token))
        return int(stack[-1])

