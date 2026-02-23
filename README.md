# CEP Fetcher

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

## Descrição

Aplicação em Python para consulta de endereços a partir de uma lista de CEPs contidos em um arquivo ´.xlsx´.

O projeto realiza a leitura dos CEPs, consulta uma API pública de endereços (ex: ViaCEP), trata os dados retornados e salva as informações organizadas em planilha.

Objetivo: automatizar consultas em massa de CEP de forma estruturada e reutilizável.

------------------------------------------------------------------------

## Estrutura do projeto

    cep-fetcher/
    │
    ├── file/
    │   └── cep.xlsx
    │
    ├── service/
    │   └── cep_service.py
    │
    ├── utils/
    │
    ├── main.py
    ├── requirements.txt
    ├── README.md
    └── LICENSE

------------------------------------------------------------------------

## Funcionamento interno

1.  O sistema lê os CEPs do arquivo `cep.xlsx`
2.  Para cada CEP:
    -   Faz uma requisição HTTP
    -   Valida a resposta
    -   Estrutura os dados
3.  Organiza tudo de forma tratada
4.  Entrega o resultado pronto

Automação pura.

------------------------------------------------------------------------

## Tecnologias utilizadas

-   Python 3
-   requests
-   pandas
-   openpyxl

------------------------------------------------------------------------

## Como executar

Clone o repositório:

``` bash
git clone https://github.com/cdhnr/cep-fetcher.git
cd cep-fetcher
```

Crie um ambiente virtual:

``` bash
python -m venv venv
source venv/bin/activate  # Linux
```

Instale as dependências:

``` bash
pip install -r requirements.txt
```

Execute:

``` bash
python main.py
```

------------------------------------------------------------------------