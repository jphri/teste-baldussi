# Teste Baldussi

Software feito para o teste da Baldussi.

## Objetivo

Construir uma aplicação web que:

1. **Consuma** uma **API simulada** de chamadas telefônicas: [API](http://217.196.61.183/calls), [Swagger](http://217.196.61.183:8080/docs)
2. **Cadastre usuários** via CRUD (com autenticação);
3. **Armazene** usuários e chamadas em um **banco de dados (relacional ou não)**;
4. **Exiba** os dados em um **dashboard React** (login + dashboard).

## Entregáveis

- Repositório com `README.md` .
- `docker-compose.yml` contendo: `db` , `api` (backend), `web` (frontend).
- Coleção do **Postman ou Swagger** endpoints do backend .
- Pelo menos **5 testes** unitários/integração no backend (autenticação, CRUD de usuários, ingestão, métricas).

## Backend

- **Auth**
- **Usuários (admin)**
- **Chamadas**
- **Métricas**

## Frontend

- **Login** (email/senha)
- **Dashboard**
    - KPIs: Total, Atendidas, **ASR (taxa de atendimento)**, **ACD (Distribuição Automática de Chamadas)**
    - Gráfico de série temporal (por hora/dia) do total de chamadas
    - **Tabela** com dados das chamadas (`período`, `destino`, `sip_code` …)

