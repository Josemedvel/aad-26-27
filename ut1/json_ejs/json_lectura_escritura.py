import json
from pathlib import Path

ruta = Path(__file__).parent / "personas.json"

personas = [
    {"id": 1, "nombre": "Ana", "edad": 25, "activo": True},
    {"id": 2, "nombre": "Juan", "edad": 32, "activo": False},
]

# Escritura: dumps convierte el objeto Python en un str JSON
with open(ruta, "w", encoding="utf-8") as f:
    f.write(json.dumps(personas, indent=2, ensure_ascii=False))

# Lectura: loads convierte el str JSON en objetos Python
with open(ruta, "r", encoding="utf-8") as f:
    datos = json.loads(f.read())

print(type(datos))  # list
for persona in datos:
    print(persona["nombre"], persona["edad"], persona["activo"])  # tipos conservados
