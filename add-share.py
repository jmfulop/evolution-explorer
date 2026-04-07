import subprocess

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add share button to topbar next to About
html = html.replace(
    '<button id="about-btn" onclick="toggleAbout()"',
    '<button id="share-btn" onclick="shareNode()" style="padding:5px 14px;border-radius:20px;font-size:10px;font-weight:600;letter-spacing:.8px;text-transform:uppercase;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.04);color:rgba(255,255,255,.4);cursor:pointer;transition:all .18s;flex-shrink:0;display:none">Share</button>\n      <button id="about-btn" onclick="toggleAbout()"'
)

# 2. Add share toast div before closing </div> of app
html = html.replace(
    '  <div id="node-count"></div>\n</div>',
    '''  <div id="node-count"></div>
  <div id="share-toast" style="position:absolute;bottom:80px;left:50%;transform:translateX(-50%) translateY(20px);background:rgba(29,158,117,.95);color:#fff;font-size:12px;font-weight:600;padding:10px 20px;border-radius:24px;opacity:0;transition:all .3s ease;pointer-events:none;white-space:nowrap;z-index:50;letter-spacing:.3px">Link copied to clipboard</div>
</div>'''
)

# 3. Add share logic — show button when node selected, hide when closed
html = html.replace(
    "  document.getElementById('info').style.transform='translateY(0)';",
    """  document.getElementById('info').style.transform='translateY(0)';
  const sb=document.getElementById('share-btn');
  sb.style.display='block';
  sb.style.borderColor=col.css+'88';
  sb.style.color=col.css;"""
)

html = html.replace(
    "window.closeInfo=function(){",
    """window.closeInfo=function(){
  const sb=document.getElementById('share-btn');
  sb.style.display='none';sb.style.borderColor='rgba(255,255,255,.18)';sb.style.color='rgba(255,255,255,.4)';"""
)

# 4. Add shareNode function after toggleAbout
html = html.replace(
    'window.toggleAbout=function(){',
    '''window.shareNode=function(){
  if(selIdx<0)return;
  const url=window.location.origin+window.location.pathname+'?node='+selIdx;
  navigator.clipboard.writeText(url).then(()=>{
    const t=document.getElementById('share-toast');
    t.style.opacity='1';t.style.transform='translateX(-50%) translateY(0)';
    setTimeout(()=>{t.style.opacity='0';t.style.transform='translateX(-50%) translateY(20px)';},2200);
  });
};

window.toggleAbout=function(){'''
)

# 5. Auto-open node from URL param on load — add after animate() call
html = html.replace(
    'animate();\n});',
    '''animate();

// Deep link — open node from ?node=X in URL
const params=new URLSearchParams(window.location.search);
const nodeParam=params.get('node');
if(nodeParam!==null){
  const idx=parseInt(nodeParam);
  if(!isNaN(idx)&&idx>=0&&idx<EVT.length){
    setTimeout(()=>selectNode(idx),400);
  }
}
});'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Share button added")
subprocess.run(['git','add','.'])
subprocess.run(['git','commit','-m','feat: share button with deep link to node'])
subprocess.run(['git','push'])
print("Pushed - wait 30s then refresh")