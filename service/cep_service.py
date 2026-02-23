
# Importa o módulo time para controlar pausas entre tentativas
import time
# Importa requests para fazer requisições HTTP às APIs de CEP
import requests

# Função que busca a UF (estado) correspondente a um CEP consultando múltiplas APIs públicas
def buscar_uf(cep):


    # Lista de URLs de APIs públicas para consulta de CEP
    apis = [
        f"https://brasilapi.com.br/api/cep/v1/{cep}",
        f"https://cep.awesomeapi.com.br/json/{cep}",
        f"https://api.postmon.com.br/v1/cep/{cep}",
    ]

    # Tenta consultar cada API até obter uma resposta válida
    for url in apis:
        try:
            # Faz a requisição HTTP para a API
            r = requests.get(url, timeout=8)

            # Se a resposta for bem-sucedida
            if r.status_code == 200:
                data = r.json()

                # Tenta extrair o campo da UF, que pode ser 'state' ou 'uf' dependendo da API
                uf = (
                    data.get("state")
                    or data.get("uf")
                )

                # Se encontrou a UF, retorna o CEP e a UF
                if uf:
                    return cep, uf

        except:
            # Em caso de erro (timeout, conexão, etc.), espera um pouco antes de tentar a próxima API
            time.sleep(0.3)

    # Se nenhuma API retornar resultado, retorna o CEP e None
    return cep, None