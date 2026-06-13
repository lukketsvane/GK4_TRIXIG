# TRIXIG 3.6 — parametric CAD completion (2026-06-12)

Fusion document: **"IKEA TRIXIG 3.6 original"** (project *IKEA Redesign GK4*), saved v3+.
Part Design document → parts are **named bodies at root** (Part Design docs cannot hold
components/occurrences; insert this part into a separate assembly design if needed).

## What was completed this session (via Fusion MCP scripting)

1. **Split + shells** — `Body_Main` split on the XZ plane (Y=0 parting plane) into
   `Body_Front` (+Y) / `Body_Back` (−Y); both shelled to **1.6 mm** wall
   (2.0 / 1.8 mm offsets fail on the screw-well and pocket geometry — 1.6 is
   consistent with the real product's molding).
2. **Screw system** — back half got six Ø8.6 × 10 mm bosses on the screw axes;
   Ø2.4 pilots re-drilled through front wall + bosses from the original
   `Screw_Pilots` sketch. (Pilot + strap-pin features had to be removed before
   shelling — Ø2.4/Ø3.0 features cannot be offset inward 1.6 mm — then re-created.)
3. **Strap pin** re-added on `Body_Back` (clip bail wraps it).
4. **Badge + IKEA wordmark** — raised rounded-rect badge (38 × 13 mm, R3.5, ~0.7–1.3 mm
   proud, rim fillet R0.8) on the +Y shell at centre (−237, 110.8); wordmark debossed
   0.4 mm from `ikea.svg` path data (33 mm wide, A-counter island preserved).
   Sketches: `Badge_Outline`, `Wordmark`.
5. **Fwd/rev rocker** — through-slot (9.4 × 5.2 pill) + `Switch_FwdRev` bar body
   (8.8 × 4.6 × 43, rounded ends) at scan position X −234.4…−225.6, Z 93.2…97.8.
6. **USB-C opening** — 9.2 × 3.4 pill cut in the handle base at (−171.5, 0), per scan.
7. **Appearances** — custom `TRIXIG Brown ABS` (62,46,40) shells,
   `TRIXIG Accent GrayBlue` (198,206,212) for panel/buttons/clip/rocker,
   Stainless Steel Satin bit holder, matte black screws/LED.

## Reference dimensions extracted from the Blender concept model (mm)

- Overall 170 × 46.1 × 133.6; parting plane Y=0; drive axis Z = 110.5.
- Barrel Ø45.6 shoulder → Ø44.7, front face X −308.7, nose cone to Ø16.4;
  elbow bend starts ~X −223, centreline bend R≈25.8, turn ≈71°.
- Grip oval 44.4 × 33.0, raked ~17–19° from vertical; domed base.
- Screw positions (X, Z): (−295.7, 98.4), (−295.7, 122.7), (−211.7, 121.1),
  (−196.8, 44.0), (−187.7, 91.5), (−163.2, 12.8); thread Ø2.8 × 13, head Ø5.6 × 2.2.
- Bit holder: shaft Ø10.1, flange Ø12.7, ¼″ hex socket 6.5 AF × 13, tip at X −323.
- Wire bail Ø3.5, hairpin to X −9, legs ≈Z 10.4 / 17→22.

## Known simplifications

- Grip cross-sections are ellipses (≤1 mm fuller than the scanned egg-profile at the
  front shoulders).
- Front screw holes use the original Ø2.4 pilot size (no separate Ø3.4 clearance).
- Panel/buttons are drop-in fits; no snap clips modeled.

## Fusion MCP scripting gotchas (hard-won)

- A script that throws **rolls back everything it did** — guard verification code.
- `Path.create()` needs occurrence **proxies** (`createForAssemblyContext`) for curves
  inside components; root-level curves are fine.
- Loft rails pinned to scan silhouettes beat centerlines for accuracy; loft tangency
  conditions only accept **BRepEdge** sections.
- Shell fails (`ASM_LOP_TWK_*`) on any face that can't offset by the wall thickness:
  holes < 2×wall, knife-edge pocket walls, raised badge pads → do those features
  **after** the shell.
- Part Design documents cannot create occurrences via API.
- A modal command dialog (e.g. MOVE/COPY) blocks **every** MCP call until closed.
