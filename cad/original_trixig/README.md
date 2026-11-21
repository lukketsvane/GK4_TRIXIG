# Original IKEA TRIXIG 3,6 V: målte CAD-delar

Dette er dei CAD-modellerte delane frå den demonterte originalen, samla på éin stad. Dei er grunnlaget for 3D-modelleringa av redesignen.

![Alle delane med mål](delar_oversikt.png)

![Samanstilling med gjennomsiktig skal](samanstilling_rontgen.png)

## Innhald

- `delar/`: 20 delar som STL i millimeter, i samanstillingsposisjon. Importer dei samla, så passar dei i hop.
- `komponentar/`: motor, girkasse, kretskort og celle, modellerte frå skyvelære-mål i eigne koordinatar.
- `delar_oversikt.png` og `samanstilling_rontgen.png`: oversiktsbileta over.

## Kjelde

- **Skal, panel, brytarar, bitshaldar, stropp og skruer** kjem frå Fusion-dokumentet «IKEA TRIXIG 3.6 original» i prosjektet «IKEA Redesign GK4». Arbeidet er skildra i [`cad/fusion/trixig_cad_rebuild_notes.md`](../fusion/trixig_cad_rebuild_notes.md).
- STL-filene er eksporterte frå `public/assets/00_trixig_parts.glb` i repoet `trixig.iverfinne.no`.
- **Motor og kretskort** finst i to variantar:
  - fotoskann i rett posisjon i samanstillinga (i `delar/`)
  - modellar laga frå skyvelære-mål (i `komponentar/`)

## Koordinatar

- Eininga er millimeter.
- Y peikar opp, X går langs drivaksen og Z er breidda.
- Bitsspissen ligg ved X ≈ −323. Drivaksen ligg 110,5 mm over botnen (Y = 110,5).
- Delingsplanet mellom dei to skalhalvdelane er Z = 0.

## Delar i `delar/`

Måla er storleiken på delen i samanstillinga, som lengd (X) × høgd (Y) × breidd (Z).

| Fil | Del | Mål (mm) | Merknad |
|---|---|---|---|
| `skal_front.stl` | Skalhalvdel, front | 155,9 × 133,6 × 23,1 | Veggtjukkleik 1,6 mm, førehol Ø2,4 for skruene |
| `skal_bak.stl` | Skalhalvdel, bak | 155,9 × 133,6 × 23,1 | Veggtjukkleik 1,6 mm, seks skrueboss Ø8,6 × 10 |
| `toppanel.stl` | Toppanel med logo | 55,0 × 7,6 × 21,5 | |
| `toppanel_detalj.stl` | Rund lyseblå del i hòlet i toppanelet | 5,9 × 2,0 × 5,8 | Funksjonen er ikkje stadfesta |
| `avtrekkar.stl` | Avtrekkar | 37,2 × 31,0 × 18,5 | Heiter «Button» i GLB-fila |
| `retningsbrytar.stl` | Retningsbrytar fram/bak | 8,9 × 4,6 × 41,3 | Går tvers gjennom skalet |
| `bitshaldar.stl` | Bitshaldar | 38,4 × Ø12,7 | Aksel Ø10,1, flens Ø12,7, ¼″ sekskant 6,5 AF × 13 |
| `bitshaldar_innlegg.stl` | Innlegg inne i bitshaldaren | 3,1 × 6,6 × 6,5 | Truleg magneten |
| `arbeidslys_linse.stl` | Liten linse under nasen | 5,7 × 4,0 × 3,9 | Truleg arbeidslyset |
| `usb_c_kontakt.stl` | USB-C-kontakt | 5,6 × 7,9 × 9,0 | I botnen av grepet, opning 9,2 × 3,4 |
| `lysleiar_3_led.stl` | Lysleiar for tre LED-ar på kretskortet | 16,4 × 16,4 × 6,5 | Heiter «Trigger» i GLB-fila |
| `stropp.stl` | Stropp med wirebøyle | 159,9 × 19,3 × 3,6 | Wire Ø3,5 |
| `skrue_01.stl`–`skrue_06.stl` | Skruer, 6 stk | Ø5,6 × 15,3 | Gjenge Ø2,8 × 13, hovud Ø5,6 × 2,2 |
| `motor_girkasse_fotoskann.stl` | Motor og girkasse | 108,7 × 41,6 × 38,5 | Fotoskann i rett posisjon |
| `pcb_batteri_fotoskann.stl` | Kretskort med 18650-celle | 39,2 × 82,2 × 24,3 | Fotoskann, skråstilt i grepet |

## Målte komponentar i `komponentar/`

| Fil | Komponent | Mål (mm) | Laga med |
|---|---|---|---|
| `motor_girkasse_malt.stl` | Motor og girkasse | Motor Ø32 × 47, girkasse Ø35 × 35,4 (inkl. frontboss Ø18 × 3), aksel Ø10 × 24. Totalt 106,4 | [`cad/fusion/trixig_motor_girmodul.py`](../fusion/trixig_motor_girmodul.py) |
| `pcb_battery_asset/` | Kretskort med 18650-celle, i Blender, GLB, OBJ og STL | Kretskort 95,39 × 26,31 × 1,60, celle Ø18,60 × 65,02 | [`trixig_pcb_battery_blender.py`](../fusion/trixig_pcb_battery_blender.py) og [`trixig_pcb_battery_print_stl.py`](../fusion/trixig_pcb_battery_print_stl.py) |

## Hovudmål for originalen

Kjelde: [`cad/fusion/trixig_cad_rebuild_notes.md`](../fusion/trixig_cad_rebuild_notes.md).

- **Totalt utan stropp:** 171,4 × 133,6 × 46,1 mm (lengd × høgd × breidd), med bitshaldaren.
- **Tønna:** Ø45,6 ved skuldra og Ø44,7 lenger fram. Nasen smalnar inn til Ø16,4.
- **Grepet:** ovalt, 44,4 × 33,0 mm, og skråstilt om lag 17–19° frå loddrett.
- **Skalet:** veggtjukkleik 1,6 mm.

## Printfilene i `cad/print/trixig_redesign/for_bambu/`

Dei same delane ligg der som printfiler, men fleire filnamn er feil, og skalet er ufullstendig. Bruk filene i denne mappa når du modellerer.

| Fil i `for_bambu/` | Tilsvarar |
|---|---|
| `motor_gear_module.stl` | Avtrekkaren |
| `pcba_board.stl` | Toppanelet |
| `internal_wire.stl` | Retningsbrytaren |
| `shaft_collar_assy.stl` | Bitshaldaren |
| `front_end_cap.stl` | Lysleiaren for tre LED-ar |
| `rear_end_cap.stl` | Linsa under nasen |
| `bit_holder_cover.stl` | Innlegget i bitshaldaren |
| `direction_switch.stl` | Detaljen i toppanelet |
| `trigger_button.stl` | Truleg USB-C-kontakten (litt andre mål) |
| `lanyard_strap.stl`, `screw_m3x12_01`–`06.stl` | Stroppen og skruene (rette namn) |
| `pcb_battery_simplified_print_mm.stl` | Forenkla kretskort med celle (rett namn) |
| `housing_bottom_grip.stl` | Ei skalhalvdel utan nase (135,9 mm lang) |
| `housing_bottom_tip.stl`, `housing_top_tip.stl` | Øydelagde fragment |
| `housing_top_grip.stl` | Tom fil |
