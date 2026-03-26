# Gradatim
Aplicativo de Assistencia Psicologica em Tratamentos Oncologicos

Gradatim e uma plataforma mobile voltada ao apoio psicologico de pacientes em tratamento oncologico. O aplicativo oferece um ambiente seguro e empatico para registro diario de sentimentos, acompanhamento de sintomas, acesso a conteudos de apoio baseados em evidencia cientifica, gamificacao para engajamento continuo e solicitacao de sessoes de terapia psicologica.

O projeto foi desenvolvido com foco em seguranca de dados, organizacao de codigo, escalabilidade e colaboracao entre desenvolvedores.

---

## Tecnologias Utilizadas

### Backend
- Django
- Django REST Framework
- PostgreSQL

### Frontend
- React Native
- Expo
- Expo Router

### Infraestrutura de Desenvolvimento
- Docker
- Docker Compose
- Python 3.11+
- Ambiente virtual (`venv`)
- Node.js 20+

---

## Estrutura do Repositorio

/
├── backend/ API Django
│ ├── apponco_api/ Configuracoes do projeto
│ ├── accounts/ Autenticacao e usuarios
│ ├── core/ Funcionalidades centrais
│ ├── manage.py
│ └── requirements.txt
│ ├── requirements.txt
│ └── .env.example
├── frontend/ Aplicativo mobile Expo
├── docker-compose.yml Orquestracao dos containers
├── setup.py Script opcional de setup local
└── README.md

---

## Pre requisitos

- Docker Desktop
- Docker Compose
- Python 3.11 ou superior
- Node.js versao 20 ou superior
- PostgreSQL acessivel localmente ou via `DATABASE_URL`
- Expo Go para testes em dispositivo fisico

---

## Variaveis de Ambiente

### Backend

Criar o arquivo de variaveis de ambiente a partir do modelo:

backend/.env.example
`backend/.env.example`

Copiar o arquivo e renomear para:

backend/.env
`backend/.env`

Preencher o arquivo com as configuracoes locais do Django e do banco de dados.

Importante  
O arquivo .env nunca deve ser versionado.
O arquivo `.env` nunca deve ser versionado.

---

### Frontend

Criar o arquivo de variaveis de ambiente a partir do modelo:

frontend/.env.example
`frontend/.env.example`

Copiar o arquivo e renomear para:

frontend/.env
`frontend/.env`

Este arquivo contem configuracoes publicas como a URL base da API.

---

## Como Rodar o Projeto com Docker
## Como Rodar o Backend sem Docker

### Subir Backend e Banco de Dados
Na pasta `backend`, crie e ative um ambiente virtual:

Na raiz do projeto executar:
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
```

docker compose up --build
Instale as dependencias do backend:

Esse comando inicia:
- Banco de dados PostgreSQL
- API Django
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

### Rodar Migrations

As migrations nao sao executadas automaticamente no startup do container.

Com os containers em execucao, executar:
Aplique migrations e inicie a API Django:

docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py migrate

---
```bash
python manage.py migrate
python manage.py runserver
```

### Criar Superusuario

Opcional, para acesso ao admin do Django:

docker compose exec backend python manage.py createsuperuser

---
```bash
python manage.py createsuperuser
```

### Acessos

- API Backend: http://localhost:8000
- Admin Django: http://localhost:8000/admin

---

## Rodando o Frontend

O frontend Expo deve ser executado fora do Docker para facilitar o desenvolvimento.
O frontend Expo deve ser executado localmente.

Acessar a pasta frontend e executar:

```bash
cd frontend
npm install
npx expo start
```

Para testes em celular fisico, ajustar a variavel EXPO_PUBLIC_API_BASE_URL no arquivo frontend/.env para o IP da maquina local.
Para testes em celular fisico, ajustar a variavel `EXPO_PUBLIC_API_BASE_URL` no arquivo `frontend/.env` para o IP da maquina local.

---

## Padrao de Commits

- feat: nova funcionalidade
- fix: correcao de bug
- docs: documentacao
- chore: manutencao e configuracoes

---

## Observacoes Importantes

- Dados sensiveis de pacientes devem ser tratados com cuidado e nunca registrados em logs
- Arquivos de upload local nao devem ser versionados
- O projeto foi estruturado para futura migracao para ambientes de producao seguros

---

## Licenca

Projeto sob Licenca MIT.