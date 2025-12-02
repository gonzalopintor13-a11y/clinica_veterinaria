import logging
from datetime import datetime
import os

# Crear carpeta logs si no existe
os.makedirs("logs", exist_ok=True)

LOG_FILE = f"logs/clinica_{datetime.now().strftime('%Y%m%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=LOG_FILE,
    filemode="a"
)

logger = logging.getLogger("clinica")
