from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from typing import Optional
import uvicorn

# Carregar o CSV com os dados das operadoras
df = pd.read_csv('/Users/marcelodearaujo/Desktop/intuitivecare/Relatorio_cadop.csv', delimiter=';')

# Certifique-se de que todas as colunas sejam convertidas para string
df = df.applymap(str)

# Substituir valores NaN por strings vazias
df = df.fillna('')

# Inicializar o FastAPI
app = FastAPI()

origins = [
    "http://localhost:8080", 
    "http://127.0.0.1:8000",
]

# Adiciona o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

# Modelo Pydantic para os dados da operadora
class Operadora(BaseModel):
    registro_ans: str
    razao_social: str
    nome_fantasia: Optional[str] = None
    modalidade: Optional[str] = None
    logradouro: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    cep: Optional[str] = None
    ddd: Optional[str] = None
    telefone: Optional[str] = None
    fax: Optional[str] = None
    endereco_eletronico: Optional[str] = None
    representante: Optional[str] = None
    cargo_representante: Optional[str] = None
    regiao_comercializacao: Optional[str] = None
    data_registro_ans: Optional[str] = None

@app.get("/operadora/{cnpj}", response_model=Operadora)
async def get_operadora_by_cnpj(cnpj: str):
    """
    Rota para buscar uma operadora pelo CNPJ.
    """
    # Remover espaços extras na entrada (CNPJ da URL)
    cnpj = cnpj.replace(r'\s+', '').strip()
    
    # Filtra as operadoras pelo CNPJ
    operadora = df[df['CNPJ'] == cnpj]
    
    # Verifica se a operadora foi encontrada
    if operadora.empty:
        raise HTTPException(status_code=404, detail="Operadora não encontrada")
    
    # Converte o resultado para o formato esperado
    operadora_data = operadora.iloc[0]
    return Operadora(
        registro_ans=str(operadora_data['Registro_ANS']),
        razao_social=str(operadora_data['Razao_Social']),
        nome_fantasia=str(operadora_data['Nome_Fantasia']),
        modalidade=str(operadora_data['Modalidade']),
        logradouro=str(operadora_data['Logradouro']),
        numero=str(operadora_data['Numero']),
        complemento=str(operadora_data['Complemento']),
        bairro=str(operadora_data['Bairro']),
        cidade=str(operadora_data['Cidade']),
        uf=str(operadora_data['UF']),
        cep=str(operadora_data['CEP']),
        ddd=str(operadora_data['DDD']),
        telefone=str(operadora_data['Telefone']),
        fax=str(operadora_data['Fax']),
        endereco_eletronico=str(operadora_data['Endereco_eletronico']),
        representante=str(operadora_data['Representante']),
        cargo_representante=str(operadora_data['Cargo_Representante']),
        regiao_comercializacao=str(operadora_data['Regiao_de_Comercializacao']),
        data_registro_ans=str(operadora_data['Data_Registro_ANS'])
    )

# Iniciar o servidor quando for executado diretamente
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
