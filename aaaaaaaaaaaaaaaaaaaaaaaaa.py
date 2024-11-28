import time

for i in range(10):
    print(f'\rContagem: {i}    ', end='', flush=True)  # Adicionando espaços para limpar a linha
    time.sleep(1)
