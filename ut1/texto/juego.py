import json

estado = [489778, 7, 200, 75, {
                                "0":"charizard",
                                "1": "articuno",
                                "2": "bulbasaur",
                              }
         ]

with open("guardado.save", "w", encoding="utf-8") as save:
    for item in estado[:-1]:
        save.write(str(item) + ";")
    #print(json.dumps(estado[-1]), type(json.dumps(estado[-1])))
    save.write(json.dumps(estado[-1]))
    print("Tu partida ha sido guardada")
    
with open("guardado.save", "r", encoding="utf-8") as save:
    linea = save.read()
    items_save = linea.split(";")
    estado = [int(item) for item in items_save[:-1]]
    print(items_save[-1])
    pokemons = json.loads(items_save[-1])
    estado.append(pokemons)
    print("Partida cargada exitosamente")
    print(estado)
    