# Ferdigstillingsplan — GK4 V26 Modul 2 TRIXIG

*Generert 28. april 2026 (dag 2 av 18). Sluttfrist 27. mai 2026.*
*Basert på gjennomgang av designbrief, prosjektbeskrivelse, debrief-utkast, eksisterande figurar/skisser, og Skulberg/Bjørnstad si metodikk-forelesing.*

---

## 0. Tidsline (dei kritiske datoane)

| Dato | Klokke | Leveranse | Form |
|---|---|---|---|
| **Ma 4. mai** | 09:00 | Personleg debrief | Moodle (PDF/DOCX) |
| **Fr 8. mai** | dagtid | Konseptgjennomgang (gruppeseanse) | Munnleg + 3 fysiske skissemodellar |
| **Fr 8. mai** | 20:00 | 3B-analyse, kravspec, bærekrafthandling, 3 konsept­bilete + valt | Moodle |
| **Ma 11. mai** | 09:00 | Formføringsplansje + 3 verdiord | Moodle |
| **On 13. mai** | dagtid | Gjennomgang formkonsept (gruppeseanse) | Munnleg |
| **Ma 25. mai** | 20:00 | Digital sluttpresentasjon + 3 modellbilete | Moodle |
| **Ti–On 26.–27. mai** | plenum | Sluttpresentasjon + 1:1 utseendemodell | Munnleg + fysisk |

---

## 1. Status — kva som finst, kva som manglar

### 1.1 Kva som er ferdig eller nær ferdig

**Tekstgrunnlag:**
- `debrief-modul2-trixig.docx` — fullstendig 7-seksjons debrief med marknadsanalyse, teardown, EU-rammer, R2R-indeksar, materialkunnskap, ergonomi, brukar­innsikt, problemområde, 3B-analyse, kravspec og kjelder. Klart til formattering for innlevering.
- `notat/Konseptgjennomgang_8mai.md` — 12 slides med tre konseptforslag (Trixig+, Tactil, Modular), vurderingsmatrise og valt konsept. Manglar berre fotografi av dei fysiske skissemodellane.
- `notat/Formføringsplansje_11mai.md` — fullstendig drøfting av tre verdiord (Synleg, Stille, Truverdig) med referanseobjekt og A3-layout-spec. Manglar bildemateriale frå referanseobjekta og final A3-eksport.
- `notat/Prototypedokumentasjon.md` — full byggjeplan med BOM, leverandørar og tidsplan for både foam-prototype (P1) og funksjonell prototype (P2).
- `notat/Produksjonskjede_TRIXIG.md` — 10-leddskartlegging av forsyningskjeda frå kobolt til kassering, med IKEA-eigarstruktur og IWAY-grenser.

**Visuelt grunnlag:**
- `ferdigstilt_grafikk/figurar/figur=01..13` — ferdige illustrasjonar (heroshot, hand­percentilstudie ×2, regulatorisk tidsline, kritikkringen, IKEA-stigen, FIXA-vs-TRIXIG-eske ×2, instegspris, naming­kritikk, forretningsmodell-tidsline, posisjoneringskart, spesifikasjonsark).
- `ferdigstilt_grafikk/grafikk=01..04` — IKEA-logo-variantar.
- `ferdigstilt_grafikk/skisser/` — produktskisser med bakgrunn fjerna (Trixig-illustrasjon, exploded view, serviceport).
- `ferdigstilt_grafikk/teardown/` — fem teardownfoto.
- `skisser/skisse_001..100` + `skisser/figur/figur_001..029` — 130+ konseptskisser (rådata).

**Modellgrunnlag:**
- `trixig/trixig.usdz` — eksisterande 3D-fil av originalen (referanseobjekt for sammenlikning).
- `teardown/Trixig_plus.scad` — OpenSCAD-utkast (sjekk om det er nyttig for Fusion-import eller om me skal byggje frå null).

### 1.2 Kva som manglar

