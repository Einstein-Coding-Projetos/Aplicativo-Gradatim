"""Compat layer: encaminha settings para backend/apponco_api/settings.py.
Mantém compatibilidade para imports legados sem permitir divergência de schema.
"""

from pathlib import Path
import runpy

_repo_root = Path(__file__).resolve().parents[1]
_backend_settings = _repo_root / "backend" / "apponco_api" / "settings.py"

if not _backend_settings.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {_backend_settings}")

globals().update(runpy.run_path(str(_backend_settings)))