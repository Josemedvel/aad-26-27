tablero = [[" " for j in range(3)] for i in range(3)]
'''tablero = []
for x in range(3):
    tablero.append(["","",""])
'''
print(tablero)
jugadores = {
    0: "X",
    1: "O",
    }

partida_terminada = False
turno = 0


def hacer_jugada(jugador, tablero):
    jugada_valida = False
    while not jugada_valida:
        # fila
        fila = input("Ingresa la fila de la jugada: \t")
        while not comprobar_coordenada(fila):
            fila = input("Ingresa la fila de la jugada: \t")
        # columna
        fila = int(fila)
        columna = input("Ingresa la columna de la jugada: \t")
        while not comprobar_coordenada(columna):
            columna = input("Ingresa la columna de la jugada: \t")
        columna = int(columna)
        # casilla_ocupada
        if not casilla_ocupada(fila, columna, tablero):
            jugada_valida = True
        if not jugada_valida:
            print("La jugada no es válida, repite las coordenadas")
    tablero[fila][columna] = jugador
    
def casilla_ocupada(fila, columna, tablero):
    return tablero[fila][columna] != " "

def comprobar_coordenada(num):
    if not num.isnumeric():
        print("La coordenada debe ser un número entero de 0 a 2")
        return False
    if int(num) < 0 or int(num) > 2:
        print("La coordenada debe ser un número entero de 0 a 2")
        return False
    else:
        return True



def mostrar_tablero(tablero):
    for i,v in enumerate(tablero):
        for j, k in enumerate(v):
            print(k, end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("-"*9)

def v_vertical(jugador, tablero):
    for j in range(len(tablero[0])): 
        numero_fichas = 0
        for i in range(len(tablero)):
            if tablero[i][j] == jugador:
                numero_fichas += 1
        if numero_fichas == 3:
            return True
    return False

def v_horizontal(jugador, tablero):
    for i in range(len(tablero)): 
        numero_fichas = 0
        for j in range(len(tablero[0])):
            if tablero[i][j] == jugador:
                numero_fichas += 1
        if numero_fichas == 3:
            return True
    return False

def v_diagonal(jugador, tablero):
    mayor = 0
    menor = 0
    #mayor
    for i in range(len(tablero)):
        if tablero[i][i] == jugador:
            mayor += 1
    ## de 0 a 2    
    for i in range(len(tablero)):
        if tablero[len(tablero) - 1 - i][i] == jugador:
            menor += 1
    return mayor == 3 or menor == 3

def victoria(jugador, tablero):
    return v_vertical(jugador, tablero) or \
           v_horizontal(jugador, tablero) or \
           v_diagonal(jugador, tablero)
    



def empate(tablero):
    huecos = 0
    for i in tablero: # filas ([X, O, X])
        for v in i: # columnas (X)
            if v == " ":
                huecos += 1
    return huecos == 0


def partida():
    global turno, tablero, jugadores, partida_terminada
    while not partida_terminada:
        print(f"Es el turno del jugador {jugadores[turno % 2]}")
        mostrar_tablero(tablero)
        hacer_jugada(jugadores[turno % 2], tablero)
        if victoria(jugadores[turno % 2], tablero):
            partida_terminada = True
            print(f"Gana el jugador {jugadores[turno % 2]}")
        elif empate(tablero):
            partida_terminada = True
            print("Ha habido un empate!!")
        else:
            turno += 1

partida()