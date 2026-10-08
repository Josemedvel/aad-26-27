from lxml import etree

def prettyprint(root):
    xml = etree.tostring(root, pretty_print=True)
    print(xml.decode(), end="")

tree = etree.parse("personas.xml")
root = tree.getroot()

p = root.find("persona")
if etree.iselement(p):
    print(p.items()) # pares
    print(p.values()) # valores
    print(p.keys()) # claves
    print(p.get("id")) # uno en concreto
    
    # modificamos uno
    p.set("id", "2345")
    # añadimos uno nuevo
    p.set("nuevo", "vecino")
    # borramos el otro
prettyprint(root)


