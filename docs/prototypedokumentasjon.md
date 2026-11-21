# Prototypedokumentasjon — Trixig+

**Dette dokumentet beskriver hvordan en fungerende eller delvis fungerende prototype av redesignforslaget Trixig+ kan bygges. Det erstatter ikke den fysiske modellen, men gir spesifikasjoner, tegningsunderlag og en konkret produksjonsplan.**

---

## 1. Mål for prototypen

Prototypen skal demonstrere de tre kritiske endringene fra Trixig+:

1. **Reparerbar kapsling** — M3-skruer i støpte hylser, hus som åpnes uten skade.
2. **Utskiftbar batterimodul** — 18650-celle i fjærholder.
3. **Asymmetrisk retningsbryter** — taktil og visuell forskjell mellom forover/bakover.

I tillegg vises **statuslysstrip** og fjernet skjermbasert grensesnitt — disse er tilleggsdetaljer.

Prototypen trenger **ikke** å være elektrisk fungerende på første iterasjon. To prototypenivåer foreslås:

- **P1 — Foamprototype** (uten elektronikk): demonstrerer ergonomi, vekt, semantikk.
- **P2 — Funksjonell prototype** (med motor og batteri): demonstrerer faktisk drift.

---

## 2. Materialliste

### 2.1 P1 — Foamprototype

| Materiale | Mengde | Bruk |
|---|---|---|
| EVA-foam, 30 mm | 1 ark 300×300 mm | Skallhalvdeler |
| EVA-foam, 10 mm | 1 ark 200×200 mm | Avtrekker, retningsbryter |
| Sprayfilm, sort matt | 1 boks | Hovedfarge |
| Sprayfilm, lys grå | 1 boks | Avtrekker |
| Sprayfilm, oransje (RAL 2009) | 1 boks | Detaljmarkering |
| Lim (kontaktlim) | 1 tube | Sammenliming av lag |
| Smergelpapir, korn 240 og 400 | 1 ark | Forfining av kanter |
| Lommelyktdiode (dummy) | 1 stk | Visuell signifier |

**Estimerte materialkostnader:** ca. 250 NOK.
**Estimert byggetid:** 8–12 timer.

### 2.2 P2 — Funksjonell prototype

| Komponent | Spesifikasjon | Antall | Kilde |
|---|---|---|---|
| 3D-printet skall (PLA eller ABS) | egne STL-filer | 2 (over/under) | egen printer eller printbestilling |
| 18650 Li-ion celle | 3,7 V, 2 600 mAh | 1 | Clas Ohlson / Kjell |
| 18650 fjærholder med kontakter | enkel BMS-kompatibel | 1 | Aliexpress / Elfa |
| TP4056-modul | USB-C, ladekontroll | 1 | Aliexpress / Elfa |
| DC-motor 385-typen | 3,7–6 V, 5000–10 000 rpm | 1 | Elfa Distrelec |
| Planetgir for 385-motor | reduksjon ca. 60:1 | 1 | Elfa Distrelec |
| 1/4'' bitsholder med magnet | universell | 1 | Biltema / Bosch |
| Mikrobryter (avtrekker) | momentan, NO | 1 | Elfa |
| Vippebryter (retning) | DPDT, asymmetrisk | 1 | Elfa eller egendesignet |
| LED 5 mm hvit | 3,2 V, 20 mA | 1 | Elfa |
| LED 3 mm rød | for status | 4 | Elfa |
| Motstander 220 Ω, 1 kΩ | div. | et lite knippe | Elfa |
| M3 metallskruer × 16 mm | Torx T10 | 6 | byggevarehus |
| M3 hex-hylser, M3, 8 mm | innstøpt eller limt | 6 | Skruvat / Elfa |
| Ledninger 0,5 mm² | rød/sort/blå | 1 m | Elfa |
| Krymp-strømper | 2 mm og 4 mm | korte stykker | Elfa |
| Diode 1N4007 | beskyttelse | 1 | Elfa |

**Estimerte materialkostnader:** ca. 700–900 NOK.
**Estimert byggetid:** 25–35 timer (eks. 3D-printing).

---

## 3. Tegningsgrunnlag (utvendige hovedmål)

