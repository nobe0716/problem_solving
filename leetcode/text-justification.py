from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        groups = []
        group = []
        current_length = 0
        for word in words:
            if not group or current_length + len(word) + 1 <= maxWidth:
                current_length += len(word) + (1 if group else 0)
            else:
                groups.append(group)
                group = []
                current_length = len(word)
            group.append(word)
        groups.append(group)

        def get_left_justified(group: List[str]) -> str:
            r = ' '.join(group)
            return r + ' ' * (maxWidth - len(r))

        def gen_str_with_even(group: List[str]) -> str:
            if len(group) == 1:
                return get_left_justified(group)

            blank_count = maxWidth - sum(len(w) for w in group)
            r = ''
            for i in range(len(group) - 1):
                r += group[i]
                r += ' ' * (blank_count // (len(group) - 1))
                if i < blank_count % (len(group) - 1):
                    r += ' '
            r += group[-1]
            return r

        r = []
        for i in range(len(groups) - 1):
            r.append(gen_str_with_even(groups[i]))
        last_line = ' '.join(groups[-1])
        r.append(last_line + ' ' * (maxWidth - len(last_line)))
        # print(r)
        return r


"""

   "This    is    an",
   "example  of text",
   "justification.  "
"""
s = Solution()
assert s.fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16) == [
    "This    is    an",
    "example  of text",
    "justification.  "
]

assert s.fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16) == [
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
]

assert s.fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20) == [
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "]

assert s.fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6)

[
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything else we do"]
