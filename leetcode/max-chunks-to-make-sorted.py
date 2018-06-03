class Solution:
    def maxChunksToSorted(self, arr):
        l = len(arr)
        if l <= 1:
            return 1
        d = {arr[i]: i for i in range(l)}

        i = 0
        chuncks = []
        while i < l:
            chunck = []
            j = max(arr[i], d[i])
            while i <= j:
                chunck.append(arr[i])
                j = max(j, i, d[i])
                i += 1
            chuncks.append(chunck)
        # print(chuncks)
        return len(chuncks)
