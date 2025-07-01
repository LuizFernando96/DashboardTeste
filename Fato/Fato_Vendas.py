import pandas as pd

def selecionando(caminho):
    df = pd.read_csv(
        caminho,
        sep=',',
        encoding='utf-8'
    )
    
    return df

def calcular_valor_final(df):
    df['Valor_Final'] = (df['Preco_Unitario'] * df['Quantidade']) - df['Valor_Desconto']
    return df

def adicionando_continente(df):
    dfContinente = pd.read_csv(
        r'C:\Users\Luiz.Fernando\Teste\Banco\STG_Continente.csv',
        sep=',',
        encoding='utf-8'
    )

    DF = df.merge(
        dfContinente,
        on='ID_Cidade',  
        how='left'  
    )
    return DF

def adicionando_categoria(df):
    dfSC = pd.read_csv(
        r'C:\Users\Luiz.Fernando\Teste\Banco\STG_Subcategoria.csv',
        sep=',',
        encoding='utf-8'
    )

    DF = df.merge(
        dfSC,
        left_on='ID_Subcategoria', 
        right_on='idSubcategoria',  
        how='left'  
    )

    return DF

def enviando(df):
    df.to_csv(r'C:\Users\Luiz.Fernando\Teste\Banco\Fato_Vendas.csv', index=False)

def main():
    df = selecionando(r'C:\Users\Luiz.Fernando\Teste\Banco\STG_Vendas.csv')
    df = calcular_valor_final(df)
    df = adicionando_continente(df)
    df = adicionando_categoria(df)
    
    
    df = df[['ID', 'Data_Venda', 'ID_Subcategoria', 'Categoria', 'Valor_Final', 'Continente']]
    print(df.head(20))
    enviando(df)

main()
print("Script Fato_Vendas executado com sucesso")