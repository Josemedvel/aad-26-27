with open("ut1.pdf", "rb") as f:
    chunk_size = 2048
    chunk = f.read(chunk_size)
    print(chunk)
    while chunk:
        chunk = f.read()
        print(chunk, type(chunk))
        
        
with open("texto.txt", "r", encoding="utf-8") as f:
    chunk_size = 35
    chunk = f.read(chunk_size)
    print(chunk)
    while chunk:
        chunk = f.read()
        print(chunk, type(chunk))