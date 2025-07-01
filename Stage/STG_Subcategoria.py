import pandas as pd

def selecionando_dados(caminho):
    df = pd.read_json(caminho)
    return df

def enviando(df):
    df.to_csv(r'C:\Users\Luiz.Fernando\Teste\Banco\STG_Subcategoria.csv', index=False)

def main():
    df = selecionando_dados(r'C:\Users\Luiz.Fernando\Teste\Fonte\Subcategoria.json')
    enviando(df)

main()
print("Script STG_Subcategoria executado com sucesso")