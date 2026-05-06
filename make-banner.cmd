@echo off
setlocal

if "%~1"=="" (
  echo Usage: .\make-banner.cmd "C:\path\to\image.png" [width]
  echo Example: .\make-banner.cmd "C:\Users\acer\Pictures\poster.jpg" 90
  exit /b 1
)

set "WIDTH=%~2"
if "%WIDTH%"=="" set "WIDTH=90"

if not exist "%~dp0assets" mkdir "%~dp0assets"
"%USERPROFILE%\go\bin\ascii-image-converter.exe" "%~1" -W %WIDTH% --complex > "%~dp0assets\banner.txt"

echo Saved CLI banner to "%~dp0assets\banner.txt"
echo Preview it with:
echo   .\praedix.cmd --status --no-color
