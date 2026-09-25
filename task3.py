import math
x = -5.0
b = 5.0
step = 0.5
print("-" * 25)
print(f"{'x':^10} | {'y':^12}")
print("-" * 25)
while x <= b + step / 2:
    if x < 0:
        y = math.sin(x) ** 2
    elif 0 <= x <= 2:
        y = x**2 + 1
    else: 
        y = math.exp(x - 2)
    print(f"{x:10.1f} | {y:12.5f}")
    x += step
print("-" * 25)