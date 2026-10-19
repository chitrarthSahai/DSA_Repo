class Solution:
    def isValid(self, s: str) -> bool:
        #Brute force
        #Maintain a map of parenthesis complements.
        # Add all opening parenthesis into the stack.
        # When encountering closing parenthesis, peek at top and see if it's the complement of the current top
        #If no, quickly return false. If true pop the stack
        #At the end check if stack is empty, that means all complements were found. Return true else false

        bracket_map = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []

        for char in s:
            if char in bracket_map.keys():
                stack.append(char)
            else:
                if not stack:
                    return False
                elif bracket_map[stack[-1]] != char:
                    return False
                else:
                    stack.pop()

        if stack:
            return False
        else:
            return True