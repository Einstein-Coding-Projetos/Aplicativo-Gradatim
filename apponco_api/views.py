"""Compat layer: encaminha para backend/apponco_api equivalente."""

from pathlib import Path
import runpy

_repo_root = Path(__file__).resolve().parents[1]
_backend_file = _repo_root / "backend" / "apponco_api" / Path(__file__).name

if not _backend_file.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {_backend_file}")

globals().update(runpy.run_path(str(_backend_file)))