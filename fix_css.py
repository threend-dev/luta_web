import re

css = 'css/style.css'
with open(css, 'r') as f:
    text = f.read()

# remove old slider-img css
text = re.sub(r'\.screen-slider\s*\{[^}]*\}', '', text)
text = re.sub(r'\.slider-img\s*\{[^}]*\}', '', text)
text = re.sub(r'@keyframes scroll-h\s*\{[^}]*\}', '', text)

new_css = '''
.panorama-img {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: auto;
  object-fit: cover;
  /* Since the image height is 100% (560px), its width is ~258px (for 1290x2796). Wait. If the user wants horizontal scroll, either width is much larger, or I should just set height to, say, 150% or 200%. */
  height: 120%; /* Zoom in so width becomes > 100%. If height is 672px, width is 309px > 280px. */
  transform: translateX(0);
  animation: pan-image 10s alternate infinite ease-in-out;
}

@keyframes pan-image {
  0% { transform: translate(0, -10%); }
  100% { transform: translate(calc(-100% + 280px), -10%); }
}
'''
text += new_css

with open(css, 'w') as f:
    f.write(text)
