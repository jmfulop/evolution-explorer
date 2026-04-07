import re, subprocess

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Wider canvas for more elegant proportions
html = html.replace(
    '<canvas id="loader-c" width="60" height="120"',
    '<canvas id="loader-c" width="80" height="160"'
)

# 2. Replace the loader animation block with refined version
old_anim_start = "const loaderC=document.getElementById('loader-c');"
old_anim_end   = "loaderT+=0.06;\n},30);"

new_anim = """const loaderC=document.getElementById('loader-c');
const lctx=loaderC.getContext('2d');
let loaderT=0;
const loaderAnim=setInterval(()=>{
  lctx.clearRect(0,0,80,160);
  const steps=60,cx=40,r=15;
  for(let i=0;i<=steps;i++){
    const t=(i/steps)*Math.PI*5+loaderT,y=i*(160/steps);
    const x1=cx+r*Math.cos(t),x2=cx+r*Math.cos(t+Math.PI);
    const a=(Math.cos(t)+1)/2;
    if(i<steps){
      const nt=((i+1)/steps)*Math.PI*5+loaderT,ny=(i+1)*(160/steps);
      const nx1=cx+r*Math.cos(nt),nx2=cx+r*Math.cos(nt+Math.PI);
      lctx.beginPath();lctx.moveTo(x1,y);lctx.lineTo(nx1,ny);
      lctx.strokeStyle=`rgba(29,158,117,${(0.3+a*0.5).toFixed(2)})`;
      lctx.lineWidth=0.9;lctx.stroke();
      lctx.beginPath();lctx.moveTo(x2,y);lctx.lineTo(nx2,ny);
      lctx.strokeStyle=`rgba(127,119,221,${(0.3+(1-a)*0.5).toFixed(2)})`;
      lctx.lineWidth=0.9;lctx.stroke();
    }
    if(i%5===0){
      lctx.beginPath();lctx.moveTo(x1,y);lctx.lineTo(x2,y);
      lctx.strokeStyle='rgba(255,255,255,0.07)';lctx.lineWidth=0.4;lctx.stroke();
      lctx.beginPath();lctx.arc(x1,y,1.4,0,Math.PI*2);
      lctx.fillStyle=`rgba(29,158,117,${(0.6+a*0.4).toFixed(2)})`;lctx.fill();
      lctx.beginPath();lctx.arc(x2,y,1.4,0,Math.PI*2);
      lctx.fillStyle=`rgba(127,119,221,${(0.6+(1-a)*0.4).toFixed(2)})`;lctx.fill();
    }
  }
  loaderT+=0.04;
},30);"""

start_idx = html.find(old_anim_start)
end_idx   = html.find(old_anim_end) + len(old_anim_end)

if start_idx == -1:
    print("ERROR: Could not find loader animation block")
else:
    html = html[:start_idx] + new_anim + html[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done - loader refined")
    subprocess.run(['git','add','.'])
    subprocess.run(['git','commit','-m','feat: refined loader helix - elegant thin lines'])
    subprocess.run(['git','push'])
    print("Pushed - wait 30s then refresh")