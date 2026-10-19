import json
from pathlib import Path

import xmltodict
import yaml

ruta = Path(__file__).parent / "personas.xml"

# XML -> diccionario (los atributos pasan a ser claves con prefijo @)
datos = xmltodict.parse(ruta.read_text(encoding="utf-8"))

# JSON
print(json.dumps(datos, indent=2, ensure_ascii=False))

# YAML
print(yaml.dump(datos, allow_unicode=True))

# diccionario -> XML
print(xmltodict.unparse(datos, pretty=True))

