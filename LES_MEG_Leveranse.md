# GK4 V26 Modul 2 — TRIXIG redesign

Repo for AHO-prosjektet: redesign av IKEA TRIXIG 3,6 V elektrisk skrutrekkar. Veke 18–22, 27. april–27. mai 2026.

Sist oppdatert: 27. april 2026.

---

## Snarvegar — kva skal eg sjå på?

| Du leitar etter | Opne |
|---|---|
| Hovudrapporten | [`Rapport_GK4_Trixig.md`](Rapport_GK4_Trixig.md) |
| Sluttpresentasjonen (17 slides) | [`Presentasjon_GK4_Trixig.html`](Presentasjon_GK4_Trixig.html) |
| A1-plansja | [`Plansje_GK4_Trixig.html`](Plansje_GK4_Trixig.html) |
| Konseptgjennomgang for fredag 8. mai | [`Konseptgjennomgang_8mai.md`](Konseptgjennomgang_8mai.md) |
| Formføringsplansje for måndag 11. mai | [`Formføringsplansje_11mai.md`](Formføringsplansje_11mai.md) |
| Prototype-byggjeplan | [`Prototypedokumentasjon.md`](Prototypedokumentasjon.md) |
| OpenSCAD-modell | [`Trixig_plus.scad`](Trixig_plus.scad) |

## Strategiske dokument (vedlegg / forsvar)

| Du leitar etter | Opne |
|---|---|
| Kritikk av IKEA — balansert versjon med steelman | [`Kritikk_av_IKEA_Trixig.md`](Kritikk_av_IKEA_Trixig.md) |
| Slakting av TRIXIG — maksimalt kritisk lesing | [`Slakting_av_TRIXIG.md`](Slakting_av_TRIXIG.md) |
| Produksjonskjeda frå råvare til avhending | [`Produksjonskjede_TRIXIG.md`](Produksjonskjede_TRIXIG.md) |
| Nano Banana 2 promptsett for Trixig+-rendringar | [`Nano_Banana_2_promptsett_TrixigPlus.md`](Nano_Banana_2_promptsett_TrixigPlus.md) |

---

## Mappestruktur

```
GK4_TRIXIG/
├── LES_MEG_Leveranse.md            ← du les denne
├── organiser_repo.ps1              ← master-script for opprydding
│
├── Rapport_GK4_Trixig.md           ← hovudrapport (~4800 ord)
├── Presentasjon_GK4_Trixig.html    ← 17-slide sluttpresentasjon
├── Plansje_GK4_Trixig.html         ← A1-plansje
├── Prototypedokumentasjon.md       ← P1 (foam) + P2 byggjeplan
├── Trixig_plus.scad                ← parametrisk OpenSCAD-modell
│
├── Kritikk_av_IKEA_Trixig.md       ← strategisk kritikk + steelman
├── Slakting_av_TRIXIG.md           ← maksimal kritikk, dokumentert
├── Produksjonskjede_TRIXIG.md      ← forsyningskjede-kartlegging
├── Konseptgjennomgang_8mai.md      ← 8. mai-leveranse
├── Formføringsplansje_11mai.md     ← 11. mai-leveranse
├── Nano_Banana_2_promptsett_TrixigPlus.md  ← AI-rendring-promptar
│
├── kursmateriale/                  ← AHO-kursfiler (designbrief, 3B, kravspec, …)
├── referanse/                      ← Trixig-foto (demontert + IKEA-katalog)
├── scripts/                        ← push_to_github + organiser_kursmateriale
└── _arkiv/                         ← ikkje-prosjekt-filer
```

For å oppretta denne strukturen frå rotmappa: kjør `organiser_repo.ps1`. Han er idempotent — trygg å kjøra fleire gonger.

---

## Tidslinje og leveransar

| Dato | Leveranse | Fil(er) |
|---|---|---|
| **8. mai kl. 20:00** | Konseptgjennomgang Moodle | `Konseptgjennomgang_8mai.md` → eksporter til pdf/pptx |
| **11. mai kl. 09:00** | Formføringsplansje Moodle | `Formføringsplansje_11mai.md` → eksporter til A3 pdf |
| **25. mai kl. 20:00** | Sluttpresentasjon Moodle | `Presentasjon_GK4_Trixig.html` → eksporter til pdf |
| **26.–27. mai** | Sluttpresentasjon + fysisk modell | Modell etter `Prototypedokumentasjon.md` |

---

## Konvertering markdown → docx/pptx/pdf

**Markdown → Word.** Microsoft Word 2021+ og Word for Microsoft 365 opnar `.md` direkte. Dobbelklikk fila → Word opnar → "Lagre som" → "Word-dokument (.docx)".

**HTML → PDF.** Opne fila i Chrome → Cmd/Ctrl-P → "Lagre som PDF". For A1-plansja: vel papirstørrelse A1 i utskriftsdialogen.

**Markdown → PowerPoint.** Enklaste rute: lim manuset frå `Konseptgjennomgang_8mai.md` slide-for-slide inn i ein eksisterande pptx-mal. Eventuelt køyr Pandoc lokalt:
```
pandoc Konseptgjennomgang_8mai.md -o Konseptgjennomgang.pptx
```

---

## Det du må gjere før innlevering

1. **Bytt ut `[Studentnamn]`** i alle filer med ditt eige namn. Søk i: `Rapport_GK4_Trixig.md`, `Presentasjon_GK4_Trixig.html`, `Plansje_GK4_Trixig.html`, alle nye `.md`-leveransar.
2. **Kontrollér litteraturlista** mot `kursmateriale/Litteraturliste GK4 V26.docx`.
3. **Konvertér markdown og HTML** til dei formata Moodle krev (sjå over).
4. **Bygg fysisk prototype** etter `Prototypedokumentasjon.md`.
5. **Sett inn referansebilete** i presentasjonen og plansja frå `referanse/`-mappa.
6. **Generér Trixig+-rendringar** med Nano Banana 2 etter promptsettet.
7. **Kjør `organiser_repo.ps1`** for å oppretta mappestruktur og pushe.

---

## Hovudbodskap (om du blir spurd i sensur)

> *TRIXIG er eit kompetent budsjettverktøy som lykkast med tilgjenge, intuisjon og IKEA-DNA. Det feilar på batteri (ikkje utskiftbart), retningssemantikk (uklart) og reparérbarheit (selvskruver i plast). Trixig+ rettar alle tre med +10 % pris og utan å bryte med IKEAs designspråk. Innsikta frå studien om bilbrytere brukast som forsvar for det taktile minimumsuttrykket — TRIXIG bør ikkje få ein skjerm, han bør forsterkast.*

EU-batteriforordninga 2023/1542 krev uansett at IKEA gjer dette innan februar 2027. Trixig+ er det IKEA uansett må byggja. Spørsmålet er om dei gjer det proaktivt eller under regulatorisk pålegg.

---

## Innhaldsmessige avgrensingar

Sandbox-miljøet kunne ikkje opna kursfilene i `kursmateriale/` (.docx/.pptx krev kontorlivlege). Innhaldet i rapporten er bygd på 3B-PDF-en, demonteringsfotografia, IKEAs offentlege spesifikasjonar, og standard pensum (Skulberg, Krippendorff, Norman). Eg vil sterkt råde deg til å lese gjennom rapporten og rette eventuelle inkonsekvensar mot brifen og kravspesen før innlevering.

---

Lukke til med innleveringa.
