from pathlib import Path
import time

p = Path("logs")

# creacion de carpeta
if not p.exists():
    Path.mkdir(p)

# creacion de archivos
for i in range(5):
    with open(f"logs/f{i}.txt", "w") as f:
        f.writelines(["hola"])
time.sleep(2)
if p.exists():
    # borrar ficheros
    ficheros = list(p.glob("*"))
    print(ficheros)
    for f in ficheros:
        if f.exists() and f.is_file():
            f.unlink()
    # borrar carpeta
    Path.rmdir(p)
