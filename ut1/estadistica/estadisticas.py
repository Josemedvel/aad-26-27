# porcentaje de pasajeros supervivientes
# porcentaje de hombres y mujeres supervivientes
# porcentaje de menores supervivientes
# media de edad del superviviente
# media de edad de la victima
# ticket medio del superviviente
# ticket medio de la victima

pasajeros = []

def porcentaje_supervivientes(datos):
    numero_supervivientes = 0
    for p in datos:
        if p["sup"] == 1:
            numero_supervivientes += 1
    return (numero_supervivientes / len(datos)) * 100

def porcentaje_por_sexo(datos):
    hombres_sup = 0
    hombres_totales = 0
    mujeres_sup = 0
    mujeres_totales = 0
    for p in datos:
        if p["sex"] == 1: # hombre
            hombres_totales += 1
            if p["sup"] == 1:
                hombres_sup += 1
        else: #mujer
            mujeres_totales += 1
            if p["sup"] == 1:
                mujeres_sup += 1
    return (hombres_sup / hombres_totales * 100, mujeres_sup / mujeres_totales * 100)

with open("titanic.csv", "r", encoding="utf-8") as f:
    f.readline()
    for linea in f:
        datos = linea.split(",")
        pasajero = {}
        pasajero["sup"] = int(datos[0])
        pasajero["class"] = int(datos[1])
        pasajero["sex"] = 1 if datos[2] == "male" else 0
        if datos[3].strip() == "":
            continue
        pasajero["age"] = float(datos[3])
        pasajero["fare"] = float(datos[4])
        pasajeros.append(pasajero)


print(f"Porcentaje de supervivientes: {porcentaje_supervivientes(pasajeros):0.2f}%")
print(f"Porcentaje de hombres supervivientes: {porcentaje_por_sexo(pasajeros)[0]:0.2f}%")
print(f"Porcentaje de mujeres supervivientes: {porcentaje_por_sexo(pasajeros)[1]:0.2f}%")
    
        
        
        
        
        