import math
x = 0.5
chisl = x**2 + math.sqrt(x + 5)
znam = 2 * x - math.sqrt(abs(math.exp(x) - 2 * math.log(x)))
y = math.exp(-2 * x) * (chisl / znam)
print(f"y({x}) = {y:.5f}\n")