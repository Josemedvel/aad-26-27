from lxml import etree

def imprimir_arbol(elemento, nivel=0):
    indent = "\t" * nivel
    attrs = " ".join(f'{k}="{v}"' for k, v in elemento.attrib.items())
    texto = (elemento.text or "").strip()
    print(f"{indent}<{elemento.tag} {attrs}> {texto}")
    for hijo in elemento:
        imprimir_arbol(hijo, nivel + 1)
        
root = etree.parse("papers_arxiv.xml").getroot()
imprimir_arbol(root)