# =====================================================================
#  push_to_github.ps1
#  Initialiserer git i denne mappa og pushar til
#  https://github.com/lukketsvane/GK4_TRIXIG
#
#  Kjør slik:
#    1) Høgreklikk fila → "Run with PowerShell"
#    eller:
#    2) Opne PowerShell, cd til mappa, og:
#         Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#         .\push_to_github.ps1
# =====================================================================

$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

Write-Host ""
Write-Host "=== Pushar GK4_TRIXIG til GitHub ===" -ForegroundColor Cyan
Write-Host ""

# Sjekk at git er installert
try {
    git --version | Out-Null
} catch {
    Write-Host "FEIL: git er ikkje installert eller ikkje på PATH." -ForegroundColor Red
    Write-Host "Last ned frå https://git-scm.com/download/win og prøv på nytt."
    Read-Host "Trykk Enter for å avslutte"
    exit 1
}

# Initialiser repo om det ikkje finst
if (-not (Test-Path ".git")) {
    Write-Host "Initialiserer nytt git-repo..." -ForegroundColor Yellow
    git init
    git branch -M main
} else {
    Write-Host "Git-repo finst allereie." -ForegroundColor Green
}

# Sett identitet om den ikkje er sett (lokalt for dette repoet)
$userName = git config user.name 2>$null
$userEmail = git config user.email 2>$null
if (-not $userName) {
    git config user.name "lukketsvane"
}
if (-not $userEmail) {
    git config user.email "iverfinne@gmail.com"
}

# Legg til remote om den ikkje finst
$remoteUrl = "https://github.com/lukketsvane/GK4_TRIXIG.git"
$existingRemote = git remote get-url origin 2>$null
if (-not $existingRemote) {
    Write-Host "Legg til origin -> $remoteUrl" -ForegroundColor Yellow
    git remote add origin $remoteUrl
} elseif ($existingRemote -ne $remoteUrl) {
    Write-Host "Oppdaterer origin frå $existingRemote til $remoteUrl" -ForegroundColor Yellow
    git remote set-url origin $remoteUrl
} else {
    Write-Host "Origin er allereie satt riktig." -ForegroundColor Green
}

# Stage alt
Write-Host ""
Write-Host "Stagar filer..." -ForegroundColor Yellow
git add -A

# Sjekk om det er noko å commite
$status = git status --porcelain
if (-not $status) {
    Write-Host "Ingenting å committe — arbeidstreet er reint." -ForegroundColor Green
} else {
    Write-Host "Committar..." -ForegroundColor Yellow
    git commit -m "GK4 Trixig: rapport, presentasjon, plansje, prototype-dokumentasjon, CAD"
}

# Push
Write-Host ""
Write-Host "Pushar til GitHub..." -ForegroundColor Yellow
Write-Host "(Du kan bli beden om å autentisere — bruk GitHub-token eller GitHub Desktop si auth.)" -ForegroundColor DarkGray
git push -u origin main

Write-Host ""
Write-Host "=== Ferdig ===" -ForegroundColor Green
Write-Host "Sjå https://github.com/lukketsvane/GK4_TRIXIG" -ForegroundColor Cyan
Write-Host ""
Read-Host "Trykk Enter for å lukke"
