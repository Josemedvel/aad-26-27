with open("quijote.txt", "r", encoding="utf-8") as f:
    print(f.readlines()[:20])
    
with open("quijote.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea)