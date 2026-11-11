# -*- coding: utf-8 -*-
import json

with open('raw_manual.txt', 'r', encoding='utf-8') as f:
    raw_manual_text = f.read()

with open('app_base.js', 'r', encoding='utf-8') as f:
    app_base_code = f.read()

raw_json = json.dumps(raw_manual_text)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(f"// Embedded verbatim raw manual text ({len(raw_manual_text)} chars)\n")
    f.write(f"const RAW_MANUAL_TEXT = {raw_json};\n\n")
    f.write(app_base_code)

print(f"Created app.js successfully with {len(raw_manual_text)} raw chars embedded.")

