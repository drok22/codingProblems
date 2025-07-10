OPENING = ["(", "[", "{"]
CLOSING = [")", "]", "}"]


class Solution:
    def isValid(self, s: str) -> bool:
        ''' Uses a last in first out stack to track which parenthesis we need to open/close
        '''
        stack = []

        for c in s:
            if c in OPENING:
                stack.append(c)
            elif c in CLOSING and stack:
                if ((c == ")" and stack[-1] == "(") or
                        (c == "}" and stack[-1] == "{") or
                        (c == "]" and stack[-1] == "[")):
                    stack.pop()
                else:
                    return False
            else:
                return False
        if stack:
            return False
        return True


def main():
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("([])"))


if __name__ == "__main__":
    main()
