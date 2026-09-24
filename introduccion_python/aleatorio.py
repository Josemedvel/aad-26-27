import random

palabra = "casa"
indice = random.randint(0, len(palabra) - 1)
print(palabra[indice])
jugadas_1 = random.choices(["piedra", "papel", "tijera"],k=1)
jugada_2 = random.choice(["piedra", "papel", "tijera"])
print(jugadas_1, jugada_2)
print(random.random())

