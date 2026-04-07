# Add loading screen back with global scope fix
(Get-Content index.html -Raw) -replace `
  '  <div id="topbar">', `
  '  <div id="loader" style="position:absolute;inset:0;z-index:200;background:#000408;display:flex;flex-direction:column;align-items:center;justify-content:center;transition:opacity .8s ease;pointer-events:all">
    <canvas id="loader-c" width="60" height="120" style="margin-bottom:28px"></canvas>
    <div style="font-size:11px;letter-spacing:4px;text-transform:uppercase;color:rgba(255,255,255,.35);margin-bottom:10px">Initialising</div>
    <div style="font-size:22px;font-weight:700;color:#fff;letter-spacing:.5px;margin-bottom:6px">Human Evolution Explorer</div>
    <div style="font-size:10px;letter-spacing:3px;text-transform:uppercase;color:rgba(255,255,255,.3)">85 million years of history</div>
    <div style="margin-top:28px;width:180px;height:1px;background:rgba(255,255,255,.08);position:relative;overflow:hidden">
      <div style="position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,#1D9E75,#7F77DD,transparent);animation:slide 1.4s ease-in-out infinite"></div>
    </div>
  </div>
  <style>@keyframes slide{0%{left:-100%}100%{left:100%}}</style>

  <div id="topbar">' |
Set-Content index.html -Encoding UTF8

# Add loader JS before the closing }); of DOMContentLoaded
(Get-Content index.html -Raw) -replace `
  'window\.toggleAbout=function\(\)\{', `
  'const loaderC=document.getElementById(''loader-c'');
const lctx=loaderC.getContext(''2d'');
let loaderT=0;
const loaderAnim=setInterval(()=>{
  lctx.clearRect(0,0,60,120);
  for(let i=0;i<=24;i++){
    const t=(i/24)*Math.PI*4+loaderT,y=i*(120/24);
    const x1=30+18*Math.cos(t),x2=30+18*Math.cos(t+Math.PI);
    const a=Math.abs(Math.cos(t));
    lctx.beginPath();lctx.arc(x1,y,2.5,0,Math.PI*2);lctx.fillStyle=''rgba(29,158,117,''+(0.4+a*0.6)+'')'' ;lctx.fill();
    lctx.beginPath();lctx.arc(x2,y,2.5,0,Math.PI*2);lctx.fillStyle=''rgba(127,119,221,''+(0.4+(1-a)*0.6)+'')'' ;lctx.fill();
    if(i<24){
      const nt=((i+1)/24)*Math.PI*4+loaderT,ny=(i+1)*(120/24);
      const nx1=30+18*Math.cos(nt),nx2=30+18*Math.cos(nt+Math.PI);
      lctx.beginPath();lctx.moveTo(x1,y);lctx.lineTo(nx1,ny);lctx.strokeStyle=''rgba(29,158,117,.3)'';lctx.lineWidth=1;lctx.stroke();
      lctx.beginPath();lctx.moveTo(x2,y);lctx.lineTo(nx2,ny);lctx.strokeStyle=''rgba(127,119,221,.25)'';lctx.lineWidth=1;lctx.stroke();
    }
    if(i%4===0){lctx.beginPath();lctx.moveTo(x1,y);lctx.lineTo(x2,y);lctx.strokeStyle=''rgba(255,255,255,.12)'';lctx.lineWidth=.8;lctx.stroke();}
  }
  loaderT+=0.06;
},30);
window.hideLoader=function(){
  const l=document.getElementById(''loader'');
  l.style.opacity=''0'';
  l.style.pointerEvents=''none'';
  setTimeout(()=>{l.remove();clearInterval(loaderAnim);},900);
};
setTimeout(window.hideLoader,2800);

window.toggleAbout=function(){' |
Set-Content index.html -Encoding UTF8

Write-Host "Loader added" -ForegroundColor Green
git add .
git commit -m "feat: loading screen back with correct global scope"
git push
Write-Host "Done - wait 30s then refresh" -ForegroundColor Cyan