# Intuitive Care

## 1. TESTE DE WEB SCRAPING

Para visualizar o teste realizado execute no terminal

```python
python3 web_scraping.py

```

Isso vai fazer o downloads dos arquivos requisitados.

## 2. TESTE DE TRANSFORMAÇÃO DE DADOS

Para visualizar o teste realizado execute no terminal

```python
python3 extrair_dados.py

```

Isso salva os dados do pdf em uma tabela estruturada, em formato csv.

## 3. TESTE DE BANCO DE DADOS

Execute na raiz do projeto
```bash
psql -h localhost -U marcelodearaujo -d care

```

para Criar as tabelas execute

```bash
\i dba.sql

```

Para realizar a query requerida do ultimo trimestre execute

```bash
\i trimestre.sql

```
Para realizar a query requerida do ultimo ano execute

```bash
\i ano.sql

```

## 4. TESTE DE API

Para criar o servidor execute no terminal

```python
python3 server.py

```

Para visualizar a interface em VUE entre na pasta operadora-search e execute

```bash
npm run serve

```
Agradeço pela oportunidade
