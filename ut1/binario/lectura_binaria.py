extensiones = {
    "jpeg" : b'\xff\xd8\xff',
    "pdf" : b'\x25\x50\x44\x46',
    }

def is_jpeg(path):
    with open(path, "rb") as f:
        return f.read(3) == extensiones["jpeg"]

def is_pdf(path):
    with open(path, "rb") as f:
        return f.read(4) == extensiones["pdf"]
    

print(is_jpeg("gato.jpeg"))
print(is_pdf("gato.jpeg"))
print(is_pdf("ut1.pdf"))
    