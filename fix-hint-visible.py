import subprocess

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 1: app has overflow:hidden which clips the hint
# Change to overflow:visible
html = html.replace(
    '#app{position:relative;width:100%;height:100vh;overflow:hidden;cursor:grab;user-select:none}',
    '#app{position:relative;width:100%;height:100vh;overflow:visible;cursor:grab;user-select:none}'
)

# Fix 2: hint starts hidden because loader covers it - start with opacity 0
# then fade IN after loader disappears (at 3s), then fade out at 10s
html = html.replace(
    '  <div id="hint" style="position:absolute;bottom:32px;left:50%;transform:translateX(-50%);z-index:25;display:flex;align-items:center;gap:10px;background:rgba(0,0,0,.7);border:1px solid rgba(255,255,255,.22);border-radius:24px;padding:10px 22px;pointer-events:none;transition:opacity 1s ease">',
    '  <div id="hint" style="position:absolute;bottom:32px;left:50%;transform:translateX(-50%);z-index:25;opacity:0;display:flex;align-items:center;gap:10px;background:rgba(0,0,0,.75);border:1px solid rgba(255,255,255,.28);border-radius:24px;padding:10px 22px;pointer-events:none;transition:opacity 1s ease">'
)

# Fix 3: replace the fade-out timer with fade-in then fade-out
html = html.replace(
    '''// Fade hint after 8s
setTimeout(()=>{
  const h=document.getElementById('hint');
  if(h){h.style.opacity='0';setTimeout(()=>{if(h)h.style.display='none';},1000);}
},8000);''',
    '''// Fade hint IN after loader gone (3.2s), then fade OUT after 8s
setTimeout(()=>{
  const h=document.getElementById('hint');
  if(h){h.style.opacity='1';}
  setTimeout(()=>{
    if(h){h.style.opacity='0';setTimeout(()=>{if(h)h.remove();},1000);}
  },8000);
},3400);'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Hint visibility fixed")
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'fix: hint fades in after loader, overflow fix'])
subprocess.run(['git', 'push'])
print("Done - wait 30s then refresh")