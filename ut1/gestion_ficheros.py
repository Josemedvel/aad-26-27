from pathlib import Path

p = Path('docs')
print(p)
print(p.exists())
print(p.is_file())
#print(p.rename('docs/informe2.txt'))
print(p.suffix)
#print(p.read_text(encoding="utf-8"))
print(list(p.glob('*.txt')))