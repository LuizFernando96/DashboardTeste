import pandas as pd

def selecionando(caminho):
    df = pd.read_csv(
        caminho,
        sep=',',
        encoding='utf-8'
    )
    
    return df

def enviando(df):
    df.to_csv(r'C:\Users\Luiz.Fernando\Teste\Banco\Fato_Metas.csv', index=False)

def main():
    df = selecionando(r'C:\Users\Luiz.Fernando\Teste\Banco\STG_Metas.csv')
    print(df.head(20))
    enviando(df)

main()
print("Script Fato_Metas executado com sucesso")