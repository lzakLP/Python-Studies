import math

eixos = input().split()
x1 = float(eixos[0])
y1 = float(eixos[1])

eixos = input().split()
x2 = float(eixos[0])
y2 = float(eixos[1])

e_x = x2 - x1
e_y = y2 - y1

resultado1 = e_x ** 2
resultado2 = e_y ** 2

total = resultado1 + resultado2

distancia = math.sqrt(total)

print(f"{distancia:.4f}")
