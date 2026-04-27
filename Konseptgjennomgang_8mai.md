# Konseptgjennomgang — fredag 8. mai 2026

*GK4 V26 Modul 2. Innlevering Moodle innan 8. mai kl. 20:00 — 3B-analyse, kravspec, vald bærekrafthandling, tre konseptbilete, markering av vald konsept. Denne fila er manus til presentasjonen og innleveringsdokument i éin.*

Forfattar: [Studentnamn]
Dato: 8. mai 2026
Veileder: Harald Skulberg

---

## Slide 1 — Tittel

**TRIXIG redesign — frå impulskjøp til reparerbart verktøy**

Trixig+ for IKEA, GK4 V26 M2.

[Studentnamn], AHO, mai 2026.

---

## Slide 2 — Premiss

IKEA TRIXIG 3,6 V er ein dugande budsjett-skrutrekkar. Han er ikkje god nok. Innelodda batteri, sealed konstruksjon, symmetrisk retningsbrytar, ingen status-kommunikasjon, ingen ISO-merking. Februar 2027 vert han ulovleg å selja under EU 2023/1542.

Eg redesigner han slik IKEA uansett må gjera det innan 18 månader.

---

## Slide 3 — Research, kort versjon

**3B-analyse.** Brukaren er ung-vaksen førstegongskjøpar utan tidlegare verktøyerfaring. Bruksituasjonen er hjemme, kortintensivt, med visuell merksemd bunden til skruehovudet. Bruksmåten er ein fast sekvens der retningsval er den einaste reelle avgjerda — og der semantikken sviktar mest.

**Demontering.** Seks selvskruver, to ABS-skall, innelodda 18650-celle, symmetrisk retningsbrytar, ingen ISO-merking. Cella har 300–500 syklusar; produktet har same levetid som cella.

**Kritikk-aksen som ber.** Innanfor same TRIXIG-serie har 12 V-drillen utskiftbart batteri. 3,6 V-skrutrekkaren har det ikkje. Det er ikkje teknisk avgrensing. Det er prismekanikk.

(Full kritikkanalyse i `Kritikk_av_IKEA_Trixig.md`.)

---

## Slide 4 — 3B-analyse i kort

| Aks | Kjernesvar |
|---|---|
| **Brukar** | Ung-vaksen, 20–40 år, første heim, ingen verktøyerfaring, IKEA-kunde, estetisk sensibel, prisbevisst |
| **Bruksituasjon** | Hjemme på parkett, dårleg arbeidsljos (difor LED i nesen), kort­intensiv 20–60 min, månader utan bruk mellom |
| **Bruksmåte** | Pistolgrep, fast sekvens, retningsval er einaste reelle avgjerd, ingen koplings­begrensing, brukaren må sjølv vurdera når skruen er ferdig |

Detaljert utgreiing i hovudrapporten kapittel 4.

---

## Slide 5 — Kravspec, kortversjon

Kravspecen er strukturert i fire kategoriar etter MoSCoW. Dei avgjerande Must-krava er:

- F1: ≥ 5 Nm dreiemoment.
- F4: ≥ 60 standard treskruver per ladning.
- E2: vekt < 400 g.
- E5: trinnløs effektkontroll.
- E6: tydeleg haptisk og visuell forskjell mellom retningsbrytarens to posisjonar.
- S1: formspråk i samsvar med øvrige TRIXIG-produkt.
- S5: statuslys for batterinivå, men ingen skjerm.
- B1: utskiftbart batteri av brukaren med standard verkty.
- B2: skall skiljbare utan øydelegging.
- B5: minst 8 års levetid.

Full kravspec med alle 30 krav i hovudrapporten kapittel 8.

---

## Slide 6 — Vald bærekrafthandling

**Bærekrafthandling: gjera det 3,6 V-skrutrekkaren ikkje er — reparerbar.**

Konkret, målbart:
- Standard 18650-celle utskiftbar av brukaren med Torx T10
- Seks Torx T10 metallskruver i M3 messing-hylser, skall kan opnast og lukkast gjentatte gonger
- ISO 11469-merking innstøypt i ABS, materialfraksjonar separable
- Reservedelsforsyning gjennom spareparts.IKEA.com i minst 7 år etter utfasing

**Mål:** auka levetid frå ~5–10 år til 12+ år. Reduserer total miljøpåverknad per brukstime med ein faktor 2–3 gjennom forlenga produktlevetid og redusert kasserings­frekvens.

**Regulatorisk:** innfrir EU 2023/1542 artikkel 11 før februar 2027.

---

## Slide 7 — Konsept A: Trixig+ (forsiktig forbetring)

**Strategi:** Behald form, fargesetjing og produksjonsmetode. Endra det som *må* endrast.

**Fem grep:**
1. M3 Torx T10 metallskruver i messinghylser i staden for selvskruver
2. Utskiftbar 18650 i fjærkontakt-holder
3. Asymmetrisk retningsbrytar (konveks med pil-relieff fram, konkav bak)
4. Status-LED-stripe (fire prikkar) bak
5. ISO 11469-merking + 30 % rPCR ABS

