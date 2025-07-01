import pandas as pd

def selecionando(caminho):
    df = pd.read_csv(
        caminho,
        sep=';',
        encoding='utf-8',
        skiprows=2,
        header=0,
        na_values=['NULI', 'NA'],
        usecols=[0, 1, 2], 
    )
    
    return df

def adicionando_continente(df):
    df['Continente'] = pd.NA
    continente_atual = None
    
    for index, row in df.iterrows():
        if 'Continente:' in str(row['ID Localização']):

            continente_atual = str(row['Tipo Localização'])
        else:
            if continente_atual is not None:
                df.at[index, 'Continente'] = continente_atual

    df = df[~df['ID Localização'].astype(str).str.contains('Continente:')]
    
    df.reset_index(drop=True, inplace=True)
    return df

def mantendo_cidade(df):
    df = df[df['Tipo Localização'] == 'City']
    df = df[['ID Localização', 'Continente']]
    df = df.rename(columns={'ID Localização': 'ID_Cidade'})
    return df

def enviando(df):
    df.to_csv(r'C:\Users\Luiz.Fernando\Teste\Banco\STG_Continente.csv', index=False)

def main():
    df = selecionando(r'C:\Users\Luiz.Fernando\Teste\Fonte\Localizacao.csv')
    df = adicionando_continente(df)
    df = mantendo_cidade(df)
    enviando(df)

main()
print("Script STG_Localizacao executado com sucesso")