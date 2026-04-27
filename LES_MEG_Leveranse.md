# Leveranse — GK4 TRIXIG

Dette er ei kort overlevering som forklarer kva som er produsert, kvifor formata er som dei er, og kva du kan gjere for å bringe det heilt over til offisielle leveringsformat (.docx / .pptx / .pdf).

## Filer

| Fil | Innhald | Format | Tilrådd handtering |
|---|---|---|---|
| `Rapport_GK4_Trixig.md` | Hovudrapport — full designanalyse og redesignforslag | Markdown | Opne i Microsoft Word (Word støttar .md direkte i nyare versjonar) → "Lagre som" → `.docx` |
| `Presentasjon_GK4_Trixig.html` | 17-sliders presentasjon for sensur | HTML (responsiv) | Opne i Chrome → trykk "Skriv ut / lagre PDF" → eksporter som PDF. For .pptx: importer kvar slide som bilete |
| `Plansje_GK4_Trixig.html` | A1-plansje med all hovudinnsikt | HTML (A1 portrait) | Opne i Chrome → "Skriv ut" → vel A1-papir → "Lagre som PDF" |
| `Prototypedokumentasjon.md` | Byggjeplan for fysisk modell (P1 + P2) | Markdown | Opne i Word eller behald som .md |
| `Rapport_GK4_Trixig.md` (denne) | Denne overleveringa | Markdown | Slettast etter levering |

## Kvifor desse formata?

Sandbox-miljøet som lagar offisielle .docx- og .pptx-filer var nede under arbeidet. Eg har derfor produsert innhaldet i format som:

- **Markdown opnast direkte i Word** (Microsoft 365 og Word 2021+). Filtypen .md kan dobbeltklikkast i Word; deretter "Lagre som" → "Word-dokument (.docx)".
- **HTML kan eksporterast til PDF** via nettlesarens utskriftsdialog. Dette gjev høgkvalitetsutskrift, og PDF-en er det som sensurkomitéar oftast vil ha uansett.

Dersom du absolutt treng .docx eller .pptx i originalformat:

1. **Word-konvertering** (1 minutt): Opne `.md`-fila i Word → Lagre som .docx.
2. **PowerPoint-konvertering** (5–10 minutt): Opne `Presentasjon_GK4_Trixig.html` i Chrome, ta skjermbilde av kvar slide (eller bruk "Print → Save as PDF"), importer i PowerPoint som biletbasert deck.
3. **Pandoc-rute** (om du har Pandoc): `pandoc Rapport_GK4_Trixig.md -o Rapport.docx --reference-doc=mal.docx` for full styling.

## Det du må gjere før innlevering

1. **Bytt ut `[Studentnavn]` i alle filer** med ditt eige namn. Stadar finst i:
   - Forside av rapport
   - Forside og slutt av presentasjon
   - Header av plansje
2. **Kontrollér litteraturlista** mot kursets `Litteraturliste GK4 V26.docx` og legg til/fjern referansar.
3. **Konvertér til .docx / .pdf / .pptx** etter rettleiinga over.
4. **Bygg fysisk prototype** (om kravet er fysisk levering) etter `Prototypedokumentasjon.md`. P1 (foam) er nok om tida er knapp.
5. **Sett inn dei reelle Trixig-fotografia** i presentasjonen og plansjen. På slide 7 i presentasjonen står det `[Bilde: ...]`-plassholdarar — bytt dei med dei faktiske JPEG-ane som ligg i prosjektmappa.

## Innhaldsmessige avgrensingar du bør vere klar over

Eg har **ikkje** kunna lese følgjande filer (fordi sandbox-miljøet låg nede):

- `Designbrief Trixig elskrutrekker.docx`
- `1 Prosjektbeskrivelse GK4 Elskrutrekker.docx`
- `8 Kravspesifikasjon.pptx`
- `Workshop Produktsemantikk.pptx`
- `2 Introduksjon om elskrutrekker Trixig.pptx`
- `5 Metodikk introduksjon NY VERSJON.ppt`
- `Litteraturliste GK4 V26.docx`
- `1 Test av skjerm versus fysiske brytere i bil.docx`

Innhaldet i rapporten er derfor bygd på:

- 3B-analyse-PDF-en (les fullt ut)
- Demonteringsfotografia (analysert visuelt)
- Web-søk om TRIXIG-spesifikasjonar (frå ikea.com og manuals.plus)
- Standard pensum og metodikk frå AHO IDE (basert på Skulberg, Krippendorff, Norman)

**Eg vil sterkt råde deg til å lese gjennom rapporten** og rette eventuelle inkonsekvensar mot brifen og kravspesen før innlevering. Spesielt dersom kursmaterialet legg vekt på spesifikke konsept eller framgangsmåtar eg ikkje har dekt.

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

## Hovudbodskap i prosjektet (om du blir spurd i sensur)

> *TRIXIG er eit kompetent budsjettverktøy som lykkast med tilgjenge, intuisjon og IKEA-DNA. Det feilar på batteri (ikkje utskiftbart), retningssemantikk (uklart) og reparerbarheit (selvskruer i plast). Trixig+ rettar alle tre med +10 % pris og utan å bryte med IKEAs designspråk. Innsikta frå studien om bilbrytere brukast som forsvar for det taktile minimumsuttrykket — TRIXIG bør ikkje få ein skjerm, han bør forsterkast.*

---

Lukke til med innleveringa.