```
                FRONT (sett rett forfra)
                ────────────────────────

                     ┌────────┐         <- bitsfeste, 1/4''
                     │  ▒▒▒▒  │
                     ├────────┤
                     │ LED ●  │
                     │        │
   ┌─────────────────┘        └─────────────────┐
   │                                              │   <- TRIXIG-logo
   │                  HOVEDHUSET                  │
   │                                              │
   │                                              │
   └──────────────┐                  ┌────────────┘
                  │                  │
                  │                  │
                  │     GREP         │
                  │                  │
                  │  ┌────────┐      │
                  │  │ trigger│      │
                  │  └────────┘      │
                  │                  │
                  └──────┐    ┌──────┘
                         │    │
                         │stat│ <- statuslysstrip
                         │ ●●●○│
                         └────┘
                          USB-C

         Lengde A → B (nese til bunn av grep) :  ca. 175 mm
         Bredde av hovedhus                    :  ca. 60 mm
         Bredde av grep ved tommel             :  ca. 32–38 mm
         Vinkel mellom hovedhus og grep        :  ca. 110°
         Vekt målmål                           :  &lt; 400 g
```

(For en mer presis arbeidsfil, eksporter hovedformen til Rhino, Fusion 360 eller SolidWorks med en 3-vies (front/side/topp) i 1:1 og legg ved STL/STEP-eksport for 3D-printing.)

---

## 4. Bygging — P1 (foamprototype)

### Steg 1 — Oppmåling og lagdeling
Klipp 30 mm EVA-foam i fem like lag etter en mal som følger den ytre konturen. Fjern hjørner og myke kanter.

### Steg 2 — Limning
Sett ett lag i gangen med kontaktlim. Press 5 minutter mellom hvert lag. Bruk en treplate som mottrykk.

### Steg 3 — Forming
Bruk grovt smergelpapir til å avrunde kantene og skape den karakteristiske myke vinkelen mellom hovedhus og grep. Forfin med korn 400.

### Steg 4 — Detaljer
Klipp ut avtrekker og retningsbryter fra 10 mm-foam. Lim fast. Skap en synlig forskjell mellom retningsbryterens to sider — én konveks, én konkav. Test at fingrene kan kjenne forskjellen blindt.

### Steg 5 — Maling
Sprøyt sort matt på hovedhuset, lys grå på avtrekkeren, og bruk oransje sparsomt på retningsbryterens piler. La tørke 24 timer.

### Steg 6 — Finishing
Lim på en LED-dummy, en USB-C-rektangel (skåret av tynt plastikk), og en TRIXIG-tekst (klistremerke eller print).

---

## 5. Bygging — P2 (funksjonell prototype)

### Steg 1 — 3D-printing av skall

Eksporter STL-filer fra CAD med følgende toleranser:

- Veggtykkelse: 2,0 mm
- Skruekrager: ytre Ø 8 mm, innvendig boring Ø 3,2 mm med tilskudd for M3-hylse
- Toleranse mellom skall og batterirom: +0,3 mm i hver retning

Print med PLA, 0,2 mm laghøyde, 30 % infill, 3 perimeterlag. To skall (over/under).

### Steg 2 — Innstøping av M3-hylser

For hver av de 6 skruekragene: lim inn en M3-hexhylse (8 mm dyp) med tofase-epoksy. La herde 12 timer.

### Steg 3 — Elektrisk grunnkrets

Lodd opp følgende krets:

```
USB-C (TP4056) → 18650-celle (med BMS) → DPDT-vippebryter (retning)
                                       → Mikrobryter (trigger)
                                       → DC-motor
                                       → LED hvit (i parallell etter trigger)
                                       → LED rød (statusrekke, etter ladenivå)
```

Bruk diode 1N4007 i serie med motoren for tilbakestrømsbeskyttelse.

### Steg 4 — Mekanisk integrering

- Monter motor og planetgir i frontkammeret med to M2-skruer.
- Lim 18650-fjærholderen til ene skallet med tofase-epoksy. Test at cellen kan settes inn og ut uten skade.
- Monter PCB-modulen (TP4056 + småkomponenter) på en liten perfboard, fest med to M2-skruer i støpte krager.
- Lim mikrobryteren under avtrekkeren. Sjekk klikk og retur.

