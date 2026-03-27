# .env.production
EXPO_PUBLIC_API_URL=https://Aplicativo-Oncologico-8.onrender.com
EXPO_PUBLIC_ENV=production
```

### 3️⃣ Deployment Options

#### Opção A: Vercel (Backend Django)
```bash
# 1. Criar vercel.json
# 2. Conectar repositório no Vercel
# 3. Adicionar variáveis de ambiente
# 4. Deploy automático
```

#### Opção B: Heroku (Backend Django)
```bash
heroku create seu-app-name
heroku config:set DATABASE_URL=postgresql://...
git push heroku main
```

#### Opção C: DigitalOcean/VPS
```bash
# Mais controle, requer mais configuração
# Configure o servidor com Python 3.11+, venv e Gunicorn para consistencia
```

#### Opção D: Render.com (Recomendado - Gratuito)
```bash
# Similar ao Heroku, gratuito e fácil
```

### 4️⃣ CI/CD (GitHub Actions)

Criar `.github/workflows/deploy.yml`:
```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run migrations
        run: |
          cd backend
          pip install -r requirements.txt
          python manage.py migrate
      
      - name: Deploy to Heroku
        run: git push heroku main
        env:
          HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
```

### 5️⃣ Checklist Final

**Backend:**
- [ ] `DEBUG=False` em produção
- [ ] `SECRET_KEY` aleatório (não comitar!)
- [ ] `ALLOWED_HOSTS` configurado
- [ ] CORS habilitado apenas para seu domínio
- [ ] Variáveis de ambiente no servidor
- [ ] HTTPS habilitado
- [ ] Logs monitorados

**Frontend:**
- [ ] `EXPO_PUBLIC_API_URL` aponta para produção
- [ ] Build testado em emulador
- [ ] Versão incrementada (package.json)
- [ ] EAS build configurado

**Banco:**
- [ ] Backups automáticos ativados (Neon)
- [ ] Monitoramento de performance
- [ ] Alertas configurados

---

## 🔒 Segurança Essencial

### NÃO FAZER:
```
❌ Commitar .env.production
❌ Deixar DEBUG=True em produção
❌ Expor IPs ou IDs privados
❌ Usar senha genérica no banco
```

### FAZER:
```
✅ Use variáveis de ambiente do servidor
✅ Armazene secrets em CI/CD (GitHub Secrets, etc)
✅ Habilite HTTPS/SSL
✅ Valide dados de entrada
✅ Use CORS restritivo
```

---

## 📊 Fluxo de Desenvolvimento → Produção

```
local dev (localhost:8000)
    ↓
    ↓ (git push)
    ↓
GitHub (main branch)
    ↓
    ↓ (CI/CD - GitHub Actions)
    ↓
Staging Server (teste final)
    ↓
    ↓ (manual approval)
    ↓
Produção (seu-dominio.com)
```

---

## 🎯 Próximos Passos Imediatos

1. **Escolha seu provider de deploy** (Recomendo: Render.com)
2. **Gere SECRET_KEY** seguro
3. **Configure variáveis de ambiente**
4. **Teste localmente com DEBUG=False**
5. **Crie repositório GitHub privado**
6. **Configure CI/CD**
7. **Deploy inicial para staging**
8. **Teste tudo**
9. **Deploy para produção**

---

## 📚 Recursos Úteis

- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/
- Render.com Docs: https://render.com/docs
- Expo Build: https://docs.expo.dev/build/setup/
- Neon Backups: https://neon.tech/docs/manage/backups/
