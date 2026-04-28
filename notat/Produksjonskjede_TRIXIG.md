# Produksjonskjeda for TRIXIG — kartlegging frå kobolt til kasserast

*Sjølvstendig leveranse til GK4 V26 Modul 2. Heilskapleg kartlegging av forsynings­kjeda, eigarstrukturen, materialledda, monteringsledda, distribusjonen, bruksfasen og end-of-life-handsaminga for IKEA TRIXIG 3,6 V. Knytt til Rapport_GK4_Trixig.md kapittel 5 og 10, og til Kritikk_av_IKEA_Trixig.md.*

Forfattar: [Studentnamn]
Dato: 27. april 2026.

---

## 1. Føreord

Eit produkt er ikkje ein gjenstand; det er eit nett av relasjonar. Når vi seier at TRIXIG er "laga av IKEA", lyver vi gjennom forenkling. IKEA *designar* TRIXIG, IKEA *brandar* han, IKEA *sel* han, og IKEA *koordinerer* leveransen. IKEA gjer ikkje sjølve produksjonen, og IKEA eig ikkje sjølve materialet. Skrutrekkaren passerer gjennom seks-sju strategiske ledd før han når kunden, og kvar overgang er eit punkt der både risiko og verdi vert handla med.

Dette dokumentet kartlegg dei ledda. Målet er todelt: å forstå kvifor produktet ser ut som han gjer (eg trur det meste forklarast nedover i kjeden, ikkje på designstudio), og å identifisera dei ledda Trixig+-redesignet faktisk endrar. Mange grep i Trixig+ er funksjonelle for sluttbrukaren men *strukturelle* for produksjonskjeda — dei flyttar friksjon frå brukar til produsent, eller frå avfallsstraum til reservedelsstraum. Skal redesignet vurderast som realistisk, må vi forstå kva som faktisk skjer mellom råvare og hylle.

## 2. Heilskapsoversikt

| Ledd | Geografi (typisk) | Aktør | Tidsbruk | Verdi-tilskot |
|---|---|---|---|---|
| 1. Råvareutvinning | DRC, Indonesia, Australia, Kina, Saudi-Arabia | Mining-konsesjonshaldarar, oljeselskap | år | låg, høg miljørisiko |
| 2. Råvareraffinering | Kina (cobalt, ABS), Sør-Korea, Japan (li-ion-celler) | LG Energy, CATL, BYD, Sinopec | månader | medium |
| 3. Komponent­fabrikasjon | Shenzhen, Guangdong, Zhejiang | OEM-fabrikkar (1000-talet) | veker | medium |
| 4. Sluttmontering | Sør-Kina (Shenzhen-Dongguan-corridor mest sannsynleg) | OEM-monterings­anlegg | dagar | medium-høg |
| 5. Kvalitetskontroll | Same fabrikk + IKEA-IWAY-audit | Tredjepart (Bureau Veritas, SGS, Intertek) | dagar | låg, men kritisk |
| 6. Sjøtransport | Shanghai/Ningbo/Yantian → Hamburg/Rotterdam/Göteborg | Maersk, Evergreen, MSC, COSCO | 4–6 veker | låg |
| 7. Distribusjons­senter | Älmhult, kontinental-EU, GXO-anlegg | Inter IKEA Group + 3PL | dagar | låg |
| 8. Butikk og e-handel | Kvar IKEA-butikk + ikea.com | Ingka Group | dagar | medium |
| 9. Bruksfase | Brukarens hjem | Sluttbrukar | år | n/a |
| 10. End-of-life | Kommunal WEEE-mottak | Kommune + WEEE-aktørar | månader | negativ |

Kjeden er global, fragmentert, og IKEAs direkte styring strekkjer seg eigentleg berre frå ledd 5 og utover. Råvare- og komponentledda er IKEAs leverandørs leverandørar — to-tre hopp unna IWAY-rammeverket, der handhevinga er svakast.

## 3. Råvarer og første ledd

### 3.1 Litium-ion-cella (18650-format)

Hovudkomponenten i TRIXIG er ein 18650 sylindrisk litium-ion-celle på 3,6 V og om lag 1,5 Ah. Cella inneheld katode (vanlegvis NMC — nikkel-mangan-kobolt-oksid), anode (grafitt eller silisium-karbon), elektrolytt (litium-salt i organisk løysemiddel), og separator (polypropylen/polyetylen). Kvar av desse har eigen forsynings­kjede.

