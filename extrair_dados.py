import pdfplumber
import pandas as pd
import os
import zipfile

# Caminhos dos arquivos
output_dir = "anexos_ans"
input_pdf = os.path.join(output_dir, "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf")
csv_path = "Rol_de_Procedimentos.csv"
zip_path = "Teste_Marcelo.zip"

# Legenda para substituir as abreviações
legenda = {
    "OD": "Odontológica",
    "AMB": "Ambulatorial"
}

# Função para extrair tabelas do PDF
def extract_tables(pdf_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_tables = page.extract_tables()
            for table in page_tables:
                # Cria um DataFrame para cada tabela extraída
                tables.append(pd.DataFrame(table[1:], columns=table[0]))
    return tables

# Extração dos dados
dados_extraidos = extract_tables(input_pdf)

# Verifica se as tabelas foram extraídas
if not dados_extraidos:
    raise ValueError("Nenhuma tabela foi extraída do PDF. Verifique o formato do arquivo.")

# Concatenar todas as tabelas extraídas em um único DataFrame
df = pd.concat(dados_extraidos, ignore_index=True)

# Ajustar as colunas com base na estrutura do PDF
df.columns = [
    "PROCEDIMENTO", "RN (alteração)", "VIGÊNCIA", "OD", "AMB", "HCO", "HSO",
    "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"
]

# Substituir as abreviações nas colunas OD e AMB
df["OD"] = df["OD"].replace(legenda)
df["AMB"] = df["AMB"].replace(legenda)

# Salvar em CSV
df.to_csv(csv_path, index=False)

# Compactar o CSV em um arquivo ZIP
with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.write(csv_path, os.path.basename(csv_path))

print(f"Transformação concluída! Arquivo gerado: {zip_path}")
