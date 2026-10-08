from datetime import datetime
from pathlib import Path
from multiprocessing import Process
import time

p_log_dir = Path('logs')
p_log = p_log_dir / 'log.txt' # Path

try:
    Path.mkdir(p_log_dir, parents=True)
    with open(p_log, "a") as log:
        log.write(f"<{datetime.now()}> - Carpetas creadas\n")
except FileExistsError:
    with open(p_log, "a") as log:
        log.write(f"<{datetime.now()}> - Carpetas ya existe, abortando creación\n")
finally:
    with open(p_log, "a") as log:
        log.write(f"<{datetime.now()}> - Programa arranca\n")   

with open(p_log, "a") as log:
    while True:
        time.sleep(1)
        log.write(f"<{datetime.now()}> - Procesando información\n")