# QUESTÃO
# Desenvolva um programa que calcule a média das notas dos estudantes,
# arredonde o resultado para duas casas decimais e determine a situação
# do grupo com base nessa média.
#
# O programa deve:
# 1. Armazenar as notas em uma lista.
# 2. Definir uma função para calcular a média usando sum() e len().
# 3. Usar uma função lambda e round() para arredondar a média.
# 4. Classificar o grupo como "Aprovados" se a média for maior ou
#    igual a 7, ou como "Reprovados" caso contrário.
# 5. Exibir as notas, a média arredondada e a situação.
#
# Esta atividade pratica funções definidas com def, funções anônimas
# (lambda), funções prontas do Python e estruturas condicionais.
# A classificação considera a média do grupo, não cada nota individual.

# RESOLUÇÃO

# Lista de notas dos estudantes
notas = [7.5, 8.0, 6.5, 9.0, 7.0]

# Função regular para calcular a média
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Função lambda para arredondar a média para duas casas decimais
arredondar_media = lambda media: round(media, 2)

# Calcular e arredondar a média
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# Verificar a situação do grupo com base na média
situacao = "Aprovados" if media_arredondada >= 7 else "Reprovados"

# Exibir os resultados
print("Notas dos estudantes:", notas)
print("Média arredondada:", media_arredondada)
print("Situação:", situacao)
