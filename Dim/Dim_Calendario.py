import pandas as pd
from datetime import datetime

def obter_datas_min_max_csv():
    caminho_metas = r'C:\Users\Luiz.Fernando\Teste\Banco\STG_Metas.csv'
    caminho_vendas = r'C:\Users\Luiz.Fernando\Teste\Banco\STG_Vendas.csv'
    
    datas_min = []
    datas_max = []

    df_metas = pd.read_csv(caminho_metas)
    if 'Ano' in df_metas.columns:
        anos_metas = df_metas['Ano'].dropna().astype(int)
        if not anos_metas.empty:
            min_ano = min(anos_metas)
            max_ano = max(anos_metas)
            datas_min.append(datetime(min_ano, 1, 1)) 
            datas_max.append(datetime(max_ano, 12, 31)) 

    df_vendas = pd.read_csv(caminho_vendas)
    if 'Data_Venda' in df_vendas.columns:
        df_vendas['Data_Venda'] = pd.to_datetime(df_vendas['Data_Venda'], format='%Y-%m-%d')
        datas_vendas = df_vendas['Data_Venda'].dropna()
        if not datas_vendas.empty:
            datas_min.append(datas_vendas.min())
            datas_max.append(datas_vendas.max())

    data_min_global = min(datas_min)
    data_max_global = max(datas_max)

    return data_min_global, data_max_global

def criar_dim_calendario(data_min, data_max):
    """Cria o DataFrame dimCalendario."""
    print("criar_dim_calendario(data_min, data_max)")
    datas = pd.date_range(data_min, data_max)
    df_calendario = pd.DataFrame(datas, columns=["data"])
    df_calendario["Ano"] = df_calendario["data"].dt.year
    df_calendario["Mes"] = df_calendario["data"].dt.month_name()
    df_calendario["NumeroMes"] = df_calendario["data"].dt.month
    df_calendario["Dia"] = df_calendario["data"].dt.day
    df_calendario["AnoMes"] = df_calendario["Ano"].astype(str) + df_calendario["NumeroMes"].astype(str).str.zfill(2)
    df_calendario["AnoMesSlash"] = df_calendario["Ano"].astype(str) + "/" + df_calendario["NumeroMes"].astype(str).str.zfill(2)

    # Mapear nomes dos meses para português
    meses_pt = {
        "January": "Janeiro",
        "February": "Fevereiro",
        "March": "Março",
        "April": "Abril",
        "May": "Maio",
        "June": "Junho",
        "July": "Julho",
        "August": "Agosto",
        "September": "Setembro",
        "October": "Outubro",
        "November": "Novembro",
        "December": "Dezembro",
    }
    df_calendario["Mes"] = df_calendario["Mes"].map(meses_pt)
    print(f"df_calendario:\n{df_calendario}")
    return df_calendario

def enviando(df):
    df.to_csv(r'C:\Users\Luiz.Fernando\Teste\Banco\Dim_Calendario.csv', index=False)
    
def main():
    data_min, data_max = obter_datas_min_max_csv()
    df_calendario = criar_dim_calendario(data_min, data_max)
    enviando(df_calendario)

main()