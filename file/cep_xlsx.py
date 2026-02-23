# Importa a biblioteca pandas para manipulação de dados em planilhas
import pandas as pd
# Importa a função que busca a UF (estado) a partir do CEP
from service.cep_service import buscar_uf
# Importa o executor para processamento paralelo
from concurrent.futures import ThreadPoolExecutor

def p_xlsx(filepath="file/cep.xlsx"):
    # Lê o arquivo Excel com os CEPs
    df = pd.read_excel(filepath)
    # Extrai a coluna de CEPs, garantindo que todos tenham 8 dígitos (com zero à esquerda)
    ceps = df["CEP"].astype(str).str.zfill(8).unique()

    # Executa a busca da UF para cada CEP em paralelo, acelerando o processamento
    with ThreadPoolExecutor(max_workers=20) as executor:
        # Aplica a função buscar_uf para cada CEP e armazena os resultados em um dicionário
        resultados = dict(executor.map(buscar_uf, ceps))

    # Cria/atualiza a coluna "UF" no DataFrame com base nos resultados obtidos
    df["UF"] = df["CEP"].astype(str).str.zfill(8).map(resultados)

    # Salva o DataFrame atualizado de volta no arquivo Excel
    df.to_excel(filepath, index=False)
    print("Concluído.")