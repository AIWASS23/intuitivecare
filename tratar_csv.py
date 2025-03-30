import glob
import pandas as pd

def padronizar():
    df = pd.read_csv("/Users/marcelodearaujo/Desktop/intuitivecare/2023/4T2023.csv", delimiter=";", encoding="utf-8")
    df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y").dt.strftime("%Y-%m-%d")
    df.to_csv("demonstracoes_contabeis_formatado.csv", index=False, sep=";", encoding="utf-8")
    
def juntar_csv():
    arquivos = glob.glob("/Users/marcelodearaujo/Desktop/intuitivecare/2023/*.csv")
    dfs = [pd.read_csv(arquivo, delimiter=";", encoding="utf-8") for arquivo in arquivos]
    df_final = pd.concat(dfs, ignore_index=True)
    df_final.to_csv("dados_agrupados.csv", index=False, sep=";", encoding="utf-8")
    
import csv

# Corrigir vírgulas para pontos nos arquivos CSV
def ponto_virgula_csv(input_file, output_file):
    with open("/Users/marcelodearaujo/Desktop/intuitivecare/dados_agrupados.csv", mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        for row in reader:
            row[4] = row[4].replace(',', '.')  # vl_saldo_inicial
            row[5] = row[5].replace(',', '.')  # vl_saldo_final
            writer.writerow(row)

def ponto_virgula_csv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            row[4] = row[4].replace(',', '.')  # Corrigir vl_saldo_inicial
            row[5] = row[5].replace(',', '.')  # Corrigir vl_saldo_final
            writer.writerow(row)
    
if __name__ == "__main__":
    input_file = '/Users/marcelodearaujo/Desktop/intuitivecare/dados_agrupados.csv'
    output_file = '/Users/marcelodearaujo/Desktop/intuitivecare/dados_agrupados_corrigidos.csv'

    ponto_virgula_csv(input_file, output_file)
