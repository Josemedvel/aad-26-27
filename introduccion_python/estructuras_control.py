#condicional simple
edad = 19
dinero = 25
if edad >= 18 and dinero >= 25:
    print("Puedes pasar a la discoteca")
# condicional con alternativa
else:
    print("No puedes pasar")
    
if dinero < 18000:
    print("No te puedes comprar un coche nuevo")
elif dinero < 20000:
    print("Te puedes comprar un Renault 5 nuevo")
elif dinero < 30000:
    print("Te puedes comprar un Volkswagen Polo sin los extras")
elif dinero < 50000:
    print("Te puedes comprar un Toyota Rav4")
else:
    print("No me digas que te has comprado un coche")

# match también

# bucles
limite = 10
print("Cuenta atras")
'''
while limite > 0:
    print(limite)
    limite -= 1
'''
for i in range(0,6, 1):
    print(i, end=" ")
print()

multiplos = []
for i in range(7, 101, 7):
    multiplos.append(i)
print(multiplos)
print(multiplos[:5])
print(multiplos[-5:])
print(multiplos[2:6])
print(multiplos[::3])
print(multiplos[::-1])
multiplos_5 = [x for x in range(5,101,5)]
print(multiplos_5)

for i in range(len(multiplos)):
    print(multiplos[i], end=" ")
print()

for i in multiplos:
    print(i, end=" ")
print()

for i,v in enumerate(multiplos):
    print(i,v)
print()


# I/O
numero = int(input("Ingresa un numero:\t"))
print(numero)

# metodos
def suma(a,b):
    return a+b