### Steg 5 — Avslutning

- Sett sammen skallene. Skru inn de seks M3-skruene med Torx T10. Kontroller at det ikke er gnissing mellom innvendige komponenter og skall.
- Test ladingen med USB-C-ladekabel.
- Test rotasjon i begge retninger.
- Test LED og statusrekke.

---

## 6. Test- og evalueringsplan

### 6.1 Ergonomi (P1 og P2)

Be 5 personer (4 nye, 1 ekspert) holde prototypen og:
- Identifisere blindt hvilken posisjon retningsbryteren står i (mål: 100 % suksess innen 2 sekunder).
- Trykke avtrekkeren med pekefingeren mens de holder grepet på normalt vis (mål: ingen ubehag).
- Vurdere vekt og balanse på en 5-punkts Likert-skala (mål: gjennomsnitt ≥ 4,0).

### 6.2 Holdbarhet (P2)

- Skall: åpne og lukke 50 ganger med M3-skruer (mål: ingen synlige skader på krager).
- Batteri: 10 inn/ut-syklus (mål: stabile kontaktverdier på multimeter).

### 6.3 Funksjonell ytelse (P2)

- Måle tomgangshastighet (mål: 150–250 o/min).
- Måle stalldreiemoment med fjærvekt (mål: ≥ 3 Nm — lavere enn 5 Nm pga. enkel motor og forenklet gir, men bekrefter prinsippet).
- Måle ladetid fra tom til full (mål: < 5 timer).

---

## 7. Dokumentasjon for sensur

For sensurpresentasjonen anbefales:

- **3 fotografier av P1**: front, side, og hånd-i-hånd-bilde.
- **3 fotografier av P2**: front, demontert, og under bruk.
- **1 kortvideo (15–30 s)** som viser P2 i drift.
- **Tegningsoppslag**: front, side, top, perspektiv. A3-format, henges sammen med plansjen.
- **CAD-eksport (STL eller STEP)** lagt ved digital innlevering.

---

## 8. Tidsplan (anbefalt rekkefølge)

| Dag | Aktivitet | Tid |
|---|---|---|
| 1 | CAD i Fusion 360 / Rhino | 6–8 t |
| 1–2 | 3D-printing (parallelt) | 8–14 t |
| 2 | P1 foamprototype | 8 t |
| 3 | Lodding av elektrisk krets, test på løsbasis | 6 t |
| 3–4 | Sammensetting av P2 | 8 t |
| 4 | Test og dokumentasjon | 6 t |
| 4 | Foto, video, plansjeoppdatering | 4 t |
| **Sum** | | **≈ 50 t** |

---

## 9. Risikoer og avbøtning

| Risiko | Sannsynlighet | Konsekvens | Avbøtning |
|---|---|---|---|
| 3D-printer feiler underveis | Høy | Forsinkelse 1 dag | Print to skall samtidig på to skrivere; ha foamprototype som fallback |
| Motoren har for lite dreiemoment for skikkelig demonstrasjon | Medium | Demonstrasjon halter | Bruk en større motor (775-typen, 12 V) i denne iterasjonen og dokumenter at endelig produkt har 385-typen |
| Ladekretsen overopphetes | Lav | Brann- eller røykfare | Bruk TP4056 med innebygd vern; bygg første prototype uten å lukke skallet |
| Asymmetrisk retningsbryter er vanskelig å skaffe ferdig | Høy | Forsinkelse | 3D-print egen vippepinne; lim på en standard DPDT-bryter |
| Prototypen blir for tung | Medium | Bryter med kravspes | Bruk lett PLA, kort av motor om nødvendig, vurder hule volumer |

---

## 10. Vedlegg til prototypedokumentasjonen

- *trixig_plus_skall_top.stl* (3D-modellen til øvre skall — opprettes i CAD)
- *trixig_plus_skall_bottom.stl* (3D-modellen til nedre skall)
- *trixig_plus_circuit.png* (skjematisk koplingsbilde — kan tegnes i Fritzing)
- *prototype_test_log.csv* (mal for testlogg under bruksevaluering)

(Disse filene må produseres under selve byggefasen og legges til prosjektmappen.)

---

*Slutten av prototypedokumentasjonen.*
