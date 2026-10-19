from datetime import datetime
import time
import uuid

print(datetime.now())
print(uuid.uuid1())

diccionario = {}
clave = uuid.uuid1()
diccionario = {}
diccionario[clave] = {}
diccionario[clave]["titulo"] = "Eyes wide shut"
diccionario[clave]["puntuacion"] = 4.5
diccionario[clave]["cita"] = "la corrupción humana se da en todos los estratos sociales"
print(diccionario)
