# Beecrowd 1019 - Time Conversion
#
# Read an integer value representing a number of seconds.
#
# Convert this value into hours, minutes and seconds.
#
# Input:
#
# The input contains one integer value representing
# the amount of time in seconds.
#
# Output:
#
# Print the converted time in the format:
#
# hours:minutes:seconds
#
# The values must represent the number of complete hours,
# complete minutes and remaining seconds.

tempo = int(input())

horas = tempo // 3600
tempo = tempo % 3600

minutos = tempo // 60
tempo = tempo % 60

segundos = tempo

print(f"{horas}:{minutos}:{segundos}")
