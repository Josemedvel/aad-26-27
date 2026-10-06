contenido_binario = None
with open("gato.jpeg", "rb") as f:
    contenido_binario = f.read()
print(contenido_binario)

with open("gato_2.jpeg", "wb") as f:
    f.write(contenido_binario+ b'\x55')


