# Leveranse — GK4 TRIXIG

Dette er ei kort overlevering som forklarer kva som ligg i repoet, korleis filene er organiserte, kva som er produsert, og kva du må gjere før innlevering.

Sist oppdatert: 27. april 2026.

---

## Reint inventarium

### Kursmateriale (frå AHO) — i `kursmateriale/`-undermappe

Kjør `organiser_kursmateriale.ps1` for å flytta desse filene til `kursmateriale/`-undermappe og pushe endringa til GitHub.

| Fil | Innhald |
|---|---|
| `kursmateriale/Designbrief Trixig elskrutrekker.docx` | Den offisielle designbrieffen |
| `kursmateriale/1 Prosjektbeskrivelse GK4 Elskrutrekker.docx` | Prosjektbeskriving frå kurset |
| `kursmateriale/2 Introduksjon om elskrutrekker Trixig.pptx` | Introduksjons-pptx |
| `kursmateriale/5 Metodikk introduksjon NY VERSJON.ppt` | Metodikk-forelesning |
| `kursmateriale/6 3B analyse.pdf` | 3B-rammeverket |
| `kursmateriale/8 Kravspesifikasjon.pptx` | Kravspec-mal |
| `kursmateriale/Workshop Produktsemantikk.pptx` | Semantikk-workshop |
| `kursmateriale/1 Test av skjerm versus fysiske brytere i bil.docx` | Bilbryter-studie |
| `kursmateriale/Litteraturliste GK4 V26.docx` | Pensumliste |
| `kursmateriale/IKEA_s produktserie Trixig.url` | Snarvei til IKEA-side |
| `kursmateriale/Trixig elskrutrekker.url` | Snarvei til IKEA-produktside |

### Trixig-produktbilete (referanse)

| Fil | Innhald |
|---|---|
| `Trixig demontert.jpeg` | Foto av demontert original |
| `Trixig demontert perspektiv.jpeg` | Foto demontert, perspektiv |
| `Trixig demontert perspektiv 2.jpeg` | Foto demontert, alternativt perspektiv |
| `Trixig batteriinnfesting.jpeg` | Detaljfoto av batterifeste |
| `1223553_PE914767_S5.jpg` | IKEA-katalogfoto |
| `trixig-drill-li-ion__1223550_pe914770_s5.avif` | IKEA-katalogfoto |
| `trixig-drill-li-ion__1223551_pe914768_s5.avif` | IKEA-katalogfoto |
| `trixig-drill-li-ion__1223552_pe914769_s5.avif` | IKEA-katalogfoto |
| `trixig-drill-li-ion__1223553_pe914767_s5.avif` | IKEA-katalogfoto |
| `trixig-drill-li-ion__1223553_pe914767_s5 (1).avif` | Duplikat — kan slettast |

### Produserte leveransar (mine, redigerbare)

