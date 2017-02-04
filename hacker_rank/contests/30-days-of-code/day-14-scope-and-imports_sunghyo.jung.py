    def computeDifference(self):
        v = sorted(self.__elements)
        self.maximumDifference = v[len(v) - 1] - v[0]