**Skissemodell:** blåskum, full skala, demonstrerer alle fem grep visuelt.

**Pris:** 219 NOK (+10 %).

**Brand-fit:** maksimal. Uskil­ekjeneleg frå original i form, identifiserbar i detalj.

---

## Slide 8 — Konsept B: Trixig Tactil (ergonomisk oppgradering)

**Strategi:** Trixig+ pluss ergonomisk-mekaniske forbetringar.

**Fire grep utover Trixig+:**
1. TPE-overstøp på grepet for friksjon og opplevd kvalitet
2. Mekanisk dreiemomentkopling — slipper ved overdreven moment, vernar mot avskalling av skruehovud
3. Separat lommelyktknapp (ikkje koplet til avtrekkar)
4. Lett auka motorklasse for 7 Nm i staden for 5 Nm

**Skissemodell:** blåskum med syntetisk TPE-pels på grepet, ikon-skisse av koplingsmekanismen.

**Pris:** estimert 309 NOK (+55 %).

**Brand-fit:** middels. Begynner å konkurrera med Bosch IXO i prispunkt og kan øydeleggja TRIXIG si demokratiske posisjonering.

---

## Slide 9 — Konsept C: Trixig Modular (systembasert)

**Strategi:** Skrutrekkaren vert modul i eit større TRIXIG-system. Kjerne-modulen mindre og enklare; tilbehør sel separat.

**Tre modulvariantar:**
1. Kjerne-modul (det som no er TRIXIG, men 30 % mindre)
2. Lengjehandtak med ekstra batteri som forvandlar kjernen til ein lett drill
3. Auto-bits-magasin som matar bits sekvensielt for serie­montering

**Skissemodell:** blåskum, viser kjerne pluss eitt vedlegg (lengjehandtak), bajonett­kopling synleg.

**Pris:** kjerne 169 NOK, modular 199–299 NOK.

**Brand-fit:** lågast. Bryt med IKEAs ein-funksjon-eit-produkt-logikk og krev kross-produkt-redesign av heile serien. Stor risiko, stor utviklingskostnad.

---

## Slide 10 — Vurderingsmatrise

| Kriterium (vekt) | Trixig+ | Tactil | Modular |
|---|---|---|---|
| Brukarverdi (×3) | 7 | 9 | 8 |
| Pris (×3) | 9 | 6 | 4 |
| Reparérbarheit (×3) | 9 | 7 | 6 |
| Semantisk klarheit (×2) | 8 | 8 | 6 |
| IKEA-passande (×2) | 9 | 7 | 5 |
| Teknisk risiko (×2, inversert) | 9 | 7 | 4 |
| **Sum (vekta)** | **120** | **104** | **76** |

---

## Slide 11 — Valt konsept: Trixig+

Trixig+ vinn fordi han løyser alle dei seks kritikk-aksane (batteri, sealing, semantikk, status, materialretur, regulatorisk samsvar) til ein marginal­kostnad på +11 NOK per eining og eit prispåslag på 10 % som ligg innanfor IKEAs tolkningsrom for prisrevisjon. Han er teknisk realistisk innanfor fire vekers utviklingsvindauge, og han har høgaste brand-fit av dei tre alternativa.

Tactil tilfører reell brukarverdi men sprenger prispunktet. Modular er strategisk interessant men krev redesign av heile produkt­serien og er utanfor rammene for dette prosjektet.

---

## Slide 12 — Vidare arbeid

**Veke 20:** formføringsplansje med tre verdiord (synleg, stille, truverdig — sjå Formføringsplansje_11mai.md), formutvikling av Trixig+, materialprøvar.

**Veke 21:** Fusion 360 CAD-modell, sideview-strektegning A3, volummodell-bygging i verkstad.

**Veke 22:** sluttpresentasjon 26.–27. mai. Fysisk 1:1-modell, digital presentasjon, render fra Nano Banana 2 (sjå Nano_Banana_2_promptsett_TrixigPlus.md).

---

## Innleveringsliste 8. mai kl. 20:00 (Moodle)

| Fil | Innhald | Status |
|---|---|---|
| `3B_analyse_Trixig.pdf` | Slide 4-innhald som standalone PDF | må eksporterast |
| `Kravspec_Trixig.pdf` | Slide 5-innhald som standalone tabell | må eksporterast |
| `Bærekrafthandling_Trixig.pdf` | Slide 6-innhald som standalone tekst | må eksporterast |
| `Konsept_A_Trixig+.jpg` | Foto av blåskum-skissemodell A | må fotograferast |
| `Konsept_B_Tactil.jpg` | Foto av blåskum-skissemodell B | må fotograferast |
| `Konsept_C_Modular.jpg` | Foto av blåskum-skissemodell C | må fotograferast |
| `Valt_konsept.txt` | Eitt setning: "Vald konsept: A — Trixig+." | trivielt |

**Konvertering:** Opne denne markdown-fila i Word, "Lagre som" → split i fire dokument (3B, kravspec, bærekraft, samanstilling) eller hald saman som éin PDF.

---

*v1.0 — generert 27. april 2026, gjennomgang 8. mai 2026.*