**Kobolt** kjem nesten utelukkande frå Den demokratiske republikken Kongo (DRC), som står for om lag 70 % av global gruveproduksjon. Ein vesentleg del av denne produksjonen er artisanal — uregulerte, ikkje-mekaniserte gruver med dokumenterte tilfelle av barnearbeid. US Department of Labor sin lista over varer produsert med barnearbeid inkluderer kobolt frå DRC. Washington Post og fleire andre etablerte journalistiske kjelder har dokumentert arbeidsforholda. Frå gruva går kobolt­ertsen til Kina, der om lag 67 % av verdas raffinerings­kapasitet ligg. Kina importerte i 2024 kobolt for omtrent 3 milliardar USD frå DRC.

For ein 18650-celle er kobolt-innhaldet beskjedent — ein NMC811-celle (den vanlegaste i nyare verktøy) har under 5 gram kobolt per celle. Men når vi snakkar om titusenvis av TRIXIG-einingar produsert årleg, summerer det seg, og spor­barheita gjennom raffineringsledda er notorisk svak. IKEA har ikkje, så langt eg kan sjå, nokon spesifikk uttalt kobolt-sourcing-policy for sine elektroverktøy. Inter IKEA Group sin breiare bærekrafts­dokumentasjon nemner ansvarleg innkjøp av råvarer på prinsipielt nivå, men ikkje med bestemte cell-leverandørar.

**Litium** kjem frå tre hovudkjelder: salar i Chile, Argentina og Bolivia (saltsjø-utvinning), spodumen frå Australia (gruvedrift), og hard-rock-utvinning i Kina. Energi- og vassforbruk er høgt, særleg i saltsjø-utvinning der grunnvatns­uttak er kontroversielt i Atacama-ørkenen.

**Nikkel** kjem hovudsakleg frå Indonesia (over 50 % av global produksjon) og Filippinene. Indonesisk produksjon har dokumenterte miljøproblem knytt til avskoging og slam-deponi.

**Grafitt** for anodar kjem hovudsakleg frå Kina (om lag 70 % av syntetisk grafitt-produksjon).

### 3.2 ABS-plast for kapslinga

ABS (akrylnitril-butadien-styren) er eit termoplast-derivat av krudolje og naturgass. Råvarekjeden går: olje/gass-utvinning (Saudi-Arabia, Russland, USA, Norge for mindre del) → petrokjemisk raffinering → monomer-produksjon (akrylnitril, butadien, styren) → polymerisering. Kina dominerer produksjonen av ABS pellet, med over 3000 injection-molding-fabrikkar og betydeleg eksport av polymer­granulat.

Miljøaspekt: produksjonen er energi­intensiv og slipper ut betydelege mengder CO₂. Bruk av post-consumer recycled ABS (PCR-ABS) kan redusera CO₂-fotavtrykket per kilo plast med over 50 %, men krev tilbakelevert avfall, separasjons­anlegg, og kvalitets­kontroll-prosessar som ikkje er trivielle. TRIXIG har ikkje oppgitt rPCR-andel på produktbladet — det er ikkje ein opplyst verdi.

### 3.3 Andre material

**Stål** for skruver, fjør, motor­armatur, gearaksling: kjem frå global stålindustri, ofte kinesisk eller koreansk for billege komponentar.

**Kopar** for motorvikkling: hovudsakleg frå Chile (gruvedrift) raffinert i Kina eller Sør-Korea.

**Neodym** for magneten: nesten utelukkande frå Kina, som kontrollerer over 80 % av sjeldne-jord-raffinering globalt. Rare-earth-marknaden har dokumentert miljøproblem (radioaktivt avfall, jord­forureining) og er strategisk-geopolitisk monopolisert.

**Polykarbonat** og POM for trekkar og gear-komponentar: petrokjemisk derivat, lik kjede som ABS.

## 4. Komponent­fabrikasjon

Mellom råvare og monteringsledd ligg eit lag av komponent­fabrikantar som produserer cella, motoren, gearbox-en, PCB-en, brytaren, LED-en og kapsling-skall. Dette er den minst synlege delen av kjeden, fordi ingen einskild komponent er stor nok til å synast i IKEA si offisielle kommunikasjon.

