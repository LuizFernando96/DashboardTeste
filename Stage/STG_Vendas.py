import pandas as pd

def selecionando(caminho):
    df = pd.read_excel(
        caminho,
        skiprows=5,
        header=0,
        engine='openpyxl'
    )
    return df

def tratando(df):
    df = df[['Data Venda', 'ID Subcategoria', 'ID Cidade', 'No. Venda', 'Custo Unitário', 'Preço Unitário', 'Quantidade', 'Valor Desconto']]
    df = df.rename(columns={
        'Data Venda': 'Data_Venda', 
        'ID Subcategoria': 'ID_Subcategoria',
        'ID Cidade': 'ID_Cidade', 
        'No. Venda': 'ID', 
        'Custo Unitário': 'Custo_UnitArio', 
        'Preço Unitário': 'Preco_Unitario', 
        'Valor Desconto': 'Valor_Desconto'
        })
    return df

def enviando(df):
    df.to_csv(r'C:\Users\Luiz.Fernando\Teste\Banco\STG_Vendas.csv', index=False)

def main():
    df = selecionando(r'C:\Users\Luiz.Fernando\Teste\Fonte\Vendas.xlsx')
    df = tratando(df)
    enviando(df)
main()
print("Script STG_Vendas executado com sucesso")