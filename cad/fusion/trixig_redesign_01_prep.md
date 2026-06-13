# TRIXIG redesign_01 — Blender prep for Fusion rebuild (2026-06-13)

Source: Blender scene **`redesign_01`** in `trixig_original_and_drafts.blend`.
This documents the sectioning / parting-split / screw layout done on the new sculpt and
the data exported for rebuilding it parametrically in Fusion 360 (next phase, via Fusion MCP).
Mirrors the recipe of the existing master **"IKEA TRIXIG 3.6 original"**
(see `trixig_cad_rebuild_notes.md`).

## Source geometry (in `redesign_01`)

- **`main shell.001`** — 527k-vert hand sculpt = body + grip clamshell. Not watertight
  (147 open edges). This is the part that gets split at Y=0.
- **`front_shell.001`** — separate **nose cap** (X < −159), a distinct molded part; not part
  of the Y=0 body clamshell. Rebuild as its own part in Fusion.
- Accents: `triggere.001`, `reverse.004/005` (fwd/rev rocker), `detail.002/003`, `bit_holder.001`.

All prep work lives in a new collection **`redesign_01_prep`** (delete to revert; the sculpt
master is untouched — work was done on a duplicate `prep_shell_solid`).

## Frame & key dimensions (redesign_01 world, mm)

- **Parting plane = world Y = 0** (global XZ plane). Sculpt is symmetric about it
  (Y centroid 0.06 mm). Split convention: `Shell_Front_pY` (+Y) / `Shell_Back_nY` (−Y),
  same as master's Body_Front/Body_Back.
- Main-shell extents: X [−178.2, 0.6], Y [−24.5, 24.0], Z [3.7, 125.1].
  Full housing (with nose) reaches X −211 (bit-holder/spindle tip).
- **Drive axis**: world −X, at Y = 0, Z = 97.2. Spindle tip at X −211, motor rear at X −104.6.
- Base (lowest point, USB-C/lanyard): X ≈ −45, Z ≈ 3.7. Rear heel: X 0 … −15.

## Internal components (proxies fitted; full meshes exist on disk)

From documented caliper teardown (`assets/reference/teardown/`,
`trixig_motor_girmodul.py`, `trixig_pcb_battery_blender.py`):

- **Motor/gearbox** (total 106.4 mm) on the drive axis: can Ø32×47 → gearbox Ø35×32.4 →
  front boss Ø18×3 → shaft Ø10×24. World X −104.6 (rear) → −211 (tip), Z 97.2, Y 0.
- **PCB+battery**: PCB 95.39×26.31×1.6 with 18650 Ø18.6×65.0 stacked on top (stack ≈20.2).
  Stands raked in the handle: motor-wire end ≈ (−105, 0, 90), **USB-C end at the base**
  ≈ (−45, 0, 12); axis dir (0.61, 0, −0.79), board normal (0.79, 0, 0.61).
- Faithful meshes if needed: `cad/fusion/pcb_battery_asset/trixig_pcb_battery_scaled.obj`,
  `cad/print/trixig_redesign/for_bambu/{motor_gear_module,pcba_board}.stl`.

## Screw system — 5 bosses (final, user-reviewed)

Clamshell screws on the Y=0 plane, **axis along Y**. Spec: Ø2.4 pilot, Ø8.6 × 10 boss,
**M3×12 self-tapping** (matches prior print build `screw_m3x12_0X.stl`).
Layout was placed clear of all keep-outs (motor, battery, fwd/rev rocker, trigger, and the
**base strap/USB cord passage** — deliberately left screw-free), then adjusted by the user:
the original rear-mid screw was removed (→ 5 total) and S1/S2 moved forward to flank the thin
nose shaft at the `front_shell` junction (X < −178) rather than the fat gearbox.

| Screw | X | Z | role |
|---|---|---|---|
| S1 | −189.2 | 110.5 | nose/shaft, top |
| S2 | −189.9 | 83.2  | nose/shaft, bottom |
| S3 | −98.7  | 114.9 | upper body |
| S4 | −69.3  | 34.3  | grip, low |
| S6 | −10.0  | 60.0  | rear heel |

(`screws.json` holds the authoritative coordinates.)

## Debossing

Use repo **`ikea.svg`** (IKEA wordmark, viewBox 751×138, single path, #0058A3) — NOT the
in-scene grease-pencil `ikea.svg`. Per master: badge 38×13 mm R3.5 raised on +Y shell;
wordmark 33 mm wide, debossed 0.4 mm, A-counter island preserved.

## Exported handoff — `cad/fusion/redesign_01/`

| File | Use |
|---|---|
| `sections.json` | Y0 silhouette (78-pt, [X,Z]) + 7 transverse stations (uv + plane co/normal). Primary Fusion sketch input. Ignore loops < 8 pts (sculpt noise). |
| `parting_Y0.dxf` / `.svg` | Y0 silhouette, manual-insert fallback (true mm). |
| `screws.json` | 6 positions + fastener spec. |
| `internal_layout.json` | Motor + PCB/battery placement. |
| `Shell_Front_pY_mm.stl` / `Shell_Back_nY_mm.stl` | Split halves, mm, as visual/measure reference (solid, not yet shelled). |

## Fusion rebuild recipe (next phase, via Fusion MCP)

1. Insert/loft the **Y0 silhouette** (sections.json) on the XZ plane → main solid; refine
   profile against the transverse stations.
2. Split on Y=0 → Body_Front (+Y) / Body_Back (−Y).
3. **Shell to 1.6 mm** (remove pilots/bosses first, re-add after — small/raised features
   can't offset; see master gotchas).
4. Add 6 Ø8.6 bosses on Body_Back at the screw (X,Z); Ø2.4 pilots through both halves.
5. Badge + debossed IKEA wordmark on +Y shell.
6. Openings: fwd/rev rocker slot, USB-C pill at the base.
7. Nose cap (`front_shell`) as a separate part around the gearbox/spindle.

## Caveats

- Sculpt is not watertight; STL halves are solid blocks (Fusion rebuilds clean surfaces from
  the section profiles — the meshes are measurement references only).
- Component proxies are envelopes from caliper dims; placement verified visually against the
  Y0 outline but is ±a few mm — re-confirm clearances once Body shells exist.
- No Fusion MCP was connected during this prep; the rebuild is the next session.
