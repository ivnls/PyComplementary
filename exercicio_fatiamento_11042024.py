# Fatiamento de Strings - Exercício - 11/04/2024
# Peça para digitar uma frase e imprima na tela a segunda metade da frase digitada

frase = input('Digite uma frase: ')

tamanho = len(frase)
meio = tamanho // 2  # mesmo que: meio = len(frase) // 2

print(frase[meio: ])  # mesmo que: frase[meio:tamanho]

    