**Research som ikkje er gjort enno:**
- Kvantitativ brukarundersøking (sjå seksjon 3.1).
- Strukturerte brukarintervju og observasjon (sjå 3.2).
- Antropometriske målingar i hovet (eigen hand mot DINED 5/50/95-percentilar) (sjå 3.3).
- Konkurrent-prising og hyllesjekk i fysisk butikk (Biltema, Clas Ohlson, Jula, IKEA) (sjå 3.4).
- Brand-audit av TRIXIG-serien (heile sortimentet, ikkje berre 3,6 V) (sjå 3.5).

**Spesifikasjonar som ikkje er detaljerte:**
- Komplett BOM for Trixig+ med leverandørar, einingspris og kostnadsmål (skal liggje under +11 NOK per eining over original).
- Strektegning A3 sideview med kotering.
- Materialspec med ISO 11469-koder, rPCR-andel, leverandørreferansar.
- CMF-board (Colour-Material-Finish) med fysiske prøver.
- Tolerance-spec for 18650-fjørholder, kapsling-pasning og Torx-skruekrager.

**Modellbygging:**
- 3 blåskum-skissemodellar for konseptgjennomgang 8. mai.
- 1 blåskum 1:1 utseendemodell for sluttpresentasjon (utan farge per krav).

**CAD:**
- Fusion 360-modell (heile produktet, inkludert eksplodert visning).
- 3D-rendering for digital presentasjon.

**Designdagbok:**
- Ingen eksisterande fil. Skal førast fortløpande — sjå 6.

**Innleverings­filer:**
- Eksport av debrief til PDF.
- Eksport av Konseptgjennomgang til presentasjons-PDF + separate Moodle-filer.
- Eksport av Formføringsplansje til A3-PDF.
- Sluttpresentasjon (PowerPoint eller Keynote).

---

## 2. Leveransematrise

| Leveranse | Krav (frå kursdok) | Status | Kva manglar | Frist |
|---|---|---|---|---|
| Personleg debrief | Designbriefen reflektert + eige standpunkt | Utkast komplett | Format­tering, illustrasjons­plassering, eksport til PDF | 4.5. 09:00 |
| 3B-analyse | Brukar / Bruksituasjon / Bruksmåte | Utkast i debrief + slide 4 i Konseptgjennomgang | Standalone PDF, kanskje styrkast med kvant data | 8.5. 20:00 |
| Kravspec | Estetisk/Ergonomi/Teknisk/Marknadsøkonomi/Bærekraft + Skal/Bør/Kan | 30 krav lista i Konseptgjennomgang slide 5; 6 kategoriar i debrief 5 | Konsolidering til éin matrise (5×3) etter Skulberg si mal, prioriteringsmerking | 8.5. 20:00 |
| Bærekrafthandling | ≥ 1 konkret handling med målbar effekt | Definert (utbyttbart batteri + reparerbart hus + ISO-merking + 7 års reservedelar) | Standalone PDF med målbar effekt-estimat | 8.5. 20:00 |
| 3 konseptforslag | Skissemodellar + bilete | Konsept utvikla på papir; modellar ikkje bygde | **Bygg 3 blåskum-modellar; fotografer**| 8.5. 18:00 |
| Vald konsept | Markering | Trixig+ er valt i tekst | Ein-setning .txt + foto av valt | 8.5. 20:00 |
| Formføringsplansje | A3 med 3 verdiord + form-DNA | Tekst komplett | Eksport, referansebilete, strekteikning | 11.5. 09:00 |
| Sideview-strekteikning A3 | Som grunnlag for volummodell | Skisse i Prototypedok kap. 3 | Reint A3-format med kotering | 11.5. 09:00 |
| 1:1 fysisk utseendemodell | Utan farge | Ikkje starta | **Bygg etter blåskum-prosess** | 25.5. 18:00 (foto­dato) |
| 3 modellbilete | Front, side, perspektiv | n/a | Ta etter modell ferdig | 25.5. 20:00 |
| Fusion 360 CAD | Detaljert med modulgrenser | Ikkje starta (.scad finst som grunnlag) | **Heil modellering** | 25.5. 18:00 |
| 3D-rendering | I Fusion 360 | Ikkje starta | Render etter CAD ferdig | 25.5. 18:00 |
| Digital sluttpresentasjon | Løysing + bærekrafthandling + materialvalg + formuttrykk + brand-pos + render | Ikkje samla | **Slå saman alle delar i éin PPT/Keynote** | 25.5. 20:00 |
| Designdagbok | Fortløpande | Ikkje ført | **Føre kvar dag** (sjå 6) | løpande |

