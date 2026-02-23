import pandas as pd
from service.cep_service import buscar_uf
from concurrent.futures import ThreadPoolExecutor

def p_xlsx(filepath="file/cep.xlsx"):
    df = pd.read_excel(filepath)
    ceps = df["CEP"].astype(str).str.zfill(8).unique()

    with ThreadPoolExecutor(max_workers=20) as executor:
        resultados = dict(executor.map(buscar_uf, ceps))

    df["UF"] = df["CEP"].astype(str).str.zfill(8).map(resultados)

    df.to_excel(filepath, index=False)
    print("Concluído.")