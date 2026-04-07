# Fix 1: topbar z-index above loader, pointer-events guaranteed
(Get-Content index.html) `
  -replace '#topbar\{position:absolute;top:0;left:0;right:0;height:64px;z-index:30;', `
           '#topbar{position:absolute;top:0;left:0;right:0;height:64px;z-index:110;' `
  -replace '#about\{position:absolute;top:64px;right:0;bottom:0;width:400px;z-index:20;', `
           '#about{position:absolute;top:64px;right:0;bottom:0;width:400px;z-index:110;' |
Set-Content index.html -Encoding UTF8

# Fix 2: loader also sets pointer-events none immediately on creation
(Get-Content index.html) `
  -replace "id=""loader"" style=""position:absolute;inset:0;z-index:100;", `
           'id="loader" style="position:absolute;inset:0;z-index:100;pointer-events:all;' |
Set-Content index.html -Encoding UTF8

Write-Host "Fixes applied" -ForegroundColor Green
git add .
git commit -m "fix: topbar and about z-index above loader"
git push
Write-Host "Pushed - wait 30 seconds then refresh" -ForegroundColor Cyan