---

## 3. Research-plan

Briefen er i hovudsak skriven, men det manglar empiri som vil styrke argumenta i sluttpresentasjonen og som sensorane vurderer under "prosjektets troverdighet i bedriftskontekst" og "produktets bruksverdi for tiltenkte sluttbruker". Research­arbeidet bør komprimerast til ei intens veke (28. april–4. mai), parallelt med ferdigstilling av debriefen.

### 3.1 Kvantitativ brukarundersøking

**Mål:** Validere persona-hypotesane i debriefen (ambisiøs amatør, leigetakar/student, sporadisk brukar). Få fram tal for jobs-to-be-done, smertepunkt og betalingsvilje.

**Metode:** Online-spørjeskjema via Google Forms eller Typeform, distribuert i tre kanalar:
- AHO/UiO-studentkull (leigetakar/student-segment)
- Facebook-grupper for DIY ("Jeg liker å bygge", "Oppussings­tips") (amatør-handverkar)
- Eige nettverk via LinkedIn (sporadisk brukar)

**Spørsmål (ca. 20 stk):**
1. Eig du elektrisk skrutrekkar? Kva merke/modell?
2. Kor ofte brukar du han? (skala: kvar dag — aldri)
3. Kva oppgåver brukar du han til? (multi-select: flatpakke-møblar, gardin­stenger, dørhandtak, hyller, småreparasjon, anna)
4. Kor mykje betalte du? Var det med tilbehør i esken?
5. Har batteriet svikta? Kva gjorde du då?
6. Har du forsøkt å reparere? Kva hindra deg?
7. Kor viktig (1–5) er: pris / merke / reparerbarheit / utskiftbart batteri / tilbehør i esken / ladetid / vekt / dreiemoment?
8. Skala 1–5: kor mykje ekstra ville du betalt for: utskiftbart batteri / 7 års reservedelar / tilbehør i esken / lengre garanti?
9. Demografi: alder, kjønn, bustad­situasjon (leigar/eigar), inntekt­band.

**Mål for utval:** N ≥ 50 svar, fordelt på ~30 % per persona.

**Tid:** Distribusjon 28.4. — datasamling 28.4.–3.5. — analyse 3.–4.5.

### 3.2 Kvalitative brukarintervju

**Mål:** Få djupne på smertepunkt som ikkje fangast i Likert-skala. Validere semantikk-hypotesar (asymmetrisk retningsbrytar, status-LED-stripe).

**Metode:** Halvstrukturerte intervju, 30–45 min per person, 3–5 informantar fordelt på personae. Showe TRIXIG-original og spørje "kva er problemet med denne?", "kva ville du endra?".

**Tid:** 29.–30. april (parallelt med spørjeskjema).

**Logg:** Notater og lydopptak (med samtykke) i `notat/intervju/`.

### 3.3 Antropometri og handpassing

**Mål:** Verifisere at 110° grepvinkel og 32–38 mm grepdiameter dekkjer 5.-perentil kvinne til 95.-perentil mann. Få faktiske handmål frå minst tre forsøkspersonar i ulik storleik.

**Metode:**
- Mål handlengde, handbreidde, tommel-omkrins frå tre personar (familiemedlem + medstudent + ein større/mindre informant).
- Samanlikne mot DINED-tabell (TU Delft) eller Pheasant Bodyspace 2006.
- Test grepskomfort på TRIXIG-original, evt. modifisert med tape/skum for å simulere endringar.
- Lag enkel grafikk av hand i tre storleikar over Trixig+-silhuett (vidareføring av figur=02 og figur=05).

**Tid:** 1.–2. mai (laurdag/sundag).

### 3.4 Konkurrentanalyse i fysisk butikk

