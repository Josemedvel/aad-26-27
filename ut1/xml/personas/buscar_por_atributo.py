from pathlib import Path

from lxml import etree

tree = etree.parse(Path(__file__).parent / "personas.xml")
root = tree.getroot()

# Elementos que tienen el atributo
for p in root.findall("persona[@activo]"):
    print("Con atributo activo:", p.get("id"))

# Elementos con un valor concreto en el atributo
for p in root.findall("persona[@activo='true']"):
    print("Activos:", p.find("nombre").text)

# Primer elemento con id concreto
p = root.find("persona[@id='2']")
if p is not None:
    print("id=2:", p.find("nombre").text)

# Con XPath (cualquier nivel, y atributo distinto de un valor)
print(root.xpath("//persona[@activo!='true']/nombre/text()"))
print(root.xpath("//persona[@id='1']/@activo"))  # devuelve el valor del atributo

