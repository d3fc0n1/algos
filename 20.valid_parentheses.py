class Solution(object):
    def isValid(self, string):
        """
        :type s: str
        :rtype: bool
        """
        if not string:
            return True
        
        if string[0] in ["]", ")", "}"]:
            return False
        
        stack = []
        for s in string:
            if s in ["[", "(", "{"]:
                stack.append(s)
            elif s == "]" and stack and stack[-1] == "[":
                stack.pop()
            elif s == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif s == "}" and stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
        
        return False if stack else True
                