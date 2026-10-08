from pathlib import Path
import time
# creacion de ficheros automática
for i in range(5):
    with open(f"logs/f{i}.txt", "a") as f:
        f.write("hola")

for i in range(5):
    with open(f"f{i}.txt", "a") as f:
        f.write("hola")


p = Path("logs/log.txt")

if p.exists() and p.is_file():
    p.unlink()

p = Path(".")
# borrado con búsqueda
ficheros = list(p.glob("f*.txt"))
p /= "logs"
ficheros_logs = list(p.glob("f*.txt"))
print(ficheros.extend(ficheros_logs))
print(ficheros)

time.sleep(10)

for f in ficheros:
    if f.exists() and f.is_file():
        f.unlink()
print("archivos borrados")