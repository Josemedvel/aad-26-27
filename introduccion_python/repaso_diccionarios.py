datos_alumnos = {
    "1": {
        "nombre": "Antonio",
        "curso" : 2,
        "ciclo" : "DAM",
        },
    }
print(datos_alumnos)
# indexación de datos
print(datos_alumnos["1"]["curso"])
datos_alumnos["2"] = {
    "nombre" : "Julia",
    "curso" : 1,
    "ciclo" : "DAW",
    }
print(datos_alumnos)
# borrado de Antonio
del(datos_alumnos["1"])
print(datos_alumnos)

# comprobar existencia de clave
if "2" in datos_alumnos:
    print(datos_alumnos["2"]["nombre"])

# iterar un diccionario
for clave in datos_alumnos:
    print(datos_alumnos[clave])

# lista de claves del diccionario
print(datos_alumnos.keys())
# lista de valores del diccionario
print(datos_alumnos.values())

try:
    # KeyError
    print(datos_alumnos["2345"])
except KeyError:
    print("La clave no existe")
# None
print(datos_alumnos.get("2345", -1))

# calcular la moda de una lista de n numeros
import random
random.seed(0)
lista_aleatoria = [random.randint(0,10) for x in range(10)]
print(lista_aleatoria)


def moda_1(lista):
    num_max_rep = 0
    num_mas_rep = None
    for i in lista:
        num_rep_actual = 0
        for j in lista:
            if j == i: # coinciden los números
                num_rep_actual += 1
                if num_rep_actual > num_max_rep:
                    num_max_rep = num_rep_actual
                    num_mas_rep = i                
    print(num_mas_rep, num_max_rep)

def moda_2(lista):
    repeticiones = {}
    num_max_rep = 0
    num_mas_rep = None
    for i in lista:
        if i in repeticiones:
            repeticiones[i] += 1
        else:
            repeticiones[i] = 1
        if repeticiones[i] > num_max_rep:
            num_max_rep = repeticiones[i]
            num_mas_rep = i
    print(num_mas_rep, num_max_rep)
    
def moda_3(lista):
    num_max_rep = 0
    num_mas_rep = None
    for i in lista:
        rep = lista.count(i)
        if rep > num_max_rep:
            num_max_rep = rep
            num_mas_rep = i
    print(num_mas_rep, num_max_rep)

moda_3(lista_aleatoria)