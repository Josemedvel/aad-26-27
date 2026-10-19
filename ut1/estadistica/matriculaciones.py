cabecera = ("fecha", "marca", "modelo", "num_bastidor", "cilindrada", "ni_idea", "num_asientos", "municipio")

matriculaciones = []

with open("export_mat_20260928.txt", "r", encoding="windows-1252") as f:
    f.readline()
    for linea in f:
        cursor = 0
        fecha_mat = linea[cursor:cursor + 8]
        cursor += 8
        cod_clase_mat = linea[cursor:cursor + 1]
        cursor += 1
        fec_tramitacion = linea[cursor: cursor + 8]
        cursor += 8
        marca_itv = linea[cursor: cursor + 30]
        cursor += 30
        modelo_itv = linea[cursor: cursor + 22]
        cursor += 22
        cod_procedencia_itv = linea[cursor: cursor + 1]
        cursor += 1
        bastidor_itv = linea[cursor : cursor + 21]
        cursor += 21
        cod_tipo = linea[cursor : cursor + 2]
        cursor += 2
        cod_propulsion_itv = linea[cursor : cursor + 1]
        cursor += 1
        cilindrada_itv = linea[cursor : cursor + 5]
        vehiculo = {
            "fec_mat": fecha_mat,
            "marca": marca_itv.strip(),
            "modelo": modelo_itv.strip(),
            "cilindrada": int(cilindrada_itv.strip())
            }
        matriculaciones.append(vehiculo)
    print(matriculaciones[:20])
