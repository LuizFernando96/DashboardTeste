import pandas as pd

def selecionando(caminho):
    todas_abas = pd.read_excel(caminho, sheet_name=None, header=None)
    
    return todas_abas

def tratando(todas_abas):
    dfs_processados = []
    
    for nome_aba, df_aba in todas_abas.items():
        ano = nome_aba
        
        df_aba = df_aba.drop(0)
        
        df_aba.columns = df_aba.iloc[0]
        df_aba = df_aba.drop(1)
        
        df_aba = df_aba.rename(columns={df_aba.columns[0]: 'Categoria'})
        
        df_melted = pd.melt(
            df_aba,
            id_vars=['Categoria'],
            var_name='Continente',
            value_name='Meta'
        )
        
        df_melted['Ano'] = ano
        
        df_melted = df_melted[df_melted['Categoria'] != 'Total']
        
        dfs_processados.append(df_melted)
    
    df_final = pd.concat(dfs_processados, ignore_index=True)
    
    return df_final

def enviando(df):
    df.to_csv(r'C:\Users\Luiz.Fernando\Teste\Banco\STG_Metas.csv', index=False)

def main():
    todas_abas = selecionando(r'C:\Users\Luiz.Fernando\Teste\Fonte\Metas.xlsx')
    df = tratando(todas_abas)
    enviando(df)

main()
print("Script STG_Metas executado com sucesso")