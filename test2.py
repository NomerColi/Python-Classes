weights = list()

for i in range(4):
    weights.append(float(input(f"Enter weight {i + 1}:\n")))

print("Weights: ", end='')
s = str(["%.1f" % elem for elem in weights])
s = s.replace("'", '')
print(s)

max = 0.0
sum = 0.0
for w in weights:
    if w > max:
        max = w
    sum += w

avg = sum / len(weights)

print(f"\nAverage weight: {avg:0.2f}")
print(f"Max weight: {max:0.2f}")

idx = int(input("\nEnter a list location (1 - 4):\n"))
weight = weights[idx - 1]
print(f"Weight in pounds: {weight:0.2f}")
weight_kilo = weight / 2.2
print(f"Weight in kilograms: {weight_kilo:0.2f}")

weights.sort()

print("\nSorted list: ", end='')
s = str(["%.1f" % elem for elem in weights])
s = s.replace("'", '')
print(s)