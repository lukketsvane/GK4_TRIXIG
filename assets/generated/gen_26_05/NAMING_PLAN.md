# gen_26_05 naming plan

Convention:

`<folder>/trixig_260526_<uid>_<short-slug>.png`

Rules:

- `trixig` keeps the project/product visible.
- `260526` is the generation date, 26 May 2026.
- `<uid>` is the stable inspected unique-image id from `u001` to `u239`.
- `<short-slug>` is lowercase ASCII, dense, and visually descriptive.
- Folders carry the broad category, so filenames stay short.
- Exact duplicates are deleted only when their SHA-256 hash is identical.
- `cleanup_manifest.csv` records every moved image and every deleted duplicate.
- `duplicate_manifest.csv` records the deleted duplicate and the retained file.
- `rename_manifest.csv` records the final path for every retained unique image.

Folders:

- `01_reference_renders` - baseline isolated TRIXIG renders.
- `02_mechanics_cutaways` - cutaways, exploded views, translucent internals, and motor/battery studies.
- `03_process_boards` - Tjalve/process/method boards and structure studies.
- `04_decision_boards` - selection, evaluation, comparison, and final-decision boards.
- `05_concept_presentations` - polished concept presentation sheets.
- `06_ideation_grids` - broad ideation grids, mixed catalogs, and exploratory generated boards.
- `07_variant_renders_light` - single variant renders on white/light backgrounds.
- `08_variant_renders_dark` - single variant renders on dark backgrounds.

