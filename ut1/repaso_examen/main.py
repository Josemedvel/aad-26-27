from pathlib import Path
from lxml import etree
import json

def prettyprint(element):
    xml = etree.tostring(element, pretty_print=True)
    print(xml.decode(), end="")

p = Path(__file__).parent / "customers.xml"
p_out = Path(__file__).parent / "codigos_postales.json"


tree = etree.parse(p)
root = tree.getroot()
print(etree.iselement(root))

codigos = {}

customers = root.findall("customer")
print(customers)
for c in customers:
    addresses = c.findall("address")
    for a in addresses:
        zip_code = a.find("zip")
        # print(zip_code.text)
        if zip_code.text in codigos:
            codigos[zip_code.text] += 1
        else:
            codigos[zip_code.text] = 1
        
print(codigos)
with open(p_out, "w", encoding="UTF-8") as f:
    json.dump(codigos, f, ensure_ascii=False)
    
direccion_nueva = etree.Element("address")
calle = etree.SubElement(direccion_nueva, "street")
calle.text = "Calle Manzana 4"
ciudad = etree.SubElement(direccion_nueva, "city")
ciudad.text = "Mostoles"
provincia = etree.SubElement(direccion_nueva, "state")
provincia.text = "Madrid"
codigo_postal = etree.SubElement(direccion_nueva, "zip")
codigo_postal.text = "28604"
prettyprint(direccion_nueva)

cliente_1 = root.find("customer[@id='55000']")
if etree.iselement(cliente_1):
    cliente_1.append(direccion_nueva)

prettyprint(root)

tree.write(p, pretty_print=True, encoding="UTF-8", xml_declaration=True)


