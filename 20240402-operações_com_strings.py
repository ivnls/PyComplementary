# Operações com Strings - 02/04/2024 e 09/04/2024
nome = "Henrique Sant'Anna"
idade = 42
altura = 1.85

# Concatenação:
print("Me chamo " + nome + ".")

# Composição (com marcador de %):
print("Me chamo %s." % nome) # marcador %s, usado para string

print("Tenho %d anos." % idade) # marcador %d, usado para digitos numéricos

print("E tenho %.2f metros de altura." % altura) # %f, usado para números float

# quando temos mais de um marcador, as variáveis vão entre () e separadas por ,
print("Sou %s, tenho %d anos e %.2f m de altura." % (nome,idade,altura) )

# Composição com o método .format()
print("Sou {:20}, tenho {:03} anos e {:.2f} m de altura.".format(nome,idade,altura) )

# Composição com f-String
print(f"Sou {nome:20}, tenho {idade:03} anos e {altura:.2f} m de altura.")

