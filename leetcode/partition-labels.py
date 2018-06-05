class Solution(object):
    def partitionLabels(self, S):
        l = len(S)
        if l == 0:
            return []
        dict_front_back = {}
        for i in range(l):
            e = S[i]
            if e not in dict_front_back:
                dict_front_back[e] = [i, i]
            dict_front_back[e][1] = i
        j = -1
        dict_group_idx = {}
        groups = []
        res = []
        for i in range(l):
            e = S[i]
            if i <= j:
                groups[-1].append(e)
                j = max(j, dict_front_back[e][1])
            elif e not in dict_group_idx:
                res.append(i)
                groups.append([e])
                j = dict_front_back[e][1]
        return list(map(len, groups))
