
# 🏥 API de Gestão de Clínica Médica

[![Django CI](https://github.com/Enge-Olate/apiHealth/actions/workflows/ci.yml/badge.svg)](https://github.com/Enge-Olate/apiHealth/actions/workflows/ci.yml)
Uma API RESTful robusta desenvolvida para gerenciamento de clínicas médicas, permitindo o cadastro de profissionais, pacientes e o agendamento de consultas com validações de conflito de horário.

## 🚀 Tecnologias Utilizadas

O projeto foi construído utilizando as melhores práticas modernas de desenvolvimento Python:

* **Framework:** Django & Django REST Framework (DRF)
* **Banco de Dados:** PostgreSQL
* **Gerenciamento de Dependências:** Poetry
* **Containerização:** Docker & Docker Compose
* **Autenticação:** JWT (JSON Web Token)
* **CI/CD:** GitHub Actions (Pipeline automatizado de testes)

---
## 🧠 Decisões Técnicas

Nesta seção, detalhamos as escolhas arquiteturais e ferramentas adotadas para garantir segurança, escalabilidade e qualidade do código.

### 1. Autenticação e Segurança (JWT)
Optamos por utilizar **JSON Web Tokens (JWT)** via a biblioteca `djangorestframework-simplejwt` para gerenciar a autenticação.

* **Por que JWT?** Diferente da autenticação por sessão (cookies), o JWT é *stateless*. Isso significa que o servidor não precisa armazenar o estado da sessão do usuário, o que facilita a escalabilidade horizontal da aplicação e permite que o back-end sirva múltiplos front-ends (Web, Mobile, IoT) sem acoplamento.
* **Fluxo de Tokens:** Implementamos o padrão de `Access Token` (curta duração) e `Refresh Token` (longa duração). Isso aumenta a segurança, pois caso um token de acesso seja comprometido, ele expira rapidamente, exigindo uma revalidação segura via refresh token.

### 2. Banco de Dados (PostgreSQL)
O **PostgreSQL** foi o banco de dados relacional escolhido para este projeto.

* **Integridade e Robustez:** O Postgres é amplamente reconhecido por sua conformidade com ACID e confiabilidade em ambientes de produção.
* **Suporte a JSONB:** Utilizamos o Postgres também pela sua capacidade eficiente de armazenar e consultar dados não estruturados (JSON Binary). Isso nos permite flexibilidade em tabelas que requerem esquemas dinâmicos sem precisar recorrer a um banco NoSQL separado.
* **Compatibilidade com Docker:** A facilidade de orquestração via Docker Compose garante que o ambiente de desenvolvimento seja idêntico ao de produção, evitando erros de compatibilidade de drivers ou versões SQL.

### 3. Estratégia de Testes (APITestCase)
A qualidade do código é assegurada através de testes automatizados utilizando a classe `APITestCase` do Django REST Framework.

* **Testes de Integração vs. Unitários:** Ao invés de testar apenas métodos isolados dos Models ou Serializers, priorizamos o `APITestCase` para simular o ciclo completo de uma requisição HTTP. Isso garante que a rota, a permissão, a validação do serializer e a persistência no banco estão funcionando em conjunto.
* **O que testamos:**
    * **Happy Path:** Requisições válidas retornando status `200 OK` ou `201 Created`.
    * **Edge Cases:** Tentativas de envio de dados inválidos ou incompletos (`400 Bad Request`).

---


## ⚙️ Arquitetura e Apps

O sistema é modularizado nos seguintes contextos:

1.  **Profissionais:** Gestão de médicos (CRM, Especialidade).
2.  **Pacientes:** Gestão de dados dos pacientes.
3.  **Consultas:** Lógica de agendamento, garantindo integridade entre médico e paciente.

---

## 🛠️ Como Rodar o Projeto

### Opção 1: Via Docker (Recomendado) 🐳

Você não precisa instalar Python ou Postgres localmente. Basta ter o Docker.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/](https://github.com/)[Enge-Olate]/[apiHealth].git
    cd [apiHealth]
    ```

2.  **Suba o ambiente:**
    ```bash
    docker-compose up --build
    ```

3.  **Acesse a API:**
    O servidor estará rodando em: `http://localhost:8000/`

---

### Opção 2: Rodando Manualmente (Local) 🐍

Pré-requisitos: Python 3.12+ e Poetry instalados.

1.  **Instale as dependências:**
    ```bash
    poetry install
    ```

2.  **Ative o ambiente virtual:**
    ```bash
    poetry shell
    ```

3.  **Configure o .env:**
    Crie um arquivo `.env` na raiz baseado no `.env.example` e configure as credenciais do banco.

4.  **Execute as migrações e rode o servidor:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

---

## 🧪 Rodando os Testes

O projeto conta com cobertura de testes automatizados para garantir a integridade dos CRUDs e regras de negócio.

**Via Docker:**
```bash
docker-compose exec django-web python manage.py test

