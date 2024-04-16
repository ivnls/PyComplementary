palavra = input("Digite a palavra à ser fatiada em frases: ")
contador = 1

palavra_dividida = palavra.split()

for plvr in palavra_dividida:
    print("%d° palavra:" % contador)

    print(plvr)
    contador += 1
