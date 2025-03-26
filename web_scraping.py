import requests
from bs4 import BeautifulSoup
import os
import zipfile

# Diretório para salvar os PDFs
output_dir = "anexos_ans"
os.makedirs(output_dir, exist_ok=True)

# URL da página
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"


# Fazendo a requisição para a página
response = requests.get(url)
response.raise_for_status()

# Parseando o conteúdo da página
soup = BeautifulSoup(response.text, 'html.parser')

# Identificando os links dos PDFs (Anexo I e II)
pdf_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    if "anexo" in href.lower() and href.endswith(".pdf"):
        pdf_links.append(href)

# Download dos PDFs
pdf_files = []
for pdf_link in pdf_links:
    pdf_url = pdf_link if pdf_link.startswith("http") else f"https://www.gov.br{pdf_link}"
    pdf_name = pdf_url.split("/")[-1]
    pdf_path = os.path.join(output_dir, pdf_name)

    print(f"Baixando: {pdf_url}")
    pdf_response = requests.get(pdf_url)
    pdf_response.raise_for_status()

    with open(pdf_path, 'wb') as pdf_file:
        pdf_file.write(pdf_response.content)

    pdf_files.append(pdf_path)

# Compactação dos PDFs em um único arquivo ZIP
zip_path = "anexos_ans.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for pdf_file in pdf_files:
        zipf.write(pdf_file, os.path.basename(pdf_file))

print(f"Download e compactação concluídos: {zip_path}")
