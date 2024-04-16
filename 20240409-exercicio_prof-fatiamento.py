# Exercício - Fatiamento de Strings - 09/04/2024
# Peça para digitar uma frase e imprima a segunda metade da frase.

frase = input('Digite uma frase: ')

meio = len(frase) // 2  # divisão inteira, para encontrar a posição exata

print(frase[meio: ]) # fatiamento do meio até o final (não informa o fim)
