# Hol-rapport — designbrief vs. nåverande konsept

*Generert tysdag 28. april 2026 (dag 2 av 18). Ein "nye-auge"-gjennomgang av designbriefen frå Skulberg (versjon 22.04.2026) sett mot kva som faktisk ligg i Trixig+-konseptet i dag.*

Mål: identifisere kvar konseptet held, kvar det er svakt, og kvar det er direkte ute av brief-ramma. Rapporten er medvite kritisk — det er det som tener prosjektet no.

---

## 1. Brief-krav, status, kommentar

### Tabell — krav for krav

| # | Krav (frå brief) | Status | Kommentar |
|---|---|---|---|
| B1 | Eksisterande motor og batteri skal brukast | **Tolka, ikkje løyst** | Debrifen seier eksplisitt at "eksisterande batteri" er tolka som *celletype og elektrisk grensesnitt*, ikkje den forsegla integrasjonen. Det er ein defensiv argumentasjon Skulberg kan godta — men han kan òg avvise den. Lever-risiko: **HØG** dersom argumentet ikkje vert gjenta klart i munnleg presentasjon 8. mai. |
| B2 | Meir kompakt produkt — reduserte ytre dimensjonar | **Svakt adressert** | Skisse_082 viser 165 × 145 mm. Original TRIXIG 3,6 V er 165 mm lang. Det er **ikkje meir kompakt — det er om lag like stort**. Skisse_081 viser 100 mm høgde, betre. Kompaktheits-argumentet manglar: ingen direkte volum-samanlikning (cm³) i nokon av leveransedokumenta. |
| B3 | Reduser emballasjevolum, maks 993 cm³ | **Ikkje adressert** | Inga emballasje-løysing teikna eller spesifisert. Ingen volum-rekneskap. Kritisk for sluttleveransen. |
| B4 | Ny elskrutrekker skal innehalde IKEA-logo | Adressert | Ovale logo-merke synast på skissene. |
| B5 | Brukar fargar frå TRIXIG-serien | Adressert | Lyseblå snor og avtrekkar = TRIXIG-blå. Svart hovudkapsling = TRIXIG-svart. Oransje aksent på retningsbrytar er **ein avvik** frå serien — kan forsvarast som FIXA-arvelinje, men må forsvarast eksplisitt. |
| B6 | Tilpassa IKEA-målgruppe | Adressert i debrief (3B-analyse) | Ung-vaksen førstegongskjøpar. |
| B7 | Inngå i og fungere med TRIXIG-serien | Delvis adressert | TRIXIG 12 V har utskiftbart batteri (proprietært). Trixig+ med utskiftbart 18650 ville vere meir reparerbart enn 12 V-versjonen. Det skaper ein **inkonsistens innanfor serien** som Skulberg kan plukke på. Argumentasjonsleg løysing: framstill 3,6 V som *forløparen* IKEA bør oppgradere 12 V etter. |
| B8 | Bærekrafthandling med positiv livssyklus-effekt | Sterkt adressert | Reparerbarheit som hovud-bærekrafthandling. EU 2023/1542 art. 11. |
| B9 | Form på emballasje | **Ikkje adressert** | Sjå B3. |
| B10 | Eigna grafisk merkevaretilpassa uttrykk på emballasje | **Ikkje adressert** | Sjå B3. |
| B11 | IKEA si eksisterande emballasjetypografi skal brukast | **Ikkje adressert** | Inga typografi-research enno (Verdana / Noto IKEA). |
| B12 | Same kartongkvalitet (eller liknande) | **Ikkje adressert** | Brun bølgjepapp, single-wall, FSC-merka — må stadfestast. |
| B13 | USB-C lader (5 V DC, min. 1 A) | **Delvis adressert** | Skisse_082 nemner "USB-C 5V/1A". Det er **akkurat på minimum** (krever ≥1 A). For 18650-celle er 1 A under-dimensjonert (5 t lading). Bør spesifisere 1,5 A eller 2 A. |
| B14 | Bits og lader inngår ikkje i produktemballasje | **Inkonsistens-risiko** | Briefen er klar: ingen system­komponentar i emballasjen. Konseptet må visa emballasje med berre verktøy + snor. |
| B15 | Bitholder for 6,35 mm bits | Adressert | Magnetisk hex-feste. |

### Kort dom

Tre store hol — **emballasje (B3, B9–B12), kompaktheits-argumentet (B2), og lader-spec (B13)**. Det første er mest alvorleg fordi det er ein eksplisitt leveranse, ikkje berre eit argument. Emballasje­arbeidet bør startast i dag.

---

## 2. Inkonsistensar internt mellom dokumenta

Desse er det som vil gjera presentasjonen rotete dersom dei ikkje vert lukka før 4. mai.

### 2.1 Verdiord — 3 vs. 4

- **Formføringsplansje_11mai.md** seier: *Synleg, Stille, Truverdig.*
- **utvalgt_01_skisse_082_valgt_konsept.png** seier: *kompakt, reparerbar, ærleg, tilkopla.* Fire ord. Heilt annleis.
- **debrief-modul2-trixig.docx** seier: *opnen, varig, ærleg.* Tre ord, men *ikkje* dei same.

Tre dokument, tre forskjellige verdiord-set. Det er den mest synlege inkonsistensen i prosjektet og det fyrste ein sensor vil legge merke til.

**Anbefaling:** Lås verdiordene til *Synleg, Stille, Truverdig* (som har sterkast skriven argumentasjon i Formføringsplansja). Oppdater plansje­skissene og debrifen før 4. mai. "Tilkopla" som verdiord i skisse_082 er òg internt tvilsamt — det motseier "Stille" og introduserer eit smart-feature-løfte konseptet ikkje innfrir.

### 2.2 Antal skruver — 5 vs. 6

- **utvalgt_04_skisse_094_serviceport_innmat.png** seier: "5 skruer. Full tilgang til alle komponenter."
- **Konseptgjennomgang_8mai.md** seier: "Seks Torx T10 metallskruver i M3 messing-hylser."
- **utvalgt_03_skisse_095_reparerbar_moduloppbygging.png** viser fire skruvehovud i illustrasjon (men kallar dei "Standard PH1") — som motseier Torx-argumentet i Konseptgjennomgangen.

Lukk inn på **6 Torx T10**. Standardiser bilete­materialet før plansja vert eksportert til A3.

### 2.3 Skruvetype — Torx vs. Phillips

- Konseptgjennomgangen og debrifen bruker Torx T10 som hovud­argument (strammare moment, mindre cam-out, IKEA bruker Torx i andre serier som BLÅHAJ/MALM).
- Skisse_095 illustrerer "Standard PH1" Phillips-skruver.

**Lukk inn på Torx T10.** Phillips er semantisk feil grep — det signaliserer billeg-monteringspakke, ikkje "verkty for liv". Oppdater illustrasjonen.

### 2.4 Batteri-tilgang — verktøy vs. verktøyfri

- Skisse_082 viser eit **verktøyfritt trekk-spor** på batteriluken (fingernegl-tilgang).
- Konseptgjennomgangen seier "Standard 18650-celle utskiftbar av brukaren med Torx T10".

EU 2023/1542 art. 11 krev "without specialised tools, thermal energy or solvents". Verktøyfri tilgang **innfrir art. 11 utan tvil**; Torx-løysing krev argumentasjon om at Torx er "udbredt verktøy". 

**Anbefaling:** Behald verktøyfri tilgang for batteriluken (skisse_082-løysinga er den sterke). For full demontering av kapslinga — der bruker ein Torx T10 (dei seks skruvene i kapslinga). Det er ein **tonivå-arkitektur** som er sterk semantisk: dagleg bruk = ingen verktøy; reparasjon = standard verktøy. Oppdater Konseptgjennomgangen før 4. mai.

### 2.5 Tilkopla / smart-feature

Skisse_082 nemner "tilkopla" som verdiord, men det er ingen konkret smart-feature i konseptet (ikkje app, ikkje status-kommunikasjon utover LED-stripe). Ordet er **lovnads­overskridande**.

**Stryk "tilkopla" frå plansjen.** Erstatt med eit av dei tre låste verdiorda.

---

## 3. Manglande leveransar (med tidsfrist)

| Leveranse | Frist | Dagar | Status |
|---|---|---|---|
| Personleg debrief PDF (formattering) | 4. mai 09:00 | 6 | Tekst klar, krev layout-pass |
| 3 fysiske skissemodellar (Cibatool/blåskum) | 8. mai | 10 | **Ikkje starta**. Verkstad-time må bookast i dag/i morgon. |
| 3-konsept-plansje + valt konsept (Moodle) | 8. mai 20:00 | 10 | Skisse_082 finst som hovudkonsept; treng to alternative konsept (Tactil, Modular) som plansjer. |
| Formføringsplansje A3 (eksport) | 11. mai 09:00 | 13 | Tekst klar, skisser klare, **A3-PDF eksport ikkje gjort**. |
| Emballasje-konsept | 25. mai 20:00 | 27 | **Ikkje starta**. Bør begynnast no. |
| Strektegning A3 sideview m/ kotering | 25. mai 20:00 | 27 | Ikkje starta. |
| CMF-board | 25. mai 20:00 | 27 | Ikkje starta. |
| BOM komplett m/ leverandørar og einingspris | 25. mai 20:00 | 27 | Ikkje starta. |
| 1:1 utseendemodell (verkstad) | 26.–27. mai | 28–29 | Ikkje starta. Blåskum eller 3D-print + sparkle/lakk. |
| Sluttpresentasjon (PPT eller PDF) | 25. mai 20:00 | 27 | Ikkje starta. |

**Risikobilde:** Tekstgrunnlaget er sterkt. Visuell dokumentasjon og fysiske artefakt er svakt. Sannsynlegheit for at studenten kjem å under­levere på modell og emballasje er reell — særleg dersom verkstad-tidene ikkje vert booke i veka.

---

## 4. Tre konkrete designkritikk-punkt på skisse_082

1. **Pistolform vs. inline.** Skisse_082 er pistol — same arkitektur som original. Dette er ein **forsiktig** form-avgjerd. Briefen ber om kompaktheit og emballasje­reduksjon. Inline-form (slik IXO 7 har) er strukturelt meir kompakt og gir kortare emballasje. Spørsmål: er pistol-valet forsvart, eller var det berre vanen? Skissene 81–84 burde testa inline-alternativ side-ved-side.

2. **Service-rygg er bra, men stengselen er uklar.** Skisse_082 viser ein "service-port (5 skruer)" på baksida. Mekanismen for korleis kapslinga *opnar* (klipsfri, dvs. kva held han saman før skruvene er ute?) er ikkje teikna. Det er det neste detaljnivået som må løysast — og det vil overraske viss det tek lenger tid enn forventa.

3. **Status-LED — kor synleg er han eigentleg?** Verdiordet "Synleg" krev at LED-stripa er lesbar i dagslys og frå avstand. Skisse_082 viser ein lita LED-prikk på snuten. Det er ikkje sterkt nok. Formføringsplansja skriv om "innfelt men ikkje gøymd" — men teikninga viser noko som kan lesast som "gøymd". **Tegn LED-stripa større, og test ho frå tre vinklar (front, side, frå bordet).**

---

## 5. Anbefalt rekkefølgje for Iver, neste 48 timar

1. **I dag, 28. april (kveld):** Lås verdiord-set (Synleg, Stille, Truverdig). Stryk "tilkopla" og "kompakt" som verdiord. Gjer dette i Figma-fila og i alle .md-dokument. 30 minutt.
2. **I dag eller i morgon:** Send mail til verkstadansvarleg på AHO og bestill (a) blåskum­bygge­tid 5.–6. mai, (b) 1:1-modell­tid 18.–22. mai. Utan dette går prosjektet mot sluttspurt utan modell.
3. **I morgon, 29. april:** Start emballasje-arbeid. Sjå `notat/emballasje_arbeidsnotat.md`.
4. **I morgon, 29. april:** Standardiser skruvetype (Torx T10) og antal (6) i alle plansje­skisser. Få ein konsistent illustrasjon.
5. **30. april:** Kompaktheits-argumentet — gjer eit volum-rekneskap som sannsynleggjer at Trixig+ er minst 10 % mindre enn original (eller endra konseptet til at det faktisk er det). Utan tal er argumentet usynleg.
6. **1.–3. mai:** Personleg debrief A4-formattering. Eksporter til PDF for innlevering 4. mai morgon.

---

## 6. Risikoar som kan velte leveransen

- **Brief-tolking av "eksisterande batteri".** Dersom Skulberg avviser tolkingsargumentet om at "batteri" = celletype + elektrisk grensesnitt, fell heile reparerbarheits-tesen. **Mitigering:** Diskuter dette i ein 1:1 med Skulberg før 4. mai dersom mogleg. Få munnleg "ok" på tolkinga.
- **Modellbygginga blir ikkje ferdig.** Verkstad-bestilling i tide er einaste mitigering.
- **Sluttpresentasjon uten emballasje** — direkte tap av poeng. Mitigering: emballasje-konseptet startast denne veka.
- **Inkonsistens på sluttdagen.** Tre verdiord-set i tre dokument er forsterka av at konseptet vart utvikla over fleire iterasjonar utan ein synkroniserings-pass. Mitigering: lås på plass i kveld.

---

*v1.0 — 28. april 2026, dag 2 av 18.*
