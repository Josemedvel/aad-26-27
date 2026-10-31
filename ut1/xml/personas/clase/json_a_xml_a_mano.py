import json
from pathlib import Path
from lxml import etree
import types

dicc = {"nombre": "jose"}
print(type(type(dicc)))


def recorrer_diccionario(dicc):
    for clave in dicc:
        if clave.isinstance(types.str):
            print(clave)
        elif type(dicc[clave]) == "<class 'list'>":
            for el in dicc[clave]:
                recorrer_diccionario(el)
        elif type(dicc[clave]) == "<class 'dict'>":
            recorrer_diccionario(el)
        else:
            print(type(dicc[clave]), dicc[clave],"no cubierto")


    

p = Path(__file__).parent / "ejemplo_json.json"

with open(p, "r", encoding="utf-8") as f:
    contenidos = json.load(f)
    
#print(contenidos)

recorrer_diccionario(contenidos)
