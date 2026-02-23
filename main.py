
# Importa a função responsável por processar o arquivo Excel de CEPs
from file.cep_xlsx import p_xlsx


# Ponto de entrada do script
if __name__ == "__main__":
    # Chama a função para processar o arquivo de CEPs localizado em file/cep.xlsx
    p_xlsx("file/cep.xlsx")