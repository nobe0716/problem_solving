class Solution(object):
    def simplifyPath(self, path):
        path = path.replace("\"", "")
        stack = []
        p = ''
        for ch in path.split('/'):
            if ch == '..':
                if len(stack) > 0:
                    stack.pop()
            elif ch == '.' or ch == '':
                continue
            else:
                stack.append(ch)
        return "/" + "/".join(filter(lambda x: len(x) > 0, stack))