# Trixig-oppgåva: oversikt

Sist oppdatert 21. november 2026.

## Status no

- **Supplering:** plansja med tre konsept er ferdig, i A3 liggande:
  [`docs/deliverables/supplering_tre_konsept/plansje_tre_konsept_a3.pdf`](docs/deliverables/supplering_tre_konsept/plansje_tre_konsept_a3.pdf).
  Ho viser konsept A Trixig+, B Tactil og C Modular frå konseptgjennomgangen 8. mai. Trixig+ er markert som valt konsept.
- **Før innlevering:** legg inn namnet ditt. Det står ikkje på plansja fordi repoet er offentleg.
  Endre `plansje_tre_konsept.html` i same mappe, og lagre som PDF frå Chrome (A3 liggande, ingen marg, bakgrunnsgrafikk på).
- **Oppgåva frå lærarane** er samla i éin PDF med prosjektbeskrivinga og designbriefen:
  [`docs/course/00_samla_oppgaveskildring_og_designbrief.pdf`](docs/course/00_samla_oppgaveskildring_og_designbrief.pdf).

## Oppgåva

| | |
|---|---|
| Emne | 70-135 Å utforske design gjennom produkter, GK4 V26, modul 2: elektrisk skrutrekkar |
| Periode | 27. april til 27. mai 2026 (veke 18–22) |
| Modulansvarleg | Harald Skulberg |
| Oppdrag | Redesign av IKEA TRIXIG 3,6 V for marknadsintroduksjon i 2028 (simulert oppdrag frå IKEA) |
| Krav | Samla PDF: [`docs/course/00_samla_oppgaveskildring_og_designbrief.pdf`](docs/course/00_samla_oppgaveskildring_og_designbrief.pdf). Originalane: [`01_prosjektbeskrivelse_gk4_elskrutrekker.docx`](docs/course/01_prosjektbeskrivelse_gk4_elskrutrekker.docx) og [`designbrief_trixig_elskrutrekker.docx`](docs/course/designbrief_trixig_elskrutrekker.docx) |
| Valt konsept | A, Trixig+: same form, utskiftbar 18650-celle, Torx-skruer, asymmetrisk retningsbrytar og status-LED |

## Leveransar

| Frist (2026) | Krav i prosjektbeskrivinga | Filer | Merknad |
|---|---|---|---|
| 4. mai kl. 09 | Personleg debrief basert på designbriefen | [`docs/deliverables/personleg_debrief_trixig.pdf`](docs/deliverables/personleg_debrief_trixig.pdf) (20 s.), [`docs/deliverables/debrief_modul2_trixig.docx`](docs/deliverables/debrief_modul2_trixig.docx), [`docs/reports/personleg_debrief_trixig.docx`](docs/reports/personleg_debrief_trixig.docx) | Den reviderte utgåva (36 s., etter tilbakemelding frå modulansvarleg) ligg berre i Drive: `GK4_Trixig.pdf` |
| 8. mai kl. 20 | 3B-analyse, kravspec, valt berekraftshandling, bilete av 3 konsept og markering av valt konsept | [`docs/deliverables/08_mai_konseptgjennomgang/`](docs/deliverables/08_mai_konseptgjennomgang/) | Konsepta låg berre som tre separate bilete. Manus: [`docs/project/konseptgjennomgang_8mai.md`](docs/project/konseptgjennomgang_8mai.md) |
| **Supplering** | **Plansje for tre design** | [`docs/deliverables/supplering_tre_konsept/`](docs/deliverables/supplering_tre_konsept/) | **Ny, november 2026** |
| 11. mai kl. 09 | Formføringsplansje med 3 verdiord | [`docs/deliverables/11_mai_formforingsplansje/`](docs/deliverables/11_mai_formforingsplansje/) (2 bilete) | Tekst: [`docs/project/formfringsplansje_11mai.md`](docs/project/formfringsplansje_11mai.md). Verdiord: Synleg, Stille, Truverdig |
| 25. mai kl. 20 | Digital sluttpresentasjon og 3 bilete av den fysiske modellen | [`docs/deliverables/25_mai_sluttpresentasjon/`](docs/deliverables/25_mai_sluttpresentasjon/) (4 bilete) | Sjølve presentasjonen ligg ikkje i repoet. I Drive finst `TRIXIG_plus_endeleg_designbrief_18_sider.pdf` og `TRIXIG_OPEN_endeleg_designbrief.pdf` frå 26. mai; dei er ikkje gjennomgått enno |
| Veke 21 | CAD i Fusion 360 | [`cad/fusion/`](cad/fusion/), særleg `redesign_01/` (skal, delingslinje, skruer) | Print-filer i [`cad/print/trixig_redesign/`](cad/print/trixig_redesign/) |
| Løpande | Designdagbok | [`docs/project/designdagbok.md`](docs/project/designdagbok.md) | Berre 28. april er ført |

## Kvar ting ligg

### GitHub

