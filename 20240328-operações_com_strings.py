# Operações com strings - 28/03/2024 e 04/04/2024

# concatenação:
nome = 'João'
idade = 15
altura = 1.75
print('Meu nome é ' + nome)

# composição de strings

# usando marcadores de %
print('Meu nome é %s' % nome)
print('E tenho %d anos.' % idade)

print('Meu nome é %s, tenho %d anos e %.2f m de altura.' % (nome,idade,altura))

# composição usando o método .format()
print('Meu nome é {:10}, tenho {:03} anos e {:.2f} metros.'.format(nome,idade,altura))

# composição usando f-String
print(f'Meu nome é {nome:10}, tenho {idade:03} anos e {altura:.2f} metros.')


