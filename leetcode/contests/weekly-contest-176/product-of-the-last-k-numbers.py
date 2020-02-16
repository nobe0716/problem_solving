class ProductOfNumbers:

    def __init__(self):
        self.elems = []
        self.products = [1]
        self.last_product = 1
        self.zero_distance = 1

    def add(self, num: int) -> None:
        self.elems.append(num)
        if num == 0:
            self.last_product = 1
            self.products.append(1)
            self.zero_distance = 1
        else:
            self.last_product *= num
            self.products.append(self.last_product)
            self.zero_distance += 1

    def getProduct(self, k: int) -> int:
        if k >= self.zero_distance:
            return 0
        return self.last_product // self.products[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# ["ProductOfNumbers","add","getProduct","getProduct","getProduct","add","add","add"]
# [[],[1],[1],[1],[1],[7],[6],[7]]
p = ProductOfNumbers()
r = [
    p.add(1),
    p.getProduct(1),
    p.getProduct(1),
    p.getProduct(1),
    p.add(7),
    p.add(6),
    p.add(7)]
print(r)