**18650-cellene** produserast av nokre få store aktørar: BAK (Shenzhen), BYD (Shenzhen), CATL (Ningde), EVE Energy (Huizhou), LG Energy Solution (Sør-Korea), Samsung SDI (Sør-Korea), Panasonic (Japan). Dei billege variantane som typisk hamnar i prisklassa under 200 NOK kjem frå dei kinesiske aktørane. Kvalitetskontrollen i denne segmentet er kjent for å vera ujevn — celler frå same partia kan ha betydeleg variasjon i kapasitet og syklus-haldbarheit.

**Motor og planet-gear** produserast typisk av spesialiserte kinesiske mikromotor-fabrikantar i Pearl River Delta. Sett som integrert eining (motor + gear + bitsfeste) er dette ein modulær komponent som mange OEM-merker brukar med lett-modifisert kapsling.

**PCB-en** med USB-C-ladar og styringskrins er truleg laga i Shenzhen-området, der over 90 % av verdas forbrukar­elektronikk-PCB-ar produserast. Komponentane på PCB-en (mikrokontrollar, MOSFET-ar, LED-driver) kjem frå globale halvleiar­leverandørar (TI, ST, NXP, eller kinesiske ekvivalentar).

**Brytaren og avtrekkar­mekanismen** produserast i POM-injection-molding-fabrikkar, ofte i Zhejiang. Dette er prismekanikk-segmentet der marginar er små og kvalitets­kontroll er proporsjonal med pris.

**Kapsling-skalla** i ABS lagar OEM-fabrikken sjølv, eller kjøper frå nær­liggande plast-fabrikk. Det er her det meste av sluttproduktets visuelle identitet er bestemt — verktøy­merkene investerer mest i form og finish her, og minst i dei underliggande komponentane som dei kjøper modulært.

## 5. Sluttmontering

OEM-monteringa av TRIXIG-skrutrekkaren er, basert på bransjeanalyse av tilsvarande produkt, høgst sannsynleg lagd til Sør-Kina, anten i Shenzhen-Dongguan-Guangzhou-korridoren eller i Ningbo-området. Dei to dominerande aktørane som leverer OEM-handelsverktøy til europeiske detaljistmerker er Diversitech Global, Jakemy, og fleire mindre fabrikkar som spesialiserer seg på lågpris-elektroverktøy. Eg har ikkje funne offentleg dokumentasjon på den eksakte fabrikken som lagar TRIXIG, og IKEA opplyser ikkje den informasjonen i offentleg kanal.

Det vi kan vita er at produktet er FCC-registrert under "IKEA of Sweden AB" som ansvarleg part (FCC-ID FHOICBL10816USBC1 for batteripakken). FCC-registreringa er administrativ — produsenten er sjeldan den som sertifiserer. Sjølve fabrikken sit eit hopp unna.

Monteringa er typisk linjebasert: kapsling-halvdel i fixtur, motor-modul plassert, batteri-modul plassert, PCB tilkopla, kapsling-halvdel andre side på, skruver i, funksjonstest, pakking. Det meste av jobben er manuell, sjølv om dei mest moderne anlegga har automatisert delar av prosessen. Lønna i Pearl River Delta-fabrikkar er i 2025 typisk 4000–5500 RMB per månad (om lag 5500–7500 NOK) for ufaglærd montering, med varierande timetal og overtid.

Kvalitetskontrollen i denne pris­segmentet er ein kjent svakheit. AQL-1.5 (Acceptable Quality Level — den vanlege detaljist-spesifikasjonen) tillet om lag 1,5 % defektar i ein produksjonsbatch. For TRIXIG i prisklassa 199 NOK er AQL-2.5 eller høgare meir realistisk, noko som vil gi ein defektrate på 2–4 %. Dei feilrapportane vi ser i bruksrapportar (sjå Slakting_av_TRIXIG.md kapittel 2) ligg innanfor det som er forventa frå denne kvalitets­spesifikasjonen.

## 6. IKEA-eigarstruktur og kven gjer kva

IKEA er ikkje eit selskap; det er ein konstellasjon. Dei viktigaste einingar i kjeden er:

