import time
import re

index = 'index.html'
with open(index, 'r') as f:
    text = f.read()

# Add cache buster:
ts = int(time.time())
text = re.sub(r'href="css/style\.css(\?[^"]+)?"', f'href="css/style.css?v={ts}"', text)

with open(index, 'w') as f:
    f.write(text)
