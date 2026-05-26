"""Skjul skall, render interne komponentar for å sjå plassering."""
import json, urllib.request, base64, sys
from pathlib import Path

def call(method, args):
    p = {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
         "params": {"name": method, "arguments": args}}
    req = urllib.request.Request("http://127.0.0.1:27182/mcp",
        data=json.dumps(p).encode("utf-8"),
        headers={"Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream"},
        method="POST")
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))

# Hide skall
hide_script = '''
import adsk.core, adsk.fusion
def run(_ctx):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    root = design.rootComponent
    for occ in root.occurrences:
        if occ.component.name == "Skall_Utvendig":
            occ.isLightBulbOn = False
        else:
            occ.isLightBulbOn = True
    app.activeViewport.fit()
'''
res = call("fusion_mcp_execute", {"featureType": "script", "object": {"script": hide_script}})
print("Hide:", res["result"]["content"][0]["text"][:200])

views = sys.argv[1:] if len(sys.argv) > 1 else ["front", "iso-top-right"]
for v in views:
    res = call("fusion_mcp_read", {"queryType": "screenshot",
        "direction": v, "width": 1500, "height": 1000, "transparentBackground": False})
    content = res["result"]["content"][0]
    if content.get("type") == "image":
        out = str(Path(__file__).resolve().parent / f"internal_{v}.png")
        with open(out, "wb") as f:
            f.write(base64.b64decode(content["data"]))
        print(f"Saved: {out}")
