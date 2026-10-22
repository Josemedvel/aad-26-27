from lxml import etree
from pathlib import Path

ruta = Path(__file__).parent.parent / "personas.xml"
print(ruta)

tree = etree.parse(ruta)
root = tree.getroot()

print(root)
first_person = root.find("persona")
# creamos el elemento nuevo
address = etree.Element("direccion")
address.text = "C/ de Móstoles, 64, Fuenlabrada"
# añadimos el elemento nuevo
first_person.append(address)
# buscamos el elemento nuevo
address_search = first_person.find("direccion")
print(address_search.text)

# recorrer hijos
for sub in first_person:
    print(sub.tag,"-->" ,sub.text)

people = root.findall("persona")
# cantidad de personas
print(len(people))
print(len(root))

# creacion etiqueta teléfono
phone_number = etree.SubElement(first_person, "telefono", tipo='movil')
phone_number.text = "87265483"

for sub in first_person:
    if sub.attrib.items():
        print(sub.tag,"-->" ,sub.text, "atributos:" ,sub.attrib.items())
    else:
        print(sub.tag,"-->" ,sub.text)