- [`lukketsvane/GK4_TRIXIG`](https://github.com/lukketsvane/GK4_TRIXIG): prosjektarkivet (dette repoet).
- [`lukketsvane/trixig.iverfinne.no`](https://github.com/lukketsvane/trixig.iverfinne.no): nettstaden med 3D-galleri. Han viser originalen i røntgenvising (`public/assets/00_trixig_parts.glb`) og fire konsept (`01.glb`–`04.glb`). Repoet har òg Trixig+-designsystemet i `design-system/`.

### Google Drive

Kartlegginga av Drive er ikkje ferdig. Denne delen blir oppdatert.

- **Hovudmapper:**
  - `GK4_TRIXIG` med undermappene `trixig`, `trixig fold`, `trixig redesign` (med `trixig_print`) og `trixig usdz`.
  - `Trixig` med undermappene `trixig rot` og `trixig_strukturbygger`.
- **Mykje ligg dobbelt.** Til dømes finst `2 Introduksjon om elskrutrekker Trixig.pptx` og `Designbrief Trixig elskrutrekker.docx` i fem kopiar kvar.
- **Store arbeidsfiler frå juni** (Blender, Plasticity, USDZ) ligg berre i Drive: `trixig_colani`, `trixig_fold`, `trixig_new_01`–`04` og `trixig_original_and_drafts`.

### Figma

- `GK4_Trixig.fig` har sidene `Ikea_brand`, `Hovuddokument` (med rammene `DesignA`, `Design_B` og `Design_C`) og `kompoenent`. Ifølgje `design-system/README.md` i nettstad-repoet kjem konseptbileta frå 8. mai derifrå. Lenkja til fila ligg ikkje i noko repo.

## Mappestruktur i dette repoet

```text
docs/
  course/            kursmateriale: prosjektbeskriving, designbrief, forelesingar, litteraturliste
  deliverables/      innleveringar per frist, pluss supplering_tre_konsept/
  project/           arbeidsnotat i markdown (konseptgjennomgang, formføringsplansje, ferdigstillingsplan …)
  reports/           docx- og pdf-versjonar av notat og debrief
  brand/             Trixig+-brandmark
  repo_cleanup/      logg over all opprydding (cleanup_manifest.csv, cleanup_summary.md)
assets/
  reference/         teardown-foto, inspirasjon, IKEA-logo, teknisk
  finished_graphics/ figurar, skisser og grafikk brukt i leveransane
  generated/         genererte bilete: skisser/ (28.04), gen_26_05/ (Tjalve-plansjar), gen_13_06/ (juni-redesign), trixig_redesign/
cad/
  fusion/            Fusion- og Blender-skript, render, redesign_01-eksport
  plasticity/        Plasticity-filer, referansemesh og OBJ-eksport (export/)
  print/             STL og 3MF for 3D-print
  models/            eksterne referansemodellar
methods/tjalve/      utval frå Tjalve-metoden
```

## Opprydding 21. november 2026

- **Sletta:**
  - 3 eksakte duplikat.
  - Next.js-byggjecachen i `grunnstruktur_web/`. Kjeldekoden til denne struktur-byggjaren vart fjerna i juni, men ligg i git-historikken (commit `8a05efe`).
  - 5 autobackup-filer (`.blend1`, `.blend11`, `_prev1.plasticity`), om lag 166 MB.
- **Flytta:**
  - Referansemesh og `plasticity_export/` til `cad/plasticity/`.
  - `ikea.svg` til `assets/reference/ikea/`.
  - `trixig_reedeeesign_01/` til `assets/generated/gen_13_06/`, med nye filnamn.
- `.gitignore` held no autobackup-filer og byggjecache ute.
- Kvar fil er logga i [`docs/repo_cleanup/cleanup_manifest.csv`](docs/repo_cleanup/cleanup_manifest.csv).
- Behaldt med vilje: to like STL-filer for batteri og kretskort. `cad/fusion/trixig_pcb_battery_print_stl.py` skriv same fil til både `cad/fusion/pcb_battery_asset/` og `cad/print/trixig_redesign/for_bambu/`.
- `.git`-mappa er om lag 1,1 GB fordi store filer ligg i historikken. Det krev omskriving av historikken å krympe ho, og det er ikkje gjort.

## Avvik å vere merksam på

1. **Vurderingsmatrisa** i `docs/project/konseptgjennomgang_8mai.md` har feil summar (120 / 104 / 76). Med same skår og vekter blir det 127 / 110 / 84. Rekkjefølgja er den same, og plansja brukar dei rette summane.
2. **Prisprosentane** i same fil (+10 % og +55 %) går ut frå 199 NOK. Debriefen oppgjev 179 NOK for TRIXIG 3,6 V. Plansja viser difor berre kronebeløp.
3. **Verdiorda** varierer mellom dokumenta:
   - den reviderte debriefen: «opnen, varig, ærleg»
   - formføringsplansja: «Synleg, Stille, Truverdig»
   - genererte plansjar: «Særeigen, Trygg, Sjølvstendig» og «Venleg, Presis, Robust»
4. **Batteriet:** 8. mai-manuset kallar cella «innelodda». Teardownen i debriefen viser derimot at cella ligg i fjørklemmer og ikkje er lodda.
5. **Fristen for debriefen:** prosjektbeskrivinga seier «mandag 4. april», men 4. april 2026 var ein laurdag. Fristen var måndag 4. mai, som er datoen debriefen sjølv oppgjev.
