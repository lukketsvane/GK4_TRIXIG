"""Tildel material/utseende til komponentar."""
import json, urllib.request

FUSION_SCRIPT = r'''
import adsk.core, adsk.fusion, traceback

# (komponent-namn, app-bibliotek-namn, ein liste av kandidatnamn for utseende)
MATERIAL_MAP = [
    ("Skall_Utvendig",   ["Plastic - Matte (Black)", "ABS Black", "Plastic - ABS (Black)", "Plastic"]),
    ("Motor_Girkasse",   ["Steel - Satin", "Steel - Polished", "Steel"]),
    ("Batteri_18650",    ["Plastic - Glossy (Blue)", "Paint - Enamel Glossy (Blue)", "Paint Glossy (Blue)"]),
    ("BitsFeste",        ["Steel - Brushed", "Steel - Satin", "Steel - Polished"]),
    ("PCB",              ["Plastic - Glossy (Green)", "Paint - Enamel Glossy (Green)"]),
    ("Trigger",          ["Plastic - Matte (Light Gray)", "Plastic - Matte (White)", "Plastic - Matte (Gray)"]),
    ("RetningBrytar",    ["Plastic - Matte (Light Gray)", "Plastic - Matte (Gray)"]),
    ("EndeCap_Bak",      ["Plastic - Matte (Black)", "Plastic - ABS (Black)"]),
]


def find_appearance(app, name_candidates):
    """Søk etter eit utseende i ALLE bibliotek; prøv kvar kandidat uavhengig."""
    for lib in app.materialLibraries:
        for cand in name_candidates:
            try:
                ap = lib.appearances.itemByName(cand)
                if ap:
                    return ap, lib.name, cand
            except Exception:
                continue
    return None, None, None


def find_occ(root, name):
    for occ in root.occurrences:
        if occ.component.name == name:
            return occ
    return None


def run(_ctx):
    try:
        app = adsk.core.Application.get()
        design = adsk.fusion.Design.cast(app.activeProduct)
        root = design.rootComponent

        # Liste alle bibliotek for debug
        print("Tilgjengelege bibliotek:")
        for lib in app.materialLibraries:
            print(f"  {lib.name}")

        for comp_name, candidates in MATERIAL_MAP:
            occ = find_occ(root, comp_name)
            if not occ:
                print(f"  {comp_name}: IKKJE FUNNE")
                continue
            ap, lib_name, used_name = find_appearance(app, candidates)
            if not ap:
                # Fallback: forsoek å finne ALT som har "plastic" eller liknande
                print(f"  {comp_name}: ingen av {candidates} funnen")
                continue
            # Importer til design hvis ikkje allereie der
            try:
                ap_in_design = design.appearances.itemByName(ap.name)
                if not ap_in_design:
                    ap_in_design = design.appearances.addByCopy(ap, ap.name)
            except Exception:
                ap_in_design = ap
            # Tildel til alle bodies i komponenten
            for b in occ.component.bRepBodies:
                b.appearance = ap_in_design
            print(f"  {comp_name}: {used_name} ({lib_name})")

    except Exception:
        raise
'''

payload = {
    "jsonrpc": "2.0", "id": 70, "method": "tools/call",
    "params": {
        "name": "fusion_mcp_execute",
        "arguments": {"featureType": "script", "object": {"script": FUSION_SCRIPT}},
    }
}
req = urllib.request.Request("http://127.0.0.1:27182/mcp",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json", "Accept": "application/json, text/event-stream"},
    method="POST")
with urllib.request.urlopen(req, timeout=180) as resp:
    print(resp.read().decode("utf-8"))
