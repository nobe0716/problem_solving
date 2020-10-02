import sys
from typing import List, Tuple

sys.setrecursionlimit(5000)


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        def remove_comment(line: str) -> Tuple[bool, str]:
            sl_pos = line.index('//') if '//' in line else float('inf')
            ml_pos = line.index('/*') if '/*' in line else float('inf')
            if sl_pos < ml_pos:
                return False, line[:sl_pos]
            elif ml_pos < sl_pos:
                rest = line[ml_pos + 2:]
                if '*/' in rest:
                    comment_opened, buffer = remove_comment(rest[rest.index('*/') + 2:])
                    return comment_opened, line[:ml_pos] + buffer
                else:
                    return True, line[:ml_pos]
            else:
                return False, line

        in_comment_block = False
        buffer = ''
        res = []

        for line in source:
            if in_comment_block:
                if '*/' not in line:
                    continue
                else:
                    has_comment, token = remove_comment(line[line.index('*/') + 2:])
                    if not has_comment:
                        in_comment_block = False
                        if buffer + token:
                            res.append(buffer + token)
            else:
                comment_opened, token = remove_comment(line)
                if comment_opened:
                    in_comment_block = True
                    buffer = token
                elif token:
                    res.append(token)
        return res


s = Solution()
assert s.removeComments(
    source=["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test",
            "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]) \
       == ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;",
           "}"]
assert s.removeComments(["a/*comment", "line", "more_comment*/b"]) == ['ab']
assert s.removeComments(["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]) \
       == ["struct Node{", "    ", "    int size;", "    int val;", "};"]
