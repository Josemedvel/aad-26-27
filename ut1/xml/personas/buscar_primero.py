from pathlib import Path

from lxml import etree

tree = etree.parse(Path(__file__).parent / "personas.xml")
root = tree.getroot()

primera_persona = root.find("persona")
print(primera_persona)
