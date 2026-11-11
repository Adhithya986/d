import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

img_srcs = re.findall(r'src=["\'](images/[^"\']+)["\']', html_content)
print(f"Total img tags found: {len(img_srcs)}")

missing = [s for s in set(img_srcs) if not os.path.exists(s)]
if missing:
    print("Missing images:", missing)
else:
    print("All referenced images exist on disk!")

# Check section IDs
ids = re.findall(r'id=["\'](sec-[^"\']+)["\']', html_content)
print("Found section IDs:", ids)

# Check buttons and copy attributes
copy_btns = re.findall(r'data-copy=', html_content)
print(f"Total copyable code buttons: {len(copy_btns)}")