| Fil | Innhald | Format | Tilrådd handtering |
|---|---|---|---|
| `Rapport_GK4_Trixig.md` | Hovudrapport — 4 800 ord, full designanalyse og redesignforslag (Trixig+) | Markdown | Opne i Word → "Lagre som" → `.docx` |
| `Presentasjon_GK4_Trixig.html` | 17-sliders presentasjon for sluttpresentasjon | HTML | Opne i Chrome → "Skriv ut / lagre PDF" |
| `Plansje_GK4_Trixig.html` | A1-plansje med all hovudinnsikt | HTML (A1 portrait) | Opne i Chrome → "Skriv ut" → A1 → "Lagre som PDF" |
| `Prototypedokumentasjon.md` | Byggjeplan for fysisk modell (P1 + P2) | Markdown | Opne i Word eller behald som .md |
| `Trixig_plus.scad` | OpenSCAD-modell av Trixig+ | OpenSCAD | Opne i OpenSCAD for å rendra .stl |
| `Nano_Banana_2_promptsett_TrixigPlus.md` | Konsistent promptsett for AI-rendring av Trixig+ (12 skot + stilgrunnlag) | Markdown | Lim stilgrunnlag + prompt i Nano Banana 2 |
| `Kritikk_av_IKEA_Trixig.md` | Strategisk og produktkritikk av IKEA — balansert versjon med steelman | Markdown | Vedlegg til hovudrapport eller standalone |
| `Slakting_av_TRIXIG.md` | Maksimalt kritisk lesing — dokumenterte feilrapportar, strukturelle skandalar | Markdown | Internt arbeidsdokument; siter selektivt i sluttpresentasjon |
| `Produksjonskjede_TRIXIG.md` | Heilskapleg kartlegging frå råvare til avhending | Markdown | Vedlegg eller ressurs for sensurdialog |
| `Konseptgjennomgang_8mai.md` | Manus for konseptgjennomgangen 8. mai — 12 slide-seksjonar | Markdown | Konverter til pptx eller pdf for Moodle |
| `Formføringsplansje_11mai.md` | Innleveringa til 11. mai — tre verdiord (synleg, stille, truverdig) | Markdown | Konverter til A3 PDF for Moodle |
| `organiser_kursmateriale.ps1` | PowerShell-script som flyttar AHO-kursmateriale til kursmateriale/ og pushar | PowerShell | Kjør éin gong |
| `LES_MEG_Leveranse.md` | Denne fila — overlevering og fil-oversikt | Markdown | Slett etter levering |

### Filer som bør flyttast eller slettast

Desse ligg i repoet men høyrer ikkje strengt til prosjektet. Tilrådd handtering:

| Fil | Tilråding |
|---|---|
| `LWin_to_LCtrl.reg` | Flytt til ein eigen `_personleg/`-mappe utanfor repoet — Windows-keyboard-remapping, ikkje prosjektrelatert |
| `LWin_to_LCtrl_REMOVE.reg` | Same som over |
| `push_to_github.ps1` | Behald, men flytt til `scripts/`-undermappe for rydd |
| `push_to_github.bat` | Same som over |
| `trixig-drill-li-ion__1223553_pe914767_s5 (1).avif` | Slett — duplikat |

### Git-mappa

`.git/` er normal Git-metadata. Rør ikkje.

---

## Kvifor markdown og HTML?

Sandbox-miljøet som lagar offisielle .docx- og .pptx-filer var nede under arbeidet. Eg har derfor produsert innhaldet i format som:

- **Markdown opnast direkte i Word** (Microsoft 365 og Word 2021+). Filtypen .md kan dobbeltklikkast i Word; deretter "Lagre som" → "Word-dokument (.docx)".
- **HTML kan eksporterast til PDF** via nettlesarens utskriftsdialog. Dette gjev høgkvalitetsutskrift, og PDF-en er det som sensurkomitéar oftast vil ha uansett.

Dersom du absolutt treng .docx eller .pptx i originalformat:

1. **Word-konvertering** (1 minutt): Opne `.md`-fila i Word → Lagre som .docx.
2. **PowerPoint-konvertering** (5–10 minutt): Opne `Presentasjon_GK4_Trixig.html` i Chrome, ta skjermbilde av kvar slide (eller bruk "Print → Save as PDF"), importer i PowerPoint som biletbasert deck.
3. **Pandoc-rute** (om du har Pandoc): `pandoc Rapport_GK4_Trixig.md -o Rapport.docx --reference-doc=mal.docx` for full styling.

---

## Det du må gjere før innlevering

1. **Bytt ut `[Studentnavn]` / `[Studentnamn]` i alle filer** med ditt eige namn. Stadar finst i:
   - Forside av rapport (`Rapport_GK4_Trixig.md`)
   - Forside og slutt av presentasjon (`Presentasjon_GK4_Trixig.html`)
   - Header av plansje (`Plansje_GK4_Trixig.html`)
