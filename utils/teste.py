import requests

b = requests.get("https://brasilapi.com.br/api/cep/v1/01153000", timeout=5)
c = requests.get("https://cep.awesomeapi.com.br/json/01153000", timeout=5)

print(b.status_code, c.status_code)
print(f"Brasil API: {b.text}, \nAwesome API: {c.text}")