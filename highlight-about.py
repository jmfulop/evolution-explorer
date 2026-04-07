import subprocess

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Make the About button visually prominent with a pulse animation
html = html.replace(
    '<button id="about-btn" onclick="toggleAbout()" style="padding:5px 14px;border-radius:20px;font-size:10px;font-weight:600;letter-spacing:.8px;text-transform:uppercase;border:1px solid rgba(255,255,255,.28);background:rgba(255,255,255,.06);color:rgba(255,255,255,.65);cursor:pointer;transition:all .18s;flex-shrink:0">About</button>',
    '<button id="about-btn" onclick="toggleAbout()" style="padding:6px 18px;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:.8px;text-transform:uppercase;border:1.5px solid #1D9E75;background:rgba(29,158,117,.15);color:#1D9E75;cursor:pointer;transition:all .18s;flex-shrink:0;animation:pulse-about 2s ease-in-out infinite">About</button>'
)

# 2. Add pulse keyframe to existing style block
html = html.replace(
    '@keyframes slide{0%{left:-100%}100%{left:100%}}',
    '@keyframes slide{0%{left:-100%}100%{left:100%}}\n    @keyframes pulse-about{0%,100%{box-shadow:0 0 0 0 rgba(29,158,117,.5)}50%{box-shadow:0 0 0 8px rgba(29,158,117,0)}}'
)

# 3. Auto-open About on first visit, stop pulse once opened
html = html.replace(
    'window.toggleAbout=function(){',
    '''// Auto-open on first visit
if(!localStorage.getItem('evo-visited')){
  setTimeout(()=>{
    aboutOpen=true;
    document.getElementById('about').style.transform='translateX(0%)';
    const btn=document.getElementById('about-btn');
    btn.style.background='rgba(255,255,255,.14)';
    btn.style.color='#fff';
    btn.style.borderColor='rgba(255,255,255,.5)';
    btn.style.animation='none';
  },3200);
  localStorage.setItem('evo-visited','1');
}

window.toggleAbout=function(){'''
)

# 4. Stop pulse animation when About is toggled open
html = html.replace(
    '''  document.getElementById('about').style.transform=aboutOpen?'translateX(0%)':'translateX(100%)';
  const btn=document.getElementById('about-btn');
  btn.style.background=aboutOpen?'rgba(255,255,255,.14)':'rgba(255,255,255,.06)';
  btn.style.color=aboutOpen?'#fff':'rgba(255,255,255,.65)';
  btn.style.borderColor=aboutOpen?'rgba(255,255,255,.5)':'rgba(255,255,255,.28)';''',
    '''  document.getElementById('about').style.transform=aboutOpen?'translateX(0%)':'translateX(100%)';
  const btn=document.getElementById('about-btn');
  btn.style.animation='none';
  btn.style.background=aboutOpen?'rgba(255,255,255,.14)':'rgba(255,255,255,.06)';
  btn.style.color=aboutOpen?'#fff':'rgba(255,255,255,.65)';
  btn.style.borderColor=aboutOpen?'rgba(255,255,255,.5)':'rgba(255,255,255,.28)';'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("About highlight added")
subprocess.run(['git','add','.'])
subprocess.run(['git','commit','-m','feat: about auto-opens on first visit, pulses to draw attention'])
subprocess.run(['git','push'])
print("Pushed - wait 30s then refresh")