
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