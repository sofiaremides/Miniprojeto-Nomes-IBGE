# Web App Nomes

Este projeto é um mini aplicativo desenvolvido em Python utilizando **Streamlit**. Ele consulta uma API do IBGE para exibir dados sobre a frequência de nomes brasileiros ao longo das décadas. Este é o seu primeiro projeto utilizando APIs.

---

## Funcionalidades

1. **Consulta de Nomes:**
   - O usuário pode inserir um nome no campo de texto.
   - O app realiza uma consulta na API do IBGE para buscar dados sobre a popularidade do nome ao longo das décadas.

2. **Exibição de Dados:**
   - Os dados são exibidos em uma tabela com a frequência do nome por década.
   - Um gráfico de linha mostra a evolução da popularidade do nome ao longo do tempo.

3. **Tratamento de Erros:**
   - Caso o nome não seja encontrado na API, uma mensagem de aviso é exibida para o usuário.

---

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:**
  - `requests`: Para realizar chamadas à API do IBGE.
  - `pandas`: Para manipulação de dados.
  - `streamlit`: Para criação da interface web.

---

## Como Executar o Projeto

### Pré-requisitos

- Python 3.9 ou superior.
- Instalar as dependências necessárias:
  ```bash
  pip install requests pandas streamlit
  ```

### Passos para Execução

1. Clone este repositório ou copie os arquivos para o seu ambiente local.
2. Execute o seguinte comando para iniciar o aplicativo:
   ```bash
   streamlit run nome_do_arquivo.py
   ```
3. No navegador, insira o nome que deseja consultar no campo de texto e visualize os resultados.

---

## Organização do Código

### Funções Principais

- **`fazer_request(url, parametro=None):`**
  - Realiza uma requisição GET para a API especificada.
  - Trata erros HTTP e retorna os dados no formato JSON.

- **`pegar_nome_por_decada(nome):`**
  - Chama a função `fazer_request` para buscar dados do nome.
  - Organiza os resultados em um dicionário com as décadas como chave e a frequência como valor.

- **`main():`**
  - Responsável pela interface com o usuário utilizando Streamlit.
  - Exibe os dados retornados pela API em formato de tabela e gráfico.

---

## Referências

- [Documentação da API de Nomes do IBGE](https://servicodados.ibge.gov.br/api/docs/censos/nomes?versao=2)
- [Streamlit](https://streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
