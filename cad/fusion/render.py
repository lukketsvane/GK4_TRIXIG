"""Show all components, fit view, render iso + side."""
import json, urllib.request, base64, sys
from pathlib import Path

def call(method, args):
    payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
               "params": {"name": method, "arguments": args}}
    req = urllib.request.Request("http://127.0.0.1:27182/mcp",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream"},
        method="POST")
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))

# Show all
show_script = """
import adsk.core, adsk.fusion
def run(_ctx):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    root = design.rootComponent
    for occ in root.occurrences:
        occ.isLightBulbOn = True
    app.activeViewport.fit()
"""
res = call("fusion_mcp_execute", {"featureType": "script", "object": {"script": show_script}})
print("Show all:", res["result"]["content"][0]["text"][:200])

views = sys.argv[1:] if len(sys.argv) > 1 else ["right", "iso-top-right"]
for v in views:
    res = call("fusion_mcp_read", {"queryType": "screenshot",
        "direction": v, "width": 1500, "height": 1000, "transparentBackground": False})
    content = res["result"]["content"][0]
    if content.get("type") == "image":
        out = str(Path(__file__).resolve().parent / f"trixig_{v}.png")
        with open(out, "wb") as f:
            f.write(base64.b64decode(content["data"]))
        print(f"Saved: {out}")
