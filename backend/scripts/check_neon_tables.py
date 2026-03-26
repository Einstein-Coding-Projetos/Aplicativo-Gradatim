import os
import sys
from pathlib import Path
import django

SCRIPT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = SCRIPT_DIR.parent
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apponco_api.settings')
django.setup()

from django.db import connection

# Testar conexão
try:
    with connection.cursor() as cursor:
        # Listar tabelas
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema='public'
            ORDER BY table_name
        """)
        tables = cursor.fetchall()
        
        print("📊 TABELAS NO NEON:")
        print("="*50)
        if tables:
            for (table_name,) in tables:
                print(f"  ✅ {table_name}")
        else:
            print("  ❌ NENHUMA TABELA ENCONTRADA!")
        
        # Verificar migrações
        print("\n📋 MIGRAÇÕES APLICADAS:")
        print("="*50)
        cursor.execute("SELECT * FROM django_migrations ORDER BY applied DESC LIMIT 10")
        migrations = cursor.fetchall()
        for mig in migrations:
            print(f"  ✅ {mig[1]} - {mig[2]}")
            
except Exception as e:
    print(f"❌ ERRO: {e}")
    print("\n⚠️  Possíveis causas:")
    print("  1. DATABASE_URL não configurado em .env")
    print("  2. Conexão Neon offline")
    print("  3. Credenciais incorretas")