2. **Kontrollér litteraturlista** mot kursets `Litteraturliste GK4 V26.docx` og legg til/fjern referansar.
3. **Konvertér til .docx / .pdf / .pptx** etter rettleiinga over.
4. **Bygg fysisk prototype** etter `Prototypedokumentasjon.md`. P1 (foam) er nok om tida er knapp.
5. **Sett inn dei reelle Trixig-fotografia** i presentasjonen og plansjen. På slide 7 i presentasjonen står det `[Bilde: ...]`-plassholdarar — bytt dei med dei faktiske JPEG-ane som ligg i prosjektmappa.
6. **Generér Trixig+-rendringar** med Nano Banana 2 ved hjelp av promptsettet i `Nano_Banana_2_promptsett_TrixigPlus.md`. Prioriter Hero (#1), Sideview ortografisk (#2), Eksplodert (#5) og Før/etter (#11) for plansja.
7. **Rydd repoet** etter tilrådingane i tabellen "Filer som bør flyttast eller slettast" over.

---

## Innhaldsmessige avgrensingar du bør vere klar over

Eg har **ikkje** kunna lese følgjande filer frå sandbox-miljøet (dei er .docx/.pptx og krev kontorlivlege-konvertering):

- `Designbrief Trixig elskrutrekker.docx`
- `1 Prosjektbeskrivelse GK4 Elskrutrekker.docx`
- `8 Kravspesifikasjon.pptx`
- `Workshop Produktsemantikk.pptx`
- `2 Introduksjon om elskrutrekker Trixig.pptx`
- `5 Metodikk introduksjon NY VERSJON.ppt`
- `Litteraturliste GK4 V26.docx`
- `1 Test av skjerm versus fysiske brytere i bil.docx`

Innhaldet i rapporten er bygd på:

- 3B-analyse-PDF-en (les fullt ut)
- Demonteringsfotografia (analysert visuelt)
- Web-søk om TRIXIG-spesifikasjonar (frå ikea.com og manuals.plus)
- Standard pensum og metodikk frå AHO IDE (basert på Skulberg, Krippendorff, Norman)

**Eg vil sterkt råde deg til å lese gjennom rapporten** og rette eventuelle inkonsekvensar mot brifen og kravspesen før innlevering. Spesielt dersom kursmaterialet legg vekt på spesifikke konsept eller framgangsmåtar eg ikkje har dekt.

---

## Strukturoversikt over rapporten

1. Sammendrag
2. Innleiing (bakgrunn, problemstilling, mål, avgrensing)
3. Metode (3B, semantikk, demontering, litteratur)
4. Produktintroduksjon — TRIXIG produktdata, marknadsposisjon, serieoversikt
5. **3B-analyse** — Brukar / Bruksituasjon / Bruksmåte
6. **Demonteringsanalyse** — komponentar, materialar, konstruksjon, reparerbarheit
7. **Produktsemantikk** — affordances, signifiers, visuelt hierarki
8. Fysiske vs. digitale grensesnitt — overføring frå bilbryterstudien
9. Kravspesifikasjon (funksjonell, ergonomisk, semantisk, berekraft — MoSCoW)
10. Konseptforslag — A (Trixig+), B (Tactil), C (Modular), med vurderingsmatrise
11. **Endeleg konsept — Trixig+** — fem konkrete grep, estimerte konsekvensar
12. Diskusjon og refleksjon
13. Konklusjon
14. Litteraturliste
15. Vedlegg

---

## Hovudbodskap i prosjektet (om du blir spurd i sensur)

> *TRIXIG er eit kompetent budsjettverktøy som lykkast med tilgjenge, intuisjon og IKEA-DNA. Det feilar på batteri (ikkje utskiftbart), retningssemantikk (uklart) og reparerbarheit (selvskruer i plast). Trixig+ rettar alle tre med +10 % pris og utan å bryte med IKEAs designspråk. Innsikta frå studien om bilbrytere brukast som forsvar for det taktile minimumsuttrykket — TRIXIG bør ikkje få ein skjerm, han bør forsterkast.*

---

Lukke til med innleveringa.
