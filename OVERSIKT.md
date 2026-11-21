# Trixig: oversikt

Sist oppdatert 21. november 2026.

Repoet er skrella ned til det som trengst for å fullføre. Alt anna er sletta, men ligg i git-historikken (sjå [Hente att sletta filer](#hente-att-sletta-filer)).

## Neste steg

1. **Lever suppleringa:** [`docs/supplering_tre_konsept/plansje_tre_konsept_a3.pdf`](docs/supplering_tre_konsept/plansje_tre_konsept_a3.pdf).
   - Legg inn namnet ditt først. Det står ikkje på plansja fordi repoet er offentleg.
   - Endre `plansje_tre_konsept.html` i same mappe, og lagre som PDF frå Chrome (A3 liggande, ingen marg, bakgrunnsgrafikk på).
2. **Vel konsept** i [`konsept/`](konsept/). README-en der forklarar kodane.
3. **Modeller konseptet** rundt dei målte originaldelane i [`cad/original_trixig/`](cad/original_trixig/). Krava står under.
4. **Print og bygg** etter [`docs/prototypedokumentasjon.md`](docs/prototypedokumentasjon.md).

## Krav som styrer forma

Frå designbriefen ([`docs/oppgaveskildring_og_designbrief.pdf`](docs/oppgaveskildring_og_designbrief.pdf)):

- Bruk den eksisterande motoren og batteriet.
- Bitshaldaren skal passe bits på 6,35 mm (¼″).
- Lading med USB-C (5 V, minst 1 A).
- Produktet skal ha IKEA-logoen og fargane i TRIXIG-serien: matt svart og lyseblå aksent.
- Emballasjen kan ikkje vere større enn 993 cm³, og helst mindre.

Frå kravspesifikasjonen din ([`docs/kravspec_trixig.md`](docs/kravspec_trixig.md)):

- Minst 5 Nm, og minst 60 treskruer per lading.
- Vekt under 400 g.
- Brukaren kan byte batteriet med standard verktøy.
- Skalhalvdelane kan skiljast utan å bli øydelagde.
- Statuslys for batteriet, men ingen skjerm.
- Retningsbrytaren har tydeleg skilnad mellom dei to posisjonane, både å kjenne og å sjå.
- Formspråket passar med resten av TRIXIG-serien.

## Innhald

```text
docs/
  oppgaveskildring_og_designbrief.pdf   oppgåva og briefen frå lærarane
  kravspec_trixig.md                    kravspesifikasjonen din
  prototypedokumentasjon.md             rettleiing for å bygge og printe prototypen
  supplering_tre_konsept/               plansja for suppleringa (PDF, PNG og HTML-kjelde)
konsept/                                kandidatkonsepta (A–C, 01–13, T1–T4, GA–GC, W1–W4, R1)
cad/
  original_trixig/                      målte delar av originalen: STL, komponentar, skyvelære-foto
  fusion/                               skript for motor og kretskort, notat, og R1-pakka i redesign_01/
assets/reference/ikea/                  IKEA-logo: ikea.svg til preging, webp-versjon til plansja
```

## Viktig å vite

1. **Måla i skyvelære-fotoa avvik frå modellane.** Til dømes er motorhuset Ø30,83 mot Ø32,0 i modellen, og kretskortet er 25,31 mot 26,31 mm breitt. Sjå tabellen i [`cad/original_trixig/README.md`](cad/original_trixig/README.md), og mål den fysiske delen før du modellerer tette passingar.
2. **To små delar har tolka namn.** Linsa under nasen og detaljen i toppanelet er namngjevne ut frå kvar dei sit.
3. **Summane i vurderingsmatrisa på plansja er retta** til 127 / 110 / 84. Notatet frå 8. mai hadde 120 / 104 / 76.

## Andre stader

- **Nettstaden** ([`lukketsvane/trixig.iverfinne.no`](https://github.com/lukketsvane/trixig.iverfinne.no)) har 3D-modellane til W1–W4 og originalen.
- **Google Drive** (`My Drive/01 aho/GK4/GK4_TRIXIG`) vart rydda 21. november. No ligg berre dette der:
  - `Modellar/`: 3D-kjeldene `trixig_new_01`–`04.usdz` (truleg W1–W4) og `FERDIG+REDESIGN_01/02.usdz`, og 3D-modellane frå mai.
  - `trixig fold/` og `trixig usdz/`: 3D-variantar i USDZ, GLB og STL.
  - `Dokument/` og rota av mappa: debriefane og eigne dokument. `Debrief_Materiale/` har kjeldematerialet til debriefen.
  - 534 filer (3,0 GB) ligg i papirkorga fram til om lag 21. desember. Alle hadde kopi i git-historikken, var duplikat eller var nedlasta referansar.
  - Kjeldefila til R1, `trixig_original_and_drafts.blend`, ligg i den synkroniserte PC-mappa `Desktop/3mf`. Den mappa er ikkje rørt.
- **Fusion 360** har den parametriske originalmodellen «IKEA TRIXIG 3.6 original» i prosjektet «IKEA Redesign GK4».

## Hente att sletta filer

Alt som vart sletta 21. november 2026, ligg i commit `dca61ec`. Slik hentar du tilbake ei fil eller ei mappe:

```bash
git checkout dca61ec -- <sti>
# døme: git checkout dca61ec -- docs/project/
```

Mellom anna vart dette sletta:

- kursforelesingane
- debriefen og dei tidlegare innleveringane
- prosessnotata
- om lag 470 bilete: KI-genererte skisser, plansjar og renderar, og overflødige foto
- printfilene frå mai
- Plasticity-studiane og referansemodellane
- Tjalve-skanningane og ryddeloggane
