import subprocess

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove share button from topbar
html = html.replace(
    '<button id="share-btn" onclick="shareNode()" style="padding:5px 14px;border-radius:20px;font-size:10px;font-weight:600;letter-spacing:.8px;text-transform:uppercase;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.04);color:rgba(255,255,255,.4);cursor:pointer;transition:all .18s;flex-shrink:0;display:none">Share</button>\n      ',
    ''
)

# 2. Remove share toast
html = html.replace(
    '\n  <div id="share-toast" style="position:absolute;bottom:80px;left:50%;transform:translateX(-50%) translateY(20px);background:rgba(29,158,117,.95);color:#fff;font-size:12px;font-weight:600;padding:10px 20px;border-radius:24px;opacity:0;transition:all .3s ease;pointer-events:none;white-space:nowrap;z-index:50;letter-spacing:.3px">Link copied to clipboard</div>',
    ''
)

# 3. Remove share button show logic from selectNode
html = html.replace(
    """  document.getElementById('info').style.transform='translateY(0)';
  const sb=document.getElementById('share-btn');
  sb.style.display='block';
  sb.style.borderColor=col.css+'88';
  sb.style.color=col.css;""",
    "  document.getElementById('info').style.transform='translateY(0)';"
)

# 4. Remove share button hide logic from closeInfo
html = html.replace(
    """window.closeInfo=function(){
  const sb=document.getElementById('share-btn');
  sb.style.display='none';sb.style.borderColor='rgba(255,255,255,.18)';sb.style.color='rgba(255,255,255,.4)';""",
    "window.closeInfo=function(){"
)

# 5. Remove shareNode function
html = html.replace(
    """window.shareNode=function(){
  if(selIdx<0)return;
  const url=window.location.origin+window.location.pathname+'?node='+selIdx;
  navigator.clipboard.writeText(url).then(()=>{
    const t=document.getElementById('share-toast');
    t.style.opacity='1';t.style.transform='translateX(-50%) translateY(0)';
    setTimeout(()=>{t.style.opacity='0';t.style.transform='translateX(-50%) translateY(20px)';},2200);
  });
};

""",
    ''
)

# 6. Remove deep link param handler
html = html.replace(
    """\n// Deep link — open node from ?node=X in URL
const params=new URLSearchParams(window.location.search);
const nodeParam=params.get('node');
if(nodeParam!==null){
  const idx=parseInt(nodeParam);
  if(!isNaN(idx)&&idx>=0&&idx<EVT.length){
    setTimeout(()=>selectNode(idx),400);
  }
}""",
    ''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Share button removed")
subprocess.run(['git','add','.'])
subprocess.run(['git','commit','-m','revert: remove share button, restore about'])
subprocess.run(['git','push'])
print("Pushed - wait 30s then refresh")