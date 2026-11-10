from pathlib import Path

p = Path(__file__).parent / "dummy-1000-rows.csv"

ocurrencias = {}

with open(p, "r", encoding="UTF-8") as f:
    #print(f.read())
    f.readline()
    for l in f:
        campos = l.split(",")
        email = campos[-1]
        dominio = email.split("@")[-1]
        dominio = dominio.replace("\n", "")
        if dominio in ocurrencias:
            ocurrencias[dominio] += 1
        else:
            ocurrencias[dominio] = 1
print(ocurrencias)
total = 0
for k in ocurrencias:
    total += ocurrencias[k]
print(total)

porcentajes = {}
for k in ocurrencias:
    porcentajes[k] = (ocurrencias[k] / total) * 100
print(porcentajes)
