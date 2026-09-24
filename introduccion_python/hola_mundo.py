# hola mundo
print('Hola buenas')

print("""
                asndkfoasndf
asdfasdfa
asdfafda
""")

a = "Hola"

# tipos de datos
num_int = 6
verdadero = True
decimal = 3.14
dec_cient = 314e-2
comp = 3 + 4j


# estructuras de datos
tupla = ("Juan", 5, True)
print(tupla[0])
print("tupla:",tupla,", tipo:", type(tupla))
print("tupla: " + str(tupla) + ", tipo: " + str(type(tupla)))
print(f"tupla: {tupla}, tipo: {type(tupla)}")
print("X", end="\t")
print("X")
print("_"*20)
lista = [1,2,3]#list()
lista.append(4)
print(lista)
lista.insert(1,10)
lista_2 = [7,9]
lista.extend(lista_2)
print(lista)
lista.append(tupla)
print(lista)
lista[-1] = ("Roberto", 5, True)
print(lista)
tupla_2 = (1, [1,2])
tupla_2[1].append(3)
print(tupla_2)

#operadores
#lógicos
print(True and False)
print(True or False)
print(not True)

#aritmético-lógicos
suma = 4 + 5
resta = 10 - 3
mult = 3 * 5
division = 20 // 3
div_exacta = 20 / 3
print(division)
modulo = 23 % 3
print(modulo)
#asignación
b = 4
#relacionales
print(4 == 4)
print(3 <= 10)
print(4 > 8)
print(4 != 4)
#acceso
import math
print(math.pi)

#constantes
PRECIO_SUSCRIPCION = 15

#conversion de segundos a horas, minutos y segundos
#8541s
horas = 8541 // 3600
minutos = (8541 - (horas * 3600)) // 60
segundos = 8541 - (horas * 3600) - (minutos * 60)
print(f"{horas}:{minutos}:{segundos}")

horas = 8541 / 3600
minutos = (horas - int(horas)) * 60
print(f"{int(horas)}:{int(minutos)}")

# sacar elementos de la lista
lista = [1,2,3]
b = lista.pop(0)
print(lista, b)

lista_bi = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
            ]
diccionario = {
        "coche": ("Seat", "Ateca", 50000, 2020),
        "moto": ("Yamaha", "Xmax")
    }

print(diccionario["coche"])
diccionario["yate"] = ("Bribón", 1999,"Mallorca")
print("patinete" in diccionario)
del(diccionario["yate"])
print(diccionario)

conj = {"Jose", "María", "Marta", "Alberto"}
conj.add("Jose")
print(conj)