**Inter IKEA Group** (registrert i Nederland, hovudkontor i Älmhult, Sverige): Eig konseptet IKEA, varemerket, designforpliktingar, sortimentet og forsyningskjeden. Dette er der TRIXIG faktisk er "skapt" som produkt-konsept.

**IKEA of Sweden AB** (Älmhult): Designar, utviklar og lagar — i meininga "definerer spesifikasjonar og koordinerer produksjon" — TRIXIG. Dette er nominelt produsenten i juridisk forstand.

**Inter IKEA Industry** (med fabrikkar i Slovakia, Sverige, Russland før 2022, fleire stader): Eig in-house produksjon for 10–12 % av IKEA-sortimentet, hovudsakleg trømøblar (BILLY, PAX). **Lagar ikkje TRIXIG.**

**Ingka Group** (eigar dei fleste IKEA-butikkane globalt): Sel til sluttkunden. Driv også ein del av Buy-Back- og reservedels­operasjonen.

**IKEA Components** (Älmhult): handterer sortiments­utvikling og kunde­service for komponent-segmentet. Truleg ikkje direkte i TRIXIG-kjeden.

**Inter IKEA Sourcing** (operasjonelle hub i Asia): forhandlar fram kontrakter med OEM-leverandørar, organiserer kvalitetskontroll og logistikk.

Det avgjerande er at den faktiske fysiske TRIXIG vert lagd av ein ekstern OEM som Inter IKEA Sourcing har kontrakt med. IKEA er ein kontraktshaldar og distributør, ikkje ein produsent. Det betyr at endring av TRIXIG-spesifikasjonar (Trixig+) krev forhandling med OEM-en, ikkje internt vedtak.

## 7. IWAY — kva det dekkjer, kva det ikkje dekkjer

IWAY er IKEAs supplier code of conduct, lansert i 2000 og oppdatert fleire gonger. Han er obligatorisk for alle leverandørar og dekkjer:

- Maksimum 60 timar arbeids­veke
- Minimum seks timars samanhengande kvile per 24 timar
- Forbod mot barnearbeid
- Forbod mot tvunge eller bunde arbeid
- Krav til lønnsutbetaling
- Sosial forsikring
- Tilsvarande bestemmelsar for animal welfare og miljø

IKEA gjennomfører jamlege, ofte uannonserte, audits gjennom både eigne og tredjeparts­revisorar. Ved avvik krev IKEA at leverandøren identifiserer rotårsak og korreksjon innan 90 dagar.

**Det IWAY ikkje dekkjer godt nok:**
- Det dekkjer berre direkte leverandørar (Tier 1) — sub-leverandørar (Tier 2 og 3, t.d. cell-fabrikanten som leverer til OEM-en) er utanfor direkte handheving.
- Det er ein "compliance"-modell, ikkje ein "improvement"-modell — auditor kjem, registrerer, dokumenterer korreksjon, går vidare. Det skapar ikkje strukturell endring av lønnsnivå eller arbeidsforhold.
- Råvareutvinningsledda (kobolt-mining i DRC, neodym-utvinning i Kina) er heilt utanfor IWAY si rekkevidde.
- Leverandørar har incentiv til å produsera ein "audit-versjon" av fabrikken som er forbetra på inspeksjonsdag og normalisert resten av tida.

IKEA har ein offentleg uttalt "view on forced labour" og engasjerer seg i International Labour Organization-prosjekt, men det breiare kobolt- og elektronikk-økosystemet IWAY ikkje når strekt seg langt forbi IKEAs synsfelt.

## 8. Logistikk og distribusjon

Frå OEM-fabrikk i Sør-Kina til norsk butikkhylle er reisa typisk 6–8 veker. Containerar går frå hamn (oftast Yantian, Ningbo eller Shanghai) på linjeruter til Hamburg, Rotterdam, Antwerpen eller Göteborg. Frå europeisk hamn med jernbane eller tungtransport til IKEAs distribusjons­senter (DC).

IKEAs DC-nettverk er drifta delvis av Inter IKEA, delvis av eksterne 3PL-aktørar. GXO Logistics har eit IKEA-DC i Storbritannia som er rangert som det meste effektive i IKEAs globale nettverk. Älmhult er kjernen for sortiments-koordinering. For Norden er Göteborg-hamna inngangsporten; for Norge går varene vidare med tungtransport til Vestby (sør for Oslo) eller Furuset.

