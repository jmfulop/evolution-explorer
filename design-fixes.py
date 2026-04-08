import subprocess

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── FIX 1: Onboarding hint ──────────────────────────────────────────
# Add animated hint above node-count
html = html.replace(
    '  <div id="node-count"></div>',
    '''  <div id="node-count"></div>
  <div id="hint" style="position:absolute;bottom:24px;left:50%;transform:translateX(-50%);z-index:6;display:flex;align-items:center;gap:10px;background:rgba(0,0,0,.55);border:1px solid rgba(255,255,255,.12);border-radius:24px;padding:8px 20px;pointer-events:none;transition:opacity 1s ease">
    <span style="font-size:11px;color:rgba(255,255,255,.6);letter-spacing:.5px;white-space:nowrap">Drag to rotate</span>
    <span style="width:1px;height:12px;background:rgba(255,255,255,.2)"></span>
    <span style="font-size:11px;color:rgba(255,255,255,.6);letter-spacing:.5px;white-space:nowrap">Click a node to explore</span>
  </div>'''
)

# Fade hint out after 5 seconds, hide on first click
html = html.replace(
    'window.toggleAbout=function(){',
    '''// Fade hint after 5s
setTimeout(()=>{
  const h=document.getElementById('hint');
  if(h){h.style.opacity='0';setTimeout(()=>{if(h)h.style.display='none';},1000);}
},5000);
// Hide hint on first interaction
app.addEventListener('mousedown',()=>{
  const h=document.getElementById('hint');
  if(h){h.style.opacity='0';setTimeout(()=>{if(h)h.style.display='none';},500);}
},{once:true});

window.toggleAbout=function(){'''
)

# ── FIX 2: About panel - don't auto-open, just pulse ───────────────
html = html.replace(
    "// Auto-open on first visit\nif(true||!localStorage.getItem('evo-visited')){\n  setTimeout(()=>{\n    aboutOpen=true;\n    document.getElementById('about').style.transform='translateX(0%)';\n    const btn=document.getElementById('about-btn');\n    btn.style.background='rgba(255,255,255,.14)';\n    btn.style.color='#fff';\n    btn.style.borderColor='rgba(255,255,255,.5)';\n    btn.style.animation='none';\n  },3200);\n  localStorage.setItem('evo-visited','1');\n}",
    "// Pulse the about button to draw attention - don't auto-open\n// Button already has pulse-about animation from CSS"
)

# ── FIX 3: Brighter filter buttons ─────────────────────────────────
# Brighter inactive state
html = html.replace(
    "'padding:6px 18px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:.5px;cursor:pointer;border:1.5px solid rgba(255,255,255,.4);background:rgba(255,255,255,.07);color:rgba(255,255,255,.85);transition:all .18s;white-space:nowrap'",
    "'padding:6px 18px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:.5px;cursor:pointer;border:1.5px solid rgba(255,255,255,.55);background:rgba(255,255,255,.1);color:#fff;transition:all .18s;white-space:nowrap'"
)
# Brighter inactive coloured buttons
html = html.replace(
    "'padding:6px 18px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:.5px;cursor:pointer;border:1.5px solid '+col.css+'99;background:'+col.css+'1a;color:'+col.css+';transition:all .18s;white-space:nowrap'",
    "'padding:6px 18px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:.5px;cursor:pointer;border:1.5px solid '+col.css+'cc;background:'+col.css+'28;color:'+col.css+';transition:all .18s;white-space:nowrap'"
)
# Brighter inactive state in setFilter
html = html.replace(
    "else if(col){btn.style.background=col.css+'1a';btn.style.borderColor=col.css+'99';btn.style.color=col.css;btn.style.boxShadow='none';}",
    "else if(col){btn.style.background=col.css+'28';btn.style.borderColor=col.css+'cc';btn.style.color=col.css;btn.style.boxShadow='none';}"
)
html = html.replace(
    "else{btn.style.background='rgba(255,255,255,.07)';btn.style.borderColor='rgba(255,255,255,.4)';btn.style.color='rgba(255,255,255,.85)';btn.style.boxShadow='none';}",
    "else{btn.style.background='rgba(255,255,255,.1)';btn.style.borderColor='rgba(255,255,255,.55)';btn.style.color='#fff';btn.style.boxShadow='none';}"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("All 3 design fixes applied")
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'design: hint pill, about pulse only, brighter filters'])
subprocess.run(['git', 'push'])
print("Done - wait 30s then refresh")