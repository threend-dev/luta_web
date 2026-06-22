import re
with open('pages/home.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Instead of `style="position: relative; overflow: hidden; border-radius: 26px;"`, we set explicit layout styles
old_style = 'style="position: relative; overflow: hidden; border-radius: 26px;"'
new_style = 'style="position: relative; overflow: hidden; border-radius: 26px; display: block;"'

content = content.replace(old_style, new_style)

# Also let's clean up any previous inline <style> we appended earlier, just to be safe.
# Actually, no need to clean up if it's not hurting, but it's cleaner without duplicates.
content = re.sub(r'<style>.*?local-slide-gallery.*?</style>', '', content, flags=re.DOTALL)

with open('pages/home.html', 'w', encoding='utf-8') as f:
    f.write(content)