**Mål:** Eksakte prisar, vekter, esketuinnhald, og hylleplassering for Bosch IXO, HOTO, Bauhaus-kjedevarer, Biltema, Clas Ohlson sine eigenmerke. Fotografi frå hylla.

**Butikkar:**
- IKEA Slependen (TRIXIG/TRIXIG 12V/eksisterande FIXA om finst)
- Clas Ohlson Storo (Cocraft LXC + Bosch IXO)
- Biltema Alnabru (Biltema-eigne + lågprisalternativ)
- Bauhaus Kalbakken / Maxbo (Bosch + DeWalt)

**Kva noterast:** Hyllepris, kva som ligg i esken, kva tilbehør sel separat, vekt frå emballasje, materialinntrykk.

**Tid:** 30. april (ein dag i butikkar).

### 3.5 Brand-audit TRIXIG-serien

**Mål:** Verifisere at Trixig+ ligg innanfor TRIXIG si visuelle ramme. Lag skjema med alle TRIXIG-produkt og deira form-DNA.

**Metode:**
- Kartlegg alle TRIXIG-produkt på ikea.com (skrutrekkar 3,6 V, drill 12 V, hammar, skiftnøkkel-sett, måleband, om relevant).
- Lag formspråk-matrise: pistolform / inline / tool­shape, hovudfarge, akssentfarge, materialinntrykk, logoplassering, snormarkør.
- Identifiser dei to-tre mest karakteristiske brand-markørane som Trixig+ må respektere.
- Krysssjekk mot IKEA brand guidelines (`ikea_profil/Brandmark_TrixigPlus.md` har eit utkast).

**Tid:** 2. mai (parallelt med antropometri).

### 3.6 Produksjons­spesifikasjon — kva skal Trixig+ faktisk vere?

**Mål:** Frå konseptbeskriving til konkret BOM, leverandørar, einingspris.

**Komponentar som skal spesifiserast:**

| Komponent | Original­spec | Trixig+-spec (mål) | Leverandør (ev.) | Einings­pris (NOK) |
|---|---|---|---|---|
| 18650 Li-ion-celle | INR19/66, 1,5 Ah, lødde | 18650 standard, 1,5–2,0 Ah, fjørmontert | Samsung 25R / LG MJ1 / Molicel P26A | 25–35 |
| Motor | DC 385-typen, 3,6 V | DC 385-typen, behaldt | Original-leverandør | 22 |
| Planet­gear | 60:1, POM | 60:1, POM, behaldt | Original | 8 |
| Bitsfeste | 1/4″ hex, magnet | 1/4″ hex, magnet, brushed steel collar | Standard | 6 |
| PCB (TP4056 + BMS) | Integrert | Modulær (bytbar) | Original eller Aliexpress-OEM | 12 |
| ABS-skall (2 halvdelar) | Tokomp. ABS+TPE | 30 % rPCR ABS, mono-material, ISO 11469-merka | Lavpris-spr. mole. Kina | 8 |
| Torx T10-skruver M3×16 | n/a (selvskruver) | A2 stål, 6 stk | Bossard / Wurth standardlager | 1,80 |
| M3 hex-hylser | n/a | Messing, 8 mm djup, 6 stk | Bossard | 3 |
| Fjørholder 18650 | n/a (lødde) | Standard fjørholder med 2 kontakt­fjør | Aliexpress-OEM | 4 |
| Status-LED-PCB | n/a | 4× 0805-LED + driver | Aliexpress-OEM | 5 |
| Asymmetrisk retningsbrytar | symmetrisk vippe | Egendesignet, konveks/konkav | DPDT-bryter + 3D-printa cap | 6 |
| Stropp + ferrule | Standard | Behaldt | Original | 3 |
| Diverse ledningar, krymp, lim | — | — | — | 5 |

**Total estimert einings­kost (Trixig+):** ca. 109 NOK BOM, vs. estimert 90 NOK for original = +19 NOK BOM. Med 50 % marginpåslag → 219 NOK utsalgspris (+11 % over original). Innanfor mål.

