import zipfile
import xml.etree.ElementTree as ET
import os

with zipfile.ZipFile('DBMS_LAB_MANUAL---2025-26 II-I SEM(updated).docx') as z:
    rels_xml = z.read('word/_rels/document.xml.rels')
    doc_xml = z.read('word/document.xml')

rels_tree = ET.fromstring(rels_xml)
r_map = {rel.attrib.get('Id'): rel.attrib.get('Target') for rel in rels_tree}

doc_tree = ET.fromstring(doc_xml)
w_ns = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
a_ns = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
r_ns = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

images_found = []
for p in doc_tree.iter(f'{w_ns}p'):
    p_text = ''.join([t.text for t in p.iter(f'{w_ns}t') if t.text]).strip()
    blips = p.findall(f'.//{a_ns}blip')
    for b in blips:
        rid = b.attrib.get(f'{r_ns}embed')
        target = r_map.get(rid, '')
        images_found.append((p_text[:50], target))

print(f"Total image references: {len(images_found)}")
for pt, tgt in images_found:
    print(f"{tgt:30} -> {pt}")

