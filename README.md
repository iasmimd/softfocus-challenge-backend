# Visão geral do projeto:

### O projeto Proagro foi construído para realizar o gerenciamento de comunicações de perda, realizadas por analistas do Proagro, a fim de exonerar agricultores rurais de obrigações fiscais, caso algum evento tenha afetado o período de colheita.

---

Principais tecnologias utilizadas:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [GeoPy](https://pypi.org/project/geopy/)
- [Swagger](https://swagger.io/)

## URL base da aplicação:

https://api-proagro.herokuapp.com/api/

# Documentação da API:

## A API foi separada em duas models, **analista** e **registro de perda**.

## > **Analista**

| Campo    | Tipo   | Descrição                  |
| -------- | ------ | -------------------------- |
| username | string | O nome de usuário analista |
| email    | string | Email do analista          |
| password | string | Senha de acesso ao sistema |

### Endpoints

| Método | Rota      | Descrição                    |
| ------ | --------- | ---------------------------- |
| POST   | analysts/ | Criação de um analista       |
| POST   | login/    | Logar um analista no sistema |

---

### `/analysts/`

### Exemplo de Request:

```
POST /analysts/
Content-type: application/json
```

### Corpo da Requisição:

```json
{
  "username": "iasmim",
  "email": "iasmim@gmail.com",
  "password": "senhaforte"
}
```

### Exemplo de Response:

```
201 Created
```

```json
{
  "username": "iasmim",
  "email": "iasmim@gmail.com"
}
```

### `/login/`

### Exemplo de Request:

```
POST /login/
Content-type: application/json
```

### Corpo da Requisição:

```json
{
  "username": "iasmim",
  "password": "senhaforte"
}
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "token": "9e097cd49c21af22a48f0ceacacdfd8720fe1979",
  "user_id": "c2e16b3e-f3cf-4b89-bf65-b3aa3737571d"
}
```

---

## > **Registro de perda**

| Campo        | Tipo   | Descrição                            |
| ------------ | ------ | ------------------------------------ |
| farmer_name  | string | Nome do agricultor                   |
| farmer_email | string | Email do agricultor                  |
| farmer_cpf   | string | CPF do agricultor                    |
| latitude     | number | Latitude em que se localiza a terra  |
| longitude    | number | Longitude em que se localiza a terra |
| tillage_type | string | Tipo de lavoura                      |
| harvest_date | date   | Data do evento que ocasionou a perda |
| cause        | string | Causa do evento ocorrido             |

---

### `/registrations/`

### Exemplo de Request:

```
GET /registrations/
Content-type: application/json
```

### Corpo da Requisição:

```json
Vazio
```

### Exemplo de Response:

```
200 OK
```

```json
[
  {
    "id": "43a11de9-59a4-463c-9074-c84293e6d28f",
    "farmer_name": "Maria da Silva",
    "farmer_email": "maria@email.com",
    "latitude": "52.509669",
    "longitude": "13.376294",
    "address": "Steinecke, Potsdamer Platz, Tiergarten, Mitte, Berlin, 10785, Deutschland",
    "farmer_cpf": "482.553.078-85",
    "tillage_type": "Café",
    "harvest_date": "2022-07-01",
    "cause": "Raio",
    "last_modified": "2022-09-05",
    "analyst_id": "c2e16b3e-f3cf-4b89-bf65-b3aa3737571d"
  },
  {
    "id": "6f42461b-4cd1-4072-ba9d-372b43a6d639",
    "farmer_name": "José da Silva",
    "farmer_email": "jose@email.com",
    "latitude": -23.9618,
    "longitude": -46.3322,
    "address": "Conversão Rua Doutor Luís Suplicy, Gonzaga, Santos, Região Imediata de Santos, Região Metropolitana da Baixada Santista, Região Geográfica Intermediária de São Paulo, São Paulo, Região Sudeste, 11065-500, Brasil",
    "farmer_cpf": "482.553.078-85",
    "tillage_type": "Café",
    "harvest_date": "2022-07-01",
    "cause": "Vendaval",
    "last_modified": "2022-09-06",
    "analyst_id": "94d985f5-9daa-4a47-9042-85a26f38bbeb"
  }
]
```

### `/registrations/analyst_id/`

### Exemplo de Request:

```
POST /registrations/94d985f5-9daa-4a47-9042-85a26f38bbeb/
Content-type: application/json
```

### Corpo da Requisição:

```json
{
  "farmer_name": "José da Silva",
  "farmer_email": "josesilva@gmail.com",
  "farmer_cpf": "487.423.241-75",
  "latitude": -23.9618,
  "longitude": -46.3322,
  "tillage_type": "Café",
  "harvest_date": "2022-07-01",
  "cause": "Vendaval"
}
```

### Exemplo de Response:

```
201 Created
```

```json
{
  "id": "6f42461b-4cd1-4072-ba9d-372b43a6d639",
  "farmer_name": "José da Silva",
  "farmer_email": "jose@email.com",
  "latitude": -23.9618,
  "longitude": -46.3322,
  "address": "Conversão Rua Doutor Luís Suplicy, Gonzaga, Santos, Região Imediata de Santos, Região Metropolitana da Baixada Santista, Região Geográfica Intermediária de São Paulo, São Paulo, Região Sudeste, 11065-500, Brasil",
  "farmer_cpf": "482.553.078-85",
  "tillage_type": "Café",
  "harvest_date": "2022-07-01",
  "cause": "Vendaval",
  "last_modified": "2022-09-06",
  "analyst_id": "94d985f5-9daa-4a47-9042-85a26f38bbeb"
}
```

### `/registrations/id/`

### Exemplo de Request:

```
PATCH /registrations/6f42461b-4cd1-4072-ba9d-372b43a6d639/
Content-type: application/json
```

### Corpo da Requisição:

```json
{
  "farmer_email": "josepatch@gmail.com",
  "tillage_type": "Café PATCH"
}
```

### Exemplo de Response:

```
200 OK
```

```json
{
  "id": "6f42461b-4cd1-4072-ba9d-372b43a6d639",
  "farmer_name": "José da Silva",
  "farmer_email": "josepatch@gmail.com",
  "latitude": "-23.961800",
  "longitude": "-46.332200",
  "address": "Conversão Rua Doutor Luís Suplicy, Gonzaga, Santos, Região Imediata de Santos, Região Metropolitana da Baixada Santista, Região Geográfica Intermediária de São Paulo, São Paulo, Região Sudeste, 11065-500, Brasil",
  "farmer_cpf": "482.553.078-85",
  "tillage_type": "Café PATCH",
  "harvest_date": "2022-07-01",
  "cause": "Vendaval",
  "last_modified": "2022-09-06",
  "analyst_id": "94d985f5-9daa-4a47-9042-85a26f38bbeb"
}
```

### `/registrations/id/`

### Exemplo de Request:

```
DELETE /registrations/6f42461b-4cd1-4072-ba9d-372b43a6d639/
Content-type: application/json
```

### Corpo da Requisição:

```json
Vazio
```

### Exemplo de Response:

```
204 No Content
```
---
## > **Swagger**
### `/schema/swagger-ui/`
---

# Instruções para rodar localmente:

### Crie o ambiente virtual
```
python -m venv venv
```
### Ative o venv
```bash
# linux:

source venv/bin/activate

```

### Instale as dependências
```
pip install -r requirements.txt
```
### Execute as migrações
```
./manage.py migrate
```
