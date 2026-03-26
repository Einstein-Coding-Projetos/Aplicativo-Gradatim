# Guia de Fluxo de Trabalho (Rotina Diaria)

Este guia e destinado a membros da equipe que **ja passaram pela configuracao inicial**
e estao retornando ao projeto para desenvolver novas funcionalidades.

---

## 1. Inicio: Sincronizar e Subir o Ambiente

Antes de codificar, sincronize seu repositorio local e prepare o ambiente de desenvolvimento.

1. Abra o terminal na pasta **raiz** do projeto (Aplicativo-Oncologico).

2. Puxe as ultimas atualizacoes do repositorio remoto:

`git pull`

3. Configure o backend localmente:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
```

4. Inicie o backend:

`python manage.py runserver`

### Acesso
- API Backend: http://localhost:8000
- Admin Django: http://localhost:8000/admin

---

## 2. Executando o Backend (Django)

O backend roda **localmente**, portanto e necessario:

- Ativar o ambiente virtual antes de rodar comandos Python
- Instalar dependencias a partir de `backend/requirements.txt`
- Garantir que o banco de dados configurado no `.env` esteja acessivel

### Rodar migrations (quando necessario)

Se o pull trouxe alteracoes em models ou migrations:

```bash
cd backend
source .venv/bin/activate
python manage.py makemigrations
python manage.py migrate
```

### Verificar ambiente ativo

```bash
cd backend
source .venv/bin/activate
which python
which pip
python --version
pip --version
```

---

## 3. Executando o Frontend (Expo)

O frontend deve ser executado localmente.

1. Abra um **novo terminal**.

2. Navegue para a pasta frontend:

`cd frontend`

3. Instale dependencias (seguro rodar sempre):

`npm install`

4. Inicie o Expo:

`npx expo start`

Para testes em dispositivo fisico, ajuste a variavel
`EXPO_PUBLIC_API_BASE_URL` no arquivo `frontend/.env`
para o IP da maquina local.

---

# Guia de Fluxo de Trabalho Git (Add, Commit, Push)

Este guia descreve o processo padrao para versionamento e colaboracao usando Git.

---

## Ciclo Diario de Desenvolvimento

### 1. Sincronizar com o Repositorio Remoto

Antes de iniciar qualquer trabalho:

`git pull`

Isso reduz drasticamente conflitos.

---

### 2. Desenvolver

Implemente sua funcionalidade ou correcao normalmente no codigo.

---

### 3. Verificar Alteracoes

Antes de salvar, confira os arquivos modificados:

`git status`

---

### 4. Adicionar Arquivos ao Stage

Para adicionar todas as alteracoes:

`git add .`

Ou apenas arquivos especificos:

`git add caminho/para/o/arquivo`

---

### 5. Criar Commit

Salve suas alteracoes com uma mensagem clara e padronizada:

`git commit -m "tipo: descricao curta do que foi feito"`

---

### 6. Enviar para o Repositorio Remoto

Compartilhe seu trabalho com a equipe:

`git push`

---

## Padrao de Mensagens de Commit

Formato utilizado:

`tipo: o que foi feito`

### Tipos Principais

- feat: nova funcionalidade
  Ex: feat: implementa diario do paciente

- fix: correcao de bug
  Ex: fix: corrige erro ao salvar sintomas

- docs: documentacao
  Ex: docs: atualiza guia de desenvolvimento

- chore: manutencao e configuracoes
  Ex: chore: ajusta setup local do backend

### Tipos Complementares

- refactor: melhoria de codigo sem mudar comportamento
- style: ajustes de formatacao
- test: adicao ou correcao de testes

---

## Observacoes Importantes

- Nunca versionar arquivos `.env`
- Nunca instalar dependencias Python fora do ambiente virtual do backend
- Sempre rodar migrations apos alteracoes em models
- Em caso de erro no backend, validar as variaveis do arquivo `backend/.env`  