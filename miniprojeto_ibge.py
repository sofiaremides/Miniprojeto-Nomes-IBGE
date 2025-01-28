import requests
from pprint import pprint
import streamlit as st
import pandas as pd

def fazer_request(url, parametro=None):
    resposta = requests.get(url, params=parametro)

    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f'ERRO no request: {e}')
        resultado = None
    else:
        resultado = resposta.json()

    return resultado

def pegar_nome_por_decada(nome):
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
    dados_decadas = fazer_request(url=url)

    if not dados_decadas:
        return {}

    print(dados_decadas)

    dict_decada = {}
    
    for dados in dados_decadas[0]['res']:
        decada = dados['periodo']
        quantidade = dados['frequencia']
        dict_decada[decada] = quantidade
    
    return dict_decada

def main():
    st.title('Web App Nomes')
    st.write('Dados do IBGE')

    nome = st.text_input('Consulte  um nome:')

    if not nome:
        st.stop()

    dict_decada = pegar_nome_por_decada(nome)

    if not dict_decada:
        st.warning(f'Nenhum dado encontrado para o nome {nome}')

    df = pd.DataFrame.from_dict(dict_decada, orient='index')

    col1, col2 = st.columns([0.3, 0.7])

    with col1:
        st.write('Frequência do nome por década')
        st.dataframe(df)
    with col2:
        st.write('Evolução durante os anos')
        st.line_chart(df)


if __name__ == '__main__':
    main()
