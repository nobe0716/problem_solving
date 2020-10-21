import math

n = int(input())

number_of_groups = math.factorial(n) // math.factorial(n // 2) ** 2 // 2
counts_per_group = math.factorial(n // 2) // (n // 2)
print(number_of_groups * counts_per_group ** 2)
