with open("ut1.pdf", "rb") as lector, open("copia.pdf", "wb") as escritor:
    contenido = lector.read()
    escritor.write(contenido)
    print("copia realizada exitosamente")