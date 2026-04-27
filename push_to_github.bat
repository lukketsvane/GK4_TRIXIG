@echo off
REM =====================================================================
REM  push_to_github.bat — enkel variant for cmd.exe
REM  Dobbeltklikk for å pushe alt til https://github.com/lukketsvane/GK4_TRIXIG
REM =====================================================================

cd /d "%~dp0"

echo.
echo === Pushar GK4_TRIXIG til GitHub ===
echo.

where git >nul 2>nul
if errorlevel 1 (
    echo FEIL: git er ikkje installert. Last ned fra https://git-scm.com/download/win
    pause
    exit /b 1
)

if not exist ".git" (
    echo Initialiserer git-repo...
    git init
    git branch -M main
)

git config user.name >nul 2>nul || git config user.name "lukketsvane"
git config user.email >nul 2>nul || git config user.email "iverfinne@gmail.com"

git remote get-url origin >nul 2>nul
if errorlevel 1 (
    echo Legg til origin...
    git remote add origin https://github.com/lukketsvane/GK4_TRIXIG.git
) else (
    git remote set-url origin https://github.com/lukketsvane/GK4_TRIXIG.git
)

echo Stagar filer...
git add -A

echo Committar...
git commit -m "GK4 Trixig: rapport, presentasjon, plansje, prototype-dokumentasjon, CAD" 2>nul

echo Pushar...
git push -u origin main

echo.
echo === Ferdig ===
echo Sjå https://github.com/lukketsvane/GK4_TRIXIG
echo.
pause