**Tid:** 4.–5. mai (rett etter debriefen er innlevert).

---

## 4. Dag-for-dag-plan, 28. april – 27. mai

*Norske dagar. Klokke­slett er forpliktande for synkrone aktivitetar (forelesingar, gruppe­seansar, innleveringar) og rettleiande for individuelt arbeid.*

### Veke 18 — research, semantikk, kravspec (28.4. ferdig fase 1 til 4.5.)

**Måndag 27.4.** *(allereie gjort)*
- Prosjekt-intro, semantikk-workshop trykke/skyve/vri.

**Tysdag 28.4.** ← **i dag**
- 09–12 Semantikk-workshop modellbygging (verkstad).
- 13–15 Semantikk semifinale + finale.
- 15–17 **Distribuer kvant spørjeskjema (3.1).** Identifiser tre intervju­informantar (3.2).
- 17–20 Bilete­arbeid: kople ferdig­stilt grafikk inn i debrief-utkastet, oppdater illustrasjonsforslag.

**Onsdag 29.4.**
- 09–12 Workshop produktsemantikk, hånd og grep (Nina).
- 13–15 Brukarintervju #1 (telefon eller fysisk).
- 15–17 Polering av debrief seksjon 1–4.
- Kveld: følg med på spørjeskjema-svar, send påminning om naudsynt.

**Torsdag 30.4.**
- 09–12 **Konkurrentanalyse i butikk** (3.4). Bilete + notater.
- 13–15 Brukarintervju #2.
- 15–18 Inkorporere butikk­funn i debrief seksjon 2.1 og 5.6.
- 18–21 Polering debrief seksjon 5–7.

**Fredag 1.5.** *(arbeidardagen — ikkje undervisning)*
- 09–12 Antropometri-måling (3.3). Lag handpercentil-grafikk (vidareføring av figur=02 + 05).
- 13–17 Brukarintervju #3.
- 17–21 Konsolidere kvalitative funn.

**Laurdag 2.5.**
- 09–13 **Brand-audit TRIXIG-serien** (3.5). Form-DNA-matrise.
- 13–17 Polering Formføringsplansje med audit-funn.
- Kveld: ev. søk etter referansebilete (Festool ETS, Vola FS1, Olivetti Lettera 22, Braun T1000, Muji CD-spelar, Olivetti Valentine, Braun ET 88, Vitsoe 606, Festool batteripakke).

**Sundag 3.5.**
- 09–13 Analyser kvant-data. Lag tre figurar for innlevering.
- 13–17 Skriv saman debrief til ferdig form (Word eller InDesign), eksporter PDF.
- 17–21 Korrektur. Sjekk at alle figurar har figurnummer + kjelde.

**Måndag 4.5.**
- 08:00–09:00 Siste sjekk + **Moodle-innlevering personleg debrief 09:00**.
- 10–14 Forelesing eller veiledning (Anders/Nina).
- 14–18 Detaljering av kravspec (omsetting til 5×3-matrise etter Skulberg sin metode).
- 18–21 Skissevurdering: gå gjennom 130+ skisser, vel ut dei 3 beste retningane som mappar til Trixig+, Tactil, Modular.

### Veke 19 — konseptgjennomgang (5.5. – 8.5.)

**Tysdag 5.5.**
- 09–12 **Modellbygging blåskum dag 1** (verkstad). Trixig+-modell — fokus på ergonomi og dei fem kjenneteikna grepa.
- 13–17 Trixig Tactil-modell — TPE-overstøp simulert med syntetisk pels.
- 17–20 Bærekrafts­tekst som standalone (sjå Konseptgjennomgang_8mai.md slide 6).

**Onsdag 6.5.**
- 09–13 **Modellbygging blåskum dag 2.** Trixig Modular — kjernemodul + lengjehandtak.
- 13–17 Detaljering. Pussing, malingsprøvar (men hugs: utseendemodell skal vere utan farge — desse modellane er skissemodellar og kan ha sparsam fargemarkering).
- 17–20 BOM-arbeid (3.6) for Trixig+ (vald konsept).