Frå DC til butikk er det dagleg eller fleirgongs-veka-leveransar. TRIXIG er liten og veg lite — han vert pakka i kompakte kvitfargkartongar (UV-printa direkte frå designspesifikasjon) og stabla i mengder. Containerfrakt-fotavtrykket per eining er låg, kanskje 50–80 g CO₂-ekvivalent for skip-reisa, men *summen* over heile produktets liv (frakt + butikkdrift + kunde-bil-tilbakekast) er ofte den minste delen av total fotavtrykk; produksjons- og bruksfasen dominerer.

Buy-online-pickup-in-store er den raskaste vekstkanalen. ikea.com sin direkte-til-kunde-leveranse går oftast via lokal 3PL (PostNord i Norden, DPD/DHL i kontinental-EU), ikkje IKEAs eige nett.

## 9. Bruksfasen

TRIXIG hamnar i ein heim. Han vert lada via USB-C — ein fordel for kundens fleksibilitet, men implikasjon for ladings-tap (USB-C-ladar har 75–85 % effektivitet, mot 90–95 % for direkte vegglading). Lagring mellom bruk er typisk i ein skuff eller på ein hylle. Cella sjølv-utlader langsamt (1–3 % per månad ved romtemperatur) og krev periodisk re-charging for å ikkje degradera. IKEAs manual seier at cella må ladast minst kvar tredje månad — dette er ein praktisk konsekvens av at cella er innelodda. Brukaren kan ikkje fjerna cella for langtidslagring; han må disiplinera ladings­rytmen.

Reell bruksfrekvens for primærbrukaren (DIY-monterar, ikkje profesjonell) er låg-intensiv: 4–8 timar samla aktiv tid per år, fordelt over 5–15 episodar. Total ladesyklusar over levetida er typisk 40–80, godt under cellens nominelle 300–500 syklusar — men det er likevel cella sin sjølv-degradering over kalender­tid, ikkje syklus-tal, som ofte avgjer levetida i denne brukspatternen. Etter 5–7 år har sjølv ein lite-brukt 18650-celle mista 40–60 % av nominell kapasitet, og verktøyet vert "tom" innan ein time bruk.

## 10. End-of-life

Når TRIXIG ikkje lenger fungerer, oppstår eit avfallsproblem som er strukturelt utfordrande.

**WEEE-direktivet** (EU 2012/19/EU) krev at e-avfall vert samla separat frå vanleg restavfall. Forbrukaren kan returnera produktet gratis til kommunal mottakssentral eller til detaljist (IKEA er forplikta som detaljist å ta imot). Produsenten er ansvarleg for finansiering av avfallshandsaminga gjennom WEEE-avgift.

**Litium-batteri** krev særleg handsaming — dei må fjernast før hovudprosessering, fordi dei kan skapa brann ved punktering. For TRIXIG, der cella er innelodda, krev dette demontering av profesjonelt avfalls­selskap. Det er ein arbeidsintensiv operasjon som er kostnadsdrivande, og i praksis hender det at innelodda cellar går gjennom shredding-anlegg utan separat fjerning, med påfølgjande brannrisiko og redusert materialretur.

**Material­retur** av TRIXIG er suboptimal. Utan ISO 11469-merking på utvendig flate kan ABS-en ikkje sorterast etter polymer­type utan kjemisk analyse. POM-trekkaren er ein annan polymer­fraksjon. Stålet i skruver, motoren og bitsfestet er teknisk separabel, men i praksis vert det ofte sendt som "blanda metall" til lågkvalitets­resirkulering. Neodym-magneten — eit verdifullt sjeldne-jord-element — vert nesten alltid tapt i shredding, fordi gjenvinning krev dedikert prosess som ikkje er økonomisk lønsam for ein einsleg lite magnet.

**IKEAs Buy-Back-program** dekkjer ikkje TRIXIG eller andre verktøy. Det er avgrensa til større møblar. Det betyr at verken IKEA eller forbrukaren har eit etablert kanal for retur, og dei fleste TRIXIG-einingane endar i kommunal e-avfall, om dei ikkje rett og slett vert kasta i restavfall (som er ulovleg men hender).

