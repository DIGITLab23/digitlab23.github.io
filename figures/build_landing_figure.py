"""Build static/img/landing_figure.svg from the editable Inkscape source.

    python figures/build_landing_figure.py

1. Inkscape converts all text to outlines (visitors don't have the hand-lettering
   font, and Chromium can't render text on a <circle> path).
2. Each element is wrapped in an animation group and the animation CSS is added.
   Wrapping keeps Inkscape's own `transform` attributes intact, since CSS
   transform animations would otherwise replace them.

Edit figures/landing_figure.inkscape.svg in Inkscape, then rerun this script.
To retime the animation, edit STAGES and CSS below.
"""
import pathlib
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / 'landing_figure.inkscape.svg'
OUT = HERE.parent / 'static' / 'img' / 'landing_figure.svg'
INKSCAPE = r'C:\Program Files\Inkscape\bin\inkscape.exe'

SVG = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG)
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')

# Storyboard: (start time in seconds, animation class, element ids).
# The outer circle's growth and the breathing pulse are set in CSS below.
STAGES = [
    # the human designer appears first, inside "what we can design alone"
    (0.0, 'pop', ['g3', 'text27-4-8-7-6-6-2-3-2-3-5-8-2-1-4-8']),
    # AI arrives and the design space grows around the designer
    (0.9, 'pop', ['g25']),
    # the engineering domains come within reach, left side then right side
    (1.2, 'pop', ['image13']), (1.28, 'pop', ['image12']), (1.36, 'pop', ['image11']),
    (1.44, 'pop', ['image14']), (1.52, 'pop', ['image15']), (1.6, 'pop', ['image16']),
    # side 1: push the limits of design
    (1.6, 'pop', ['text27-4-8-7-6-6-2-3-2-3-5-8-2-1-4-8-6', 'g23', 'g24']),
    (1.9, 'draw', ['path1', 'path2']),
    # side 2: keep the human at the center
    (2.4, 'pop', ['text27-4-8-7-6-6-2-3-2-3-5-8-2-1-4-8-6-5', 'g26', 'g20']),
    (2.7, 'draw', ['path1-8', 'path2-2']),
]

CSS = '''
  .ring { fill: none; stroke-linecap: round; filter: url(#rough); }
  #outer { stroke: #de6866; stroke-width: 4; fill: #de6866; fill-opacity: .07;
           transform-origin: 500px 500px; animation: grow 1.6s cubic-bezier(.2,.7,.2,1) .3s both; }
  #space { transform-origin: 500px 500px; animation: breathe 7s ease-in-out 2.4s infinite; }
  #inner { stroke: #a6a283; stroke-width: 3; stroke-dasharray: 10 12; fill: #a6a283; fill-opacity: .08; }
  .draw { fill: none; stroke: #de6866; stroke-width: 6; stroke-linecap: round; stroke-linejoin: round;
          stroke-dasharray: 1; stroke-dashoffset: 1; animation: draw .9s ease-out both; filter: url(#rough); }
  .pop { animation: pop .7s ease-out both; }
  @keyframes grow { from { transform: scale(.38); } to { transform: scale(1); } }
  @keyframes breathe { 0%,100% { transform: scale(1); } 50% { transform: scale(1.025); } }
  @keyframes draw { to { stroke-dashoffset: 0; } }
  @keyframes pop { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
  @media (prefers-reduced-motion: reduce) {
    #outer, #space, .draw, .pop { animation: none; stroke-dashoffset: 0; }
  }
'''


def q(t):
    return f'{{{SVG}}}{t}'


def main():
    with tempfile.TemporaryDirectory() as tmp:
        plain = pathlib.Path(tmp) / 'plain.svg'
        subprocess.run([INKSCAPE, str(SRC), '--export-text-to-path', '--export-plain-svg',
                        f'--export-filename={plain}'], check=True, capture_output=True)
        tree = ET.parse(plain)
    root = tree.getroot()
    children = list(root)
    by_id = {e.get('id'): e for e in children}
    missing = [i for _, _, ids in STAGES for i in ids if i not in by_id] + \
              [i for i in ('outer',) if i not in by_id]
    if missing:
        raise SystemExit(f'Not found as top-level elements in {SRC.name}: {", ".join(missing)}\n'
                         'Check the IDs in Inkscape (Object > Object Properties) and update STAGES.')

    root.find(q('style')).text = CSS

    # The circle and the label written along it breathe together.
    outer = by_id['outer']
    space = ET.Element(q('g'), id='space')
    root.insert(children.index(outer), space)
    root.remove(outer)
    space.append(outer)

    for delay, cls, ids in STAGES:
        for i in ids:
            el = by_id[i]
            if cls == 'draw':
                # inline dash settings from Inkscape would override the animation
                style = re.sub(r'stroke-dash(array|offset):[^;]*;?', '', el.get('style', ''))
                el.set('style', f'{style.rstrip(";")};animation-delay:{delay}s'.lstrip(';'))
                el.set('class', 'draw')
                continue
            if el.get('class') == 'pop':
                del el.attrib['class']
            parent = space if i == 'text27-4-8-7-6-6-2-3-2-3-5-8-2-1-4-8-6' else root
            wrap = ET.Element(q('g'), {'class': 'pop', 'style': f'animation-delay:{delay}s'})
            if parent is space:
                space.append(wrap)
            else:
                parent.insert(list(parent).index(el), wrap)
            root.remove(el)
            wrap.append(el)

    tree.write(OUT, encoding='utf-8', xml_declaration=True)
    print(f'wrote {OUT} ({OUT.stat().st_size // 1024} KB)')


if __name__ == '__main__':
    main()
