CREATE TABLE demonstracoes_contabeis (
    data DATE,
    reg_ans VARCHAR(10),
    cd_conta_contabil VARCHAR(10),
    descricao TEXT,
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL(15,2)
);

CREATE TABLE operadoras (
    registro_ans VARCHAR(10) PRIMARY KEY,
    cnpj VARCHAR(14) NOT NULL,
    razao_social TEXT NOT NULL,
    nome_fantasia TEXT,
    modalidade TEXT NOT NULL,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf VARCHAR(2),
    cep VARCHAR(8),
    ddd VARCHAR(3),
    telefone VARCHAR(20),
    fax VARCHAR(15),
    endereco_eletronico TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_comercializacao INT,
    data_registro_ans DATE
);

COPY operadoras
FROM '/Users/marcelodearaujo/Desktop/intuitivecare/Relatorio_cadop.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';


COPY demonstracoes_contabeis
FROM '/Users/marcelodearaujo/Desktop/intuitivecare/dados_agrupados_corrigidos.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';