## 11. Kva endrar Trixig+ i kjeden?

Trixig+-redesignet ser ved første blikk ut som ei design-endring. I praksis er han ein endring av kjedestrukturen i fleire ledd.

**Råvareledd:** ingen direkte endring. Cella er framleis 18650, kobolt frå DRC framleis dominerande. Men *fordi* cella no er utskiftbar, vert *kvar einskild celle* mindre kritisk per produkt-livssyklus — produkta vil bruka færre celler totalt over levetida fordi forholdet mellom celle-inneverdi og produkt-arbeidstid stig.

**Komponentledd:** ny komponent introdusert — fjærkontakt-batteriholder. Dette er ein standard komponent som finst i hyllevare frå mange leverandørar; ingen nye OEM-relasjonar krevst. Asymmetrisk retningsbrytar krev ny støypeform (mould tooling), engangskostnad ca. 15 000–25 000 USD. Status-LED-stripa krev tillegg på PCB-en, små komponentkostnadar.

**Sluttmontering:** seks Torx T10-skruver erstatter seks selvskruver. Same monteringstid. Tilleggssteg: messinghylser pre-instøypt i ein av skall-halvdelane. Ein lett ekstra steg i støypings­prosessen, ikkje i monteringa.

**Kvalitetskontroll:** auka kontroll på batteriholder-funksjon (fjærkontakt-passform, isolasjon). Lite kostnadsvekst på prov-test.

**Logistikk:** ingen endring i hovudproduktet. *Ny vare­linje* introdusert: TRIXIG 3,6 V reservebatteri, sel separat. Dette må produserast, pakkast, lagrast og distribuerast — ein ekte ny SKU. Inter IKEA Sourcing må sourca cella separat frå sluttproduktet. Produktet sin batteri-kategori-kanal er allereie etablert (12 V batteripakken sel separat under same logistikk-paraply); marginalkostnad for å leggja til 3,6 V-versjonen er låg.

**Bruksfase:** levetidsforlenging frå estimerte 5–7 år til 12–15 år. Brukaren har éin årleg eller toårleg utskiftings­handling.

**End-of-life:** materialfraksjonar er separable. ISO 11469-merking gjer at avfalls­behandlaren kan sortera. Batteriet er fjernbart utan profesjonell demontering. WEEE-avgifta per eining vil sannsynlegvis falla noko fordi behandlinga er enklare. IKEA Buy-Back kan utvidast til verktøy med liten ekstrakostnad — det reduserer brukar­friksjon for retur.

**IWAY:** ingen direkte endring, men auka kompleksitet i forsyningskjeda krev tilsvarande utvida audit. Reservebatteri-leverandøren må gå gjennom IWAY-godkjenning.

Sum: redesignet endrar ikkje grunnstrukturen i kjeden, men introduserer ein ny SKU, ein ny komponent (batteri­holder), og ein endra mould tool. Total inkrementell kostnad: 11 NOK per eining produsert, ca. 25 000 USD i mould-investering, ca. 200 000 USD i nytt-SKU-introduksjon for reservebatteri. På IKEA-skala (anslagsvis 100 000–500 000 einingar per år for TRIXIG 3,6 V) er dette små tal, fullt finansierbart innanfor normale produkt­utviklingsbudsjett.

## 12. Det viktigaste eg kunne lært meir om

Tre konkrete spørsmål eg ikkje fullt ut har svara på, men som er kritiske for ein verkeleg tett forsynings­kjede-analyse:

**For det første:** kven er den faktiske OEM-en som lagar TRIXIG? IKEA opplyser ikkje, og søk på FCC-registreringa peiker tilbake til IKEA of Sweden AB som administrativ part. Eit felt­besøk eller ein direkte førespurnad til Inter IKEA Sourcing i Hong Kong eller Shanghai ville vore det einaste pålitelege svaret.

**For det andre:** kva er den reelle reklamasjonsrate for TRIXIG i Norden? Trustpilot-omtaler er sjølvselekterte (negative røyster overrepresenterte). IKEA har internt data, men dei er ikkje offentlege. Forbrukartilsynet i Norge har ikkje publisert sak om TRIXIG spesifikt så langt eg kan sjå.

