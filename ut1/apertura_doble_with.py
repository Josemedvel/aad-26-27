with open("lectura.txt", "rb") as l, open("copia.txt", "wb") as e:
    chunk = l.read(2048)
    while chunk:
        e.write(chunk)
        chunk = l.read(2048)

