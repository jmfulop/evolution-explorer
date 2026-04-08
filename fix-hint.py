import subprocess

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 1: Raise hint z-index above everything, center it better
html = html.replace(
    '  <div id="hint" style="position:absolute;bottom:24px;left:50%;transform:translateX(-50%);z-index:6;display:flex;align-items:center;gap:10px;background:rgba(0,0,0,.55);border:1px solid rgba(255,255,255,.12);border-radius:24px;padding:8px 20px;pointer-events:none;transition:opacity 1s ease">',
    '  <div id="hint" style="position:absolute;bottom:32px;left:50%;transform:translateX(-50%);z-index:25;display:flex;align-items:center;gap:10px;background:rgba(0,0,0,.7);border:1px solid rgba(255,255,255,.22);border-radius:24px;padding:10px 22px;pointer-events:none;transition:opacity 1s ease">'
)

# Fix 2: Remove the mousedown listener that hides it immediately
# and increase fade time to 8 seconds so it's visible longer
html = html.replace(
    '''// Fade hint after 5s
setTimeout(()=>{
  const h=document.getElementById('hint');
  if(h){h.style.opacity='0';setTimeout(()=>{if(h)h.style.display='none';},1000);}
},5000);
// Hide hint on first interaction
app.addEventListener('mousedown',()=>{
  const h=document.getElementById('hint');
  if(h){h.style.opacity='0';setTimeout(()=>{if(h)h.style.display='none';},500);}
},{once:true});''',
    '''// Fade hint after 8s
setTimeout(()=>{
  const h=document.getElementById('hint');
  if(h){h.style.opacity='0';setTimeout(()=>{if(h)h.style.display='none';},1000);}
},8000);'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Hint pill fixed")
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'fix: hint pill z-index and visibility'])
subprocess.run(['git', 'push'])
print("Done - wait 30s then refresh")