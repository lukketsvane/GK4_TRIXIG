# Repo cleanup summary

- deleted_exact_duplicate: 68
- ignored_large_100mb_plus: 3
- moved: 661

## Opprydding 2026-11-21

- deleted_exact_duplicate: 3 (brandmark_trixigplus_2.md og to .url-filer med `_2`)
- deleted_build_cache: 20 (grunnstruktur_web/.next; kjeldekoden vart fjerna i ee3ce67 og ligg i 8a05efe)
- deleted_autobackup: 5 (.blend1, .blend11, _prev1.plasticity, om lag 166 MB)
- moved: 11 (laust plasserte rotfiler til cad/ og assets/)
- Behaldt med vilje: `cad/fusion/pcb_battery_asset/trixig_pcb_battery_simplified_print_mm.stl` og
  `cad/print/trixig_redesign/for_bambu/pcb_battery_simplified_print_mm.stl` er like, fordi
  `cad/fusion/trixig_pcb_battery_print_stl.py` skriv same fil til begge mappene.