**Torsdag 7.5.**
- 09–12 Foto­seanse av dei tre modellane. Front + side + perspektiv per modell, totalt 9 bilete + ev. ein samanlikningsoppstilling.
- 13–16 Førebu konseptgjennomgang-presentasjonen (12 slides — eksisterande manus i Konseptgjennomgang_8mai.md). PowerPoint eller Keynote.
- 16–19 Eksporter vurderingsmatrise, 3B-analyse, kravspec og bærekrafthandling som standalone PDF-ar.
- 19–21 Generalprøve munnleg framføring (10 min + 5 min spm).

**Fredag 8.5.**
- 09–14 **Konseptgjennomgang i gruppeseanse.** Presenter 12 slides, motta tilbakemelding, motivér konseptval.
- 14–18 Inkorporer veiledar­tilbakemeldingar.
- 18–20 Final eksport av alle Moodle-filer.
- **20:00 Moodle-innlevering** (3B-analyse, kravspec, bærekrafthandling, 3 konseptbilete, valt konsept).

### Veke 20 — formutvikling og formføringsplansje (11.5. – 15.5.)

**Måndag 11.5.**
- 08:00–09:00 **Moodle-innlevering Formføringsplansje 09:00** (eksisterande tekst i Formføringsplansje_11mai.md, må eksporterast til A3 PDF med referansebilete inkludert).
- 09–13 Strektegning A3 sideview av Trixig+ med dei tre nye elementa markerte.
- 13–17 Oppstart Fusion 360. Importere/byggje grov mass-modell.
- 17–20 Formdetaljering — radiar, skrueposisjon­ar, retningsbrytar­geometri.

**Tysdag 12.5.**
- 09–17 Fusion 360 — ferdig grov modell, alle modulgrenser.
- 17–20 Førebu munnleg gjennomgang for onsdag.

**Onsdag 13.5.**
- 09–14 **Gjennomgang formkonsept i gruppeseanse** (Nina). Presenter formføringsplansje, motta tilbakemelding.
- 14–17 Inkorporer tilbakemeldingar i CAD og plansje.
- 17–20 Detaljering — chamfer, fillet, partingslines.

**Torsdag 14.5.**
- 09–17 Fusion 360 — full detaljering. Innebygde Torx-skrue­krager. ISO-merking innstøypt på innside av skall.
- 17–20 Eksporter STL-filer for 3D-printing av prototype-skall (om P2 vert bygd).

**Fredag 15.5.**
- 09–17 Fusion 360 — render-førebuing. Material-tildeling. Lyssetjing.
- 17–20 Render første pass. Sjekk geometriproblem.

### Veke 21 — CAD og modellbygging (18.5. – 22.5.)

**Måndag 18.5.** og **Tysdag 19.5.**
- **Hovudfokus: bygge 1:1 utseende­modell i blåskum** (verkstad).
- Fem-lags blåskum, kontaktlim, smerg­ling. Sjå Prototypedokumentasjon kap. 4.
- Modellen skal vere utan farge (kursetkrav).
- Detaljar: sett inn dummy 18650-celle, dummy retningsbrytar i konveks/konkav, dummy LED-stripe.

**Onsdag 20.5.**
- 09–13 Modell-finishing (pussing korn 400, ev. enkelt grunningstrøk).
- 13–17 **Foto­seanse av 1:1-modellen.** Tre bilete (front, side, perspektiv) i god lyssetjing, ev. på nøytral bakgrunn (kvit eller grå).
- 17–21 Fusion 360 — finale render­pass.

**Torsdag 21.5.**
- 09–13 Render to perspektiv + eksplodert visning + closeup på batterimodul.
- 13–17 Bygg sluttpresentasjon (PowerPoint eller Keynote). Forventa struktur:
  1. Tittel + ein-setning posisjonering
  2. Premiss og kontekst (EU 2027 + IKEA-stigen)
  3. 3B-analyse (kondensert)
  4. Kravspec (matrise-format)
  5. Tre konsept (frå konseptgjennomgang) + valgt
  6. Trixig+ form-DNA + dei 3 verdiorda
  7. Eksplodert visning av Trixig+
  8. Dei fem kjenneteikna grepa (visuell forklaring)
  9. Bærekrafts­handling med målbar effekt
  10. Materialvalg og BOM (kondensert)
  11. Brand-tilhøyrsle (TRIXIG-DNA-matrise)
  12. Render(ar) av sluttforslaget
  13. Foto av 1:1-modellen
  14. Vegen vidare (regulatoriske rammer, kommersiell logikk)
