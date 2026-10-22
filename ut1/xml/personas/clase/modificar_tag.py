from lxml import etree
from pathlib import Path

ruta = Path(__file__).parent.parent / "personas.xml"

tree = etree.parse(ruta)
root = tree.getroot()

first_person = root.find("persona")
if etree.iselement(first_person):
    print(first_person.tag)
    first_person.tag = "person"
    print(type(first_person.text))
    print(first_person.text.strip() == "")
    print(f"'{first_person.text}'")
    print(first_person.tag)
    
    persona_objetivo = root.find("persona[@id='2']")
    if etree.iselement(persona_objetivo):
        print(persona_objetivo.find("nombre").text)        
        print(persona_objetivo.find("edad").text)
    edad_etiqueta = persona_objetivo.find("edad")
    if etree.iselement(edad_etiqueta):
        edad = edad_etiqueta.text
    try:
        edad = int(edad)
    except Exception:
        edad = 18
    edad = edad + 1
    edad_etiqueta.text = str(edad)
    
    for e in persona_objetivo:
        print(e.tag, e.text)
