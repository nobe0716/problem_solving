class Solution(object):
    def decodeString(self, s):
        st = list()
        rn = 0
        d = ""
        for c in s:
            if "0" <= c <= "9":
                rn = rn * 10 + int(c)
            elif c == "[":
                st.append([rn, len(d)])
                rn = 0
            elif c == "]":
                r, rsi = st.pop()
                rs = d[rsi:]
                d += rs * (r - 1)
            else:
                d += c
        while len(st) > 0:
            r, rsi = st.pop()
            rs = d[rsi:]
            d += rs * (r - 1)
        return d