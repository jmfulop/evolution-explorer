import subprocess

with open('index.html', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="hint"')
if idx == -1:
    print("HINT NOT FOUND - adding it now")
    # Add hint directly before closing </div> of app
    hint_html = '''  <div id="hint" style="position:absolute;bottom:32px;left:50%;transform:translateX(-50%);z-index:25;display:flex;align-items:center;gap:10px;background:rgba(0,0,0,.75);border:1px solid rgba(255,255,255,.25);border-radius:24px;padding:10px 22px;pointer-events:none;transition:opacity 1.2s ease">
    <span style="font-size:12px;font-weight:600;color:rgba(255,255,255,.85);letter-spacing:.5px;white-space:nowrap">Drag to rotate</span>
    <span style="width:1px;height:14px;background:rgba(255,255,255,.25)"></span>
    <span style="font-size:12px;font-weight:600;color:rgba(255,255,255,.85);letter-spacing:.5px;white-space:nowrap">Click a node to explore</span>
  </div>'''
    html = html.replace('  <div id="node-count"></div>\n</div>', '  <div id="node-count"></div>\n' + hint_html + '\n</div>')

    # Add fade JS before closing }); of DOMContentLoaded
    fade_js = '''// Fade hint after 8s
setTimeout(()=>{
  const h=document.getElementById('hint');
  if(h){h.style.opacity='0';setTimeout(()=>{if(h)h.remove();},1200);}
},8000);
'''
    html = html.replace('animate();\n});', 'animate();\n\n' + fade_js + '});')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Hint added successfully")
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'fix: add missing hint pill'])
    subprocess.run(['git', 'push'])
    print("Pushed - wait 30s then refresh")
else:
    print(f"Hint found at index {idx}")
    print(html[idx:idx+200])