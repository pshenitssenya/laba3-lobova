import math
a = 0.1
b = 0.9
step = 0.05
print("-" * 25)
print(f"{'x':^10} | {'y':^12}")
print("-" * 25)
tecuh = a
while tecuh <= b + step / 2:
    slag1 = (tecuh * math.sin(2 * tecuh)) / math.cos(2 * tecuh)
    slag2 = (tecuh * math.log(tecuh)) / (math.sin(tecuh) + math.cos(tecuh))
    y = slag1 + slag2
    print(f"{tecuh:10.2f} | {y:12.5f}")
    tecuh += step
print("-" * 25 + "\n")