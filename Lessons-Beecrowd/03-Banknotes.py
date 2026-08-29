# Beecrowd 1018 - Banknotes
#
# Read an integer value representing an amount of money.
#
# Calculate the minimum number of banknotes needed to represent
# this value using the available banknotes:
#
# R$100, R$50, R$20, R$10, R$5, R$2 and R$1.
#
# Input:
#
# The input contains one integer value representing
# the amount of money.
#
# Output:
#
# Print the original value and the minimum number of
# banknotes of each denomination required to represent it.
#
# The output must follow the exact format specified
# in the problem statement.

valor = int(input())
original = valor

notas100 = valor // 100
valor = valor % 100

notas50 = valor // 50
valor = valor % 50

notas20 = valor // 20
valor = valor % 20

notas10 = valor // 10
valor = valor % 10

notas5 = valor // 5
valor = valor % 5

notas2 = valor // 2
valor = valor % 2

notas1 = valor // 1
valor = valor % 1

print(original)
print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$ 50,00")
print(f"{notas20} nota(s) de R$ 20,00")
print(f"{notas10} nota(s) de R$ 10,00")
print(f"{notas5} nota(s) de R$ 5,00")
print(f"{notas2} nota(s) de R$ 2,00")
print(f"{notas1} nota(s) de R$ 1,00")
