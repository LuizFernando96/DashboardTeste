import pandas as pd

def selecionando(caminho):
    df = pd.read_csv(
        caminho,
        sep=',',
        encoding='utf-8',
        usecols=[1]
    )
    
    return df

def enviando(df):
    df.to_csv(r'C:\Users\Luiz.Fernando\Teste\Banco\Dim_Continente.csv', index=False)

def main():
    df = selecionando(r'C:\Users\Luiz.Fernando\Teste\Banco\STG_Continente.csv')
    df = df.drop_duplicates()
    enviando(df)

main()
print("Script Dim_Continente executado com sucesso")