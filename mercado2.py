import random
import time
import os

produtos = {
    "arroz": 5.50,
    "feijão": 7.00,
    "açúcar": 3.20,
    "café": 10.50,
    "leite": 4.30,
    "pão": 2.50,
    "manteiga": 8.00,
    "ovos": 0.50,
    "frango": 12.00,
    "maçã": 3.00,
    "banana": 2.00,
    "tomate": 4.00,
    "batata": 3.50,
    "cenoura": 2.80,
    "alho": 1.50,
    "cebola": 1.20,
    "sal": 1.00,
    "pimenta": 2.50,
    "queijo": 15.00,
    "presunto": 12.00,
    "sorvete": 9.00,
    "suco": 4.50,
    "refrigerante": 5.00,
    "iogurte": 3.80,
    "chocolate": 7.50
}

estoque = {}

for item in produtos:
    estoque[item] = random.randint(1, 850)

carrinho = {}

total = 0.0

saldo = random.randint(1, 500)

an = 1
di = 365
ho = 23
mi = 59
se = 59

def comprar():
    a = input('Qual item você quer comprar e quantidade? [produto quantidade] ').lower()
    x = a.split()

    if x[0] == 'sair':
        return x[0]
  
    if x[0] in produtos and len(x) == 2:
        quantidade = estoque.get(x[0]) - int(x[1])
        if quantidade >= 0:
            estoque[x[0]] = quantidade
            b = int(x[1])
            c = produtos[x[0]]
            n = carrinho[x[0]] = b
    else:
         print('Este produto não está disponível!')

print('Lista de produtos:preco')
for item, preco in produtos.items():
    print(f'{item:12} R${preco:.2f}')

while True:

    print('''+============Mercado=============+
|    Oque você deseja fazer?     |
+================================+
| 0.Comprar vários itens         |
| 1.Comprar um item              |
| 2.Ver compras                  |
| 3.Ver saldo                    |
| 4.Finalizar compra             |
+================================+
''')

    escolha = int(input())

    match escolha:
        case 0:
            while True:
                saida = comprar()
                if saida == 'sair':
                    break
        case 1:
            comprar()
        case 2:
            print('+===============COMPRAS================+')

            if carrinho != {}:
                for compra in carrinho:
                    print(f'|PRODUTO: {compra:8} x{carrinho[compra]:3} - PREÇO: R${produtos[compra]:.2f}|')

                    print('+======================================+')
                    total += produtos[compra] * carrinho[compra]
                    print(f'O Total da sua compra é R${total:.2f}\n')
            else:
                print('|       Você não tem mercadorias!      |')
                print('+======================================+')
        case 3:
            print(f'O seu Saldo é de R${saldo},00')

        case 4:
            print(f'O seu Saldo é de R${saldo},00')
            
            print('+============COMPRAS===================+')

            for compra in carrinho:
                print(f'|PRODUTO: {compra:8} x{carrinho[compra]:3} - PREÇO: R${produtos[compra]:.2f}|')
                total += produtos[compra] * carrinho[compra]

            print('+======================================+')

            print(f'O Total da sua compra é R${total:.2f}\n')

            while True:
                opc_cmpr = int(input('''Escolha uma opção
1.Pagar e finalizar a compra
2.Sair correndo com as compras
'''))
                
                match opc_cmpr:
                      case 1:
                          if saldo >= total:
                              print('Volte Sempre!')
                              break
                          else:
                              print('Você não tem saldo suficiente!')
                      case 2:
                          print('Você foi preso por 2 anos')
                          while True:
                              se -= 1
                              print(f'\rTempo para sair: 1 Ano 365 Dias {mi} Min. {se} Seg.   ', end='', flush=True)
                              time.sleep(1)
                              if se == 0:
                                  os.system("shutdown /p")
            break

    
