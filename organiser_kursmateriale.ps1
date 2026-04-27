# =====================================================================
#  organiser_kursmateriale.ps1
#  Flyttar AHO-kursmaterialet til kursmateriale/-undermappe og pushar til
#  https://github.com/lukketsvane/GK4_TRIXIG
#
#  Kjør slik:
#    1) Høgreklikk fila → "Run with PowerShell"
#    eller:
#    2) Opne PowerShell, cd til mappa, og:
#         Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#         .\organiser_kursmateriale.ps1
# =====================================================================

$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

Write-Host ""
Write-Host "=== Organiserer GK4_TRIXIG og pushar ===" -ForegroundColor Cyan
Write-Host ""

# Sjekk git
try { git --version | Out-Null } catch {
    Write-Host "FEIL: git er ikkje installert eller ikkje på PATH." -ForegroundColor Red
    Read-Host "Trykk Enter for å avslutte"
    exit 1
}

# Sørg for at vi er i eit git-repo
if (-not (Test-Path ".git")) {
    Write-Host "FEIL: Dette er ikkje eit git-repo. Kjør push_to_github.ps1 først." -ForegroundColor Red
    Read-Host "Trykk Enter for å avslutte"
    exit 1
}

# Lag kursmateriale-mappa
$target = "kursmateriale"
if (-not (Test-Path $target)) {
    New-Item -ItemType Directory -Path $target | Out-Null
    Write-Host "Laga $target/" -ForegroundColor Green
} else {
    Write-Host "$target/ finst allereie." -ForegroundColor Green
}

# Filer som høyrer til AHO-kurset
$kursfiler = @(
    "Designbrief Trixig elskrutrekker.docx",
    "1 Prosjektbeskrivelse GK4 Elskrutrekker.docx",
    "2 Introduksjon om elskrutrekker Trixig.pptx",
    "5 Metodikk introduksjon NY VERSJON.ppt",
    "6 3B analyse.pdf",
    "8 Kravspesifikasjon.pptx",
    "Workshop Produktsemantikk.pptx",
    "1 Test av skjerm versus fysiske brytere i bil.docx",
    "Litteraturliste GK4 V26.docx",
    "IKEA_s produktserie Trixig.url",
    "Trixig elskrutrekker.url"
)

Write-Host ""
Write-Host "Flyttar kursfiler til $target/ ..." -ForegroundColor Yellow

$flytta = 0
$hoppa = 0
foreach ($f in $kursfiler) {
    if (Test-Path $f) {
        # Bruk git mv slik at flyttinga vert spora som ein flytting, ikkje som delete + add
        try {
            git mv -- "$f" "$target/" 2>$null
            Write-Host "  flytta: $f" -ForegroundColor DarkGreen
            $flytta++
        } catch {
            # Om git mv feilar (t.d. ikkje tracked enno), bruk vanleg flytt
            Move-Item -Path $f -Destination "$target/" -Force
            Write-Host "  flytta (utan git mv): $f" -ForegroundColor DarkYellow
            $flytta++
        }
    } else {
        Write-Host "  hoppa over (finst ikkje): $f" -ForegroundColor DarkGray
        $hoppa++
    }
}

Write-Host ""
Write-Host "Flytta $flytta fil(er). Hoppa over $hoppa." -ForegroundColor Cyan

# Stage alt (inkludert evt. Move-Item-baserte flytta filer som ikkje er sporra av git mv)
git add -A

# Status
$status = git status --porcelain
if (-not $status) {
    Write-Host ""
    Write-Host "Ingenting å committe — arbeidstreet er reint." -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "Committar..." -ForegroundColor Yellow
    git commit -m "Organiser: flytt AHO-kursmateriale til kursmateriale/-undermappe"
}

# Push
Write-Host ""
Write-Host "Pushar til GitHub..." -ForegroundColor Yellow
Write-Host "(Du kan bli beden om å autentisere — bruk GitHub-token eller GitHub Desktop si auth.)" -ForegroundColor DarkGray
git push origin main

Write-Host ""
Write-Host "=== Ferdig ===" -ForegroundColor Green
Write-Host "Sjå https://github.com/lukketsvane/GK4_TRIXIG" -ForegroundColor Cyan
Write-Host ""
Read-Host "Trykk Enter for å lukke"
