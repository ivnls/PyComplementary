import requests

city = input('Digite o nome da cidade: ')
api_key = '420cb4acbd778e8eb675b46b22d5333e'


try:
    req = requests.get(f'https://api.openweathermap.org/data/2.5/find?q={city}&appid={api_key}')
except:
    print('Erro na requisição')

#conv = (k - 273.15)

print(req.headers)    

