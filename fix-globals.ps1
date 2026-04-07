# Fix: expose functions to global scope so onclick attributes can find them
(Get-Content index.html -Raw) -replace `
  'function toggleAbout\(\)\{', `
  'window.toggleAbout=function(){' -replace `
  'function closeInfo\(\)\{', `
  'window.closeInfo=function(){' -replace `
  'function navNode\(dir\)\{', `
  'window.navNode=function(dir){' |
Set-Content index.html -Encoding UTF8

Write-Host "Fixed" -ForegroundColor Green
git add .
git commit -m "fix: expose toggleAbout closeInfo navNode to global scope"
git push
Write-Host "Done - wait 30s then refresh" -ForegroundColor Cyan