**For det tredje:** kva er karbon-footprintet per eining over heile livssyklusen? Eit reelt LCA (Life Cycle Assessment) ville krevd kjernedata frå OEM-en og frå cell-leverandøren, og tilgjengelege LCA-modellar for tilsvarande produkt antydar 4–8 kg CO₂-ekvivalent per eining over 10 års bruk, dominert av produksjonsfasen (60 %), batteri (20 %), og end-of-life-handsaming (15 %). Denne fordelinga er den sterkaste grunnen til å forlengja levetida — kvar produsert eining er den dyre delen, ikkje kvar bruksdag.

---

## Kjelder

- [TRIXIG screwdriver, lithium-ion, 3.6 V — IKEA US](https://www.ikea.com/us/en/p/trixig-screwdriver-lithium-ion-20566969/)
- [TRIXIG Battery Pack ICBL10816USBC1 — FCC ID FHOICBL10816USBC1](https://fccid.io/FHOICBL10816USBC1)
- [Inter IKEA Group — Our business in brief](https://www.inter.ikea.com/en/this-is-inter-ikea-group/our-business-in-brief)
- [IKEA of Sweden — Wikipedia](https://en.wikipedia.org/wiki/IKEA_of_Sweden)
- [IWAY — IKEA supplier code of conduct](https://www.ikea.com/global/en/our-business/how-we-work/iway-our-supplier-code-of-conduct/)
- [IWAY for Inter IKEA Group supply chain](https://www.inter.ikea.com/en/how-we-do-business/how-we-work-with-our-suppliers/iway-for-inter-ikea-group-supply-chain)
- [IKEA — Our view on forced labour](https://www.ikea.com/global/en/our-business/our-view-on/forced-labour/)
- [IKEA Case: One Company's Fight to End Child Labor — Markkula Center](https://www.scu.edu/ethics/focus-areas/business-ethics/resources/ikea-case-one-companys-fight-to-end-child-labor/)
- [GXO distribution center named No. 1 in IKEA's global network](https://gxo.com/news_article/gxo-distribution-center-named-no-1-in-ikeas-global-network/)
- [Inside IKEA: The Wonderful Everyday — Manufacturing Digital](https://manufacturingdigital.com/articles/inside-ikea-the-wonderful-everyday)
- [Diversitech Global cordless screwdrivers manufacturer](https://www.diversitech-global.com/cordless-screwdrivers-manufacturer-china)
- [ILAB Lithium-ion Batteries Storyboard — US Department of Labor](https://www.dol.gov/agencies/ilab/reports/child-labor/list-of-goods/supply-chains/lithium-ion-batteries)
- [Cobalt mining for lithium-ion batteries has a high human cost — Washington Post](https://www.washingtonpost.com/graphics/business/batteries/congo-cobalt-mining-for-lithium-ion-battery/)
- [Ethical Concerns in Battery Production — Battery Buddy](https://batterybuddy.eu/safety/ethical-concerns-in-battery-production-cobalt-and-rare-materials-sourcing)
- [Cobalt and lithium global supply chains — ResearchGate](https://www.researchgate.net/publication/374025137_The_cobalt_and_lithium_global_supply_chains_status_risks_and_recommendations)
- [Reducing Reliance on Cobalt — US DOE](https://www.energy.gov/eere/vehicles/articles/reducing-reliance-cobalt-lithium-ion-batteries)
- [WEEE Directive — Pronexa](https://pronexa.com/blog/recycling-of-e-waste-and-batteries-the-weee-directive/)
- [EU Batteries Regulation 2023/1542 — EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/1542/oj)
- [China ABS Plastic Injection Molding — Prolean Tech](https://proleantech.com/china-abs-plastic-injection-molding/)
- [Environmental Impact of Plastic Injection Services — Mulan](https://www.china-plasticparts.com/a-the-environmental-impact-of-plastic-injection-services.html)

---

*v1.0 — 27. april 2026. Heilskapleg kartlegging av forsynings­kjeda, basert på offentleg tilgjengelege kjelder. Tre spørsmål er igjen ubesvart (sjå kapittel 12) og krev direkte kontakt med Inter IKEA Sourcing for fullstendig verifikasjon.*
