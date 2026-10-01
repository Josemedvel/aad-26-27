# podemos buscar nodos, por etiquetas o por atributos
from lxml import etree

# definimos los namespaces si fuese necesario (en este caso sí)
ns = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

# búsqueda por etiqueta
# primer artículo que sea del autor "Michael Reusens"
root = etree.parse("papers_arxiv.xml").getroot()

autor = root.find(".//atom:author", namespaces=ns)
print(autor)
