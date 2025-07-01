import pandas as pd

def selecionando(caminho):
    df = pd.read_csv(
        caminho,
        sep=',',
        encoding='utf-8',
        usecols=[0,1]
    )
    
    return df

def enviando(df):
    df.to_csv(r'C:\Users\Luiz.Fernando\Teste\Banco\Dim_Subcategoria.csv', index=False)

def main():
    df = selecionando(r'C:\Users\Luiz.Fernando\Teste\Banco\STG_Subcategoria.csv')
    df = df.drop_duplicates()
    print(df.head(20))
    enviando(df)

main()
print("Script Dim_Subcategoria executado com sucesso")