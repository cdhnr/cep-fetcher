import time
import requests
from concurrent.futures import ThreadPoolExecutor

def buscar_uf(cep):

    apis = [
        f"https://brasilapi.com.br/api/cep/v1/{cep}",
        f"https://cep.awesomeapi.com.br/json/{cep}",
        f"https://api.postmon.com.br/v1/cep/{cep}",
    ]

    for url in apis:
        try:
            r = requests.get(url, timeout=8)

            if r.status_code == 200:
                data = r.json()

                uf = (
                    data.get("state")
                    or data.get("uf")
                )

                if uf:
                    return cep, uf

        except:
            time.sleep(0.3)

    return cep, None