- 17–21 Generalprøve.

**Fredag 22.5.**
- 09–13 Korrektur og polering. Sjekk skrift­konsistens, bilete­eigarskap, kjelde­henvising.
- 13–17 Lag printa A3-plansje-versjon for å henge i sal.
- 17–20 Generalprøve nr. 2.

### Veke 22 — sluttinnlevering og presentasjon (25.5. – 27.5.)

**Måndag 25.5.**
- 09–14 Siste justering, stress-test framføring.
- 14–18 Polering bilete, tekst, animasjonar.
- 18–20 Eksporter til PDF og PPT, samanstill alle Moodle-filer (digital presentasjon + 3 modellbilete).
- **20:00 Moodle-innlevering sluttpresentasjon.**

**Tysdag 26.5. eller Onsdag 27.5.**
- Plenum­presentasjon (10 min framføring + 10 min spm).
- Demonstrasjon av fysisk modell.

---

## 5. Kritiske risikoar og avbøtingar

| Risiko | Sannsynleg | Konsekvens | Avbøting |
|---|---|---|---|
| Spørjeskjema får < 30 svar | Medium | Tynn empiri | Ta med kvalitative funn som hovud­dokumentasjon, kvant blir illustrerande |
| Brukarintervju ikkje fast in tid | Medium | Forseinking | Bestil minst 5 informant­slots, ver fleksibel på dato |
| Verkstad­plass ikkje ledig 5.–6.5. | Høg | Modellbygging stoppar | Bestill verkstad-time **i dag**; ha hjemmeløysing klar (skuredust + kjøkkenbenk) |
| 1:1-modell tek lengre enn forventa | Høg | Sluttpresentasjon utan modell | Start dagar 18.–20.5. (tre fulle dagar avsette); ha foam-prototype som backup |
| Fusion 360 har ikkje all kapasitet eg treng | Medium | Render lite imponerande | Vurder Rhino + KeyShot for render om Fusion ikkje når ut |
| Brand-audit avdekker at Trixig+ ikkje er truverdig som TRIXIG | Låg | Form-revisjon | Spar to dagar i veke 20 til form­revisjon dersom audit gir alvorleg innspel |
| Moodle nede ved innlevering | Låg | Forseinka levering | Eksporter kvar leveranse 4–6 timar før deadline |
| Sjukdom siste veke | Låg | Heile sluttveka tapt | Hold modell og presentasjon på 80 % ferdig nivå innan 20.5., slik at siste veke er polering |

---

## 6. Designdagbok — protokoll

Dagboka skal førast fortløpande (kursetkrav). Ho ligg som ein einskild fil `notat/designdagbok.md`. Kvar dagbok-oppføring har:

- **Dato.**
- **Tid på dagen.**
- **Aktivitet i overordna form** (research, skissering, modellbygging, CAD, veiledning).
- **Konkrete avgjerder** og kva som motiverte dei.
- **Kva som ikkje fungerte** og kva som skal prøvast i staden.
- **Bilete- eller fil­referansar** (kva fil i prosjektmappa dokumenterer dette).

Eksempel-format:

```
## 2026-04-28, tirsdag — dag 2

09:00–12:00. Semantikk-workshop trykke/skyve/vri på verkstad. Bygde tre
modellar i Cibatool, valde "vri" som vinnar i mi gruppe pga at den koniske
overflata bar handlinga klarare enn flat dreieskive.

13:00–15:00. Semifinale og finale plenum. Klassen valde tre
representant­modellar; mi gruppe sin kom ikkje med. Læring: Form
verifisering må vere taktil, ikkje berre visuell.

15:00–17:00. Distribuerte kvant­spørjeskjema (3.1) til 4 kanalar.
Identifiserte 3 intervju­informantar. Sende invitasjon.

17:00–20:00. La inn ferdig­stilte figurar i debrief­utkastet. Sjå
debrief-modul2-trixig.docx versjon 0.4.

Avgjerd: Beheld den asymmetriske retningsbrytaren som S1-uttrykk i
formføringsplansja, fordi semantikk-finalen viste at konveks/konkav
faktisk leser sterkare enn pil-grafikk åleine.
```

---

## 7. Dei første tre tinga eg gjer no

1. **Bestill verkstad-time** for 5.–6. mai (modellbygging blåskum) og 18.–20. mai (1:1-modell). Send mail til verkstad­ansvarleg i dag.
2. **Distribuer kvant-spørjeskjema** (3.1). Forventar første svar i kveld; hovudbølgje kjem ila. dei to neste dagane.
3. **Identifiser tre intervju-informantar** (3.2). Send 30-min Calendly-lenke for slot 29.4.–1.5.

Når desse tre er gjort, er research-blokka i gang og ein har frigjort hovudet til å arbeide med debrief-formaltering parallelt.

---

## 8. Filstruktur som styringsverktøy

For å halde oversikt under intensitet vert mappa organisert slik:

```
GK4_TRIXIG/
├── notat/
│   ├── ferdigstillingsplan.md          ← denne
│   ├── designdagbok.md                  ← oppdaterast dagleg
│   ├── Konseptgjennomgang_8mai.md       ← klar
│   ├── Formføringsplansje_11mai.md      ← klar, treng A3-eksport
│   ├── Prototypedokumentasjon.md        ← klar
│   ├── Produksjonskjede_TRIXIG.md       ← klar
│   ├── intervju/                        ← nytt: råopptak/-notater
│   ├── kvant_resultat/                  ← nytt: spørjeskjema-eksport
│   ├── butikkbesok/                     ← nytt: foto frå konkurrent­butikkar
│   └── brand_audit/                     ← nytt: TRIXIG-serien-foto
├── ferdigstilt_grafikk/
│   ├── figurar/figur=01..13             ← klare illustrasjonar
│   ├── grafikk=01..04                   ← logo-variantar
│   ├── skisser/                         ← bakgrunnsfjerna skisser
│   └── teardown/                        ← fem teardownfoto
├── assets/generated/skisser/            ← rådata, 130+ skisser
├── assets/reference/teardown/           ← teardown- og produktfoto
├── docs/brand/                          ← brand-grunnlag
├── docs/course/                         ← orginale kursdokument
├── docs/project/                        ← prosjekt- og produktdokument
├── docs/deliverables/                   ← berre eksporterte filer for Moodle
├── debrief-modul2-trixig.docx           ← under arbeid
└── personleg-debrief-trixig.pdf         ← versjon 0.X
```

---

## 9. Kva eg ber om frå deg no

Eg har ført planen med eit konservativ stilval — så litt overdimensjonering på research, og ein klar marsjordre kvar dag. Etter at du les gjennom kan du:

1. **Korrigere prioriteringar.** Skal noko fjernast (for mykje kvant?) eller leggjast til (manglande tema?).
2. **Bestemme om me skal bygge P2 funksjonell prototype** i tillegg til 1:1-utseendemodellen, eller berre P1. Kursetkrav = berre 1:1-utseendemodell utan farge. Pluss-poeng for funksjonell prototype, men det krev ekstra ~30 timar.
3. **Bestemme verktøyval for sluttpresentasjon:** PowerPoint, Keynote, eller InDesign-PDF? Påverkar render-format og animasjon.
4. **Stadfeste at Trixig+ er valt konsept.** Konseptgjennomgang_8mai.md har det allereie som vinnar — om du heller vil ta Tactil eller Modular i sluttinnspurten må me revidere planen.

Når desse fire punkta er stadfesta, byrjar me å eksekvere.

---

*v1.0 — 28. april 2026, dag 2 av 18.*
