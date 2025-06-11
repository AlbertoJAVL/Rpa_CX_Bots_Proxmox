import os, shutil, logging
from pathlib import Path
import logging

logger = logging.getLogger("rpa.temp")
EXCLUDE_EXT = {".log", ".tmp", ".crdownload"}

def eliminar_archivos():
    """Elimina archivos y carpetas en %TEMP% que no estén en uso."""
    temp_folder = Path(os.environ["TEMP"])
    for entry in temp_folder.iterdir():
        try:
            if entry.suffix.lower() in EXCLUDE_EXT:
                continue
            if entry.is_file():
                entry.unlink()
            else:
                shutil.rmtree(entry, ignore_errors=True)
        except Exception as e:
            logger = logging.getLogger("rpa")
            logger.exception("Fallo en orden %s: %s", e) 
            logger.debug("No se pudo eliminar %s: %s", entry, e)
