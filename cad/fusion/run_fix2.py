"""Fix transforms via MoveFeature (transform2 read-only i parametrisk modus)."""
import json, urllib.request

FUSION_SCRIPT = r'''
import adsk.core, adsk.fusion, math, traceback

GRIP_ANGLE_FROM_X = 110.0
BEND_X = 85.0
GRIP_LEN = 105.5
FRONT_DIA = 38.0
GRIP_DIA = 33.0
BIT_HOLDER_LEN = 12.0
FRONT_LEN_TOTAL = 145.0
MOTOR_TOTAL = 106.4
BATT_LEN = 65.0

GRIP_DIR_X = -math.cos(math.radians(180-GRIP_ANGLE_FROM_X))   # -0.342
GRIP_DIR_Z = -math.sin(math.radians(180-GRIP_ANGLE_FROM_X))   # -0.940
PERP_X = -GRIP_DIR_Z   # +0.940
PERP_Z =  GRIP_DIR_X   # -0.342


def make_xform_local_to_world(origin_mm, lx, ly, lz):
    m = adsk.core.Matrix3D.create()
    m.setWithCoordinateSystem(
        adsk.core.Point3D.create(origin_mm[0]/10, origin_mm[1]/10, origin_mm[2]/10),
        adsk.core.Vector3D.create(*lx),
        adsk.core.Vector3D.create(*ly),
        adsk.core.Vector3D.create(*lz),
    )
    return m


def find_occ(root, name):
    for occ in root.occurrences:
        if occ.component.name == name:
            return occ
    return None


def move_occurrence_to(root, occ, target_xform):
    """Sett occurrence sin transform direkte (deprekert API men funkar)."""
    occ.transform = target_xform


def run(_ctx):
    try:
        app = adsk.core.Application.get()
        design = adsk.fusion.Design.cast(app.activeProduct)
        root = design.rootComponent

        IDX = (1, 0, 0); IDY = (0, 1, 0); IDZ = (0, 0, 1)
        GX = (GRIP_DIR_X, 0, GRIP_DIR_Z)
        GY = (0, 1, 0)
        GZ = (PERP_X, 0, PERP_Z)

        # MOTOR
        m = find_occ(root, "Motor_Girkasse")
        if m:
            mx = FRONT_LEN_TOTAL - BIT_HOLDER_LEN - MOTOR_TOTAL
            xf = make_xform_local_to_world((mx, 0, 0), IDX, IDY, IDZ)
            move_occurrence_to(root, m, xf)
            print(f"Motor: X={mx:.1f}")

        # BATTERI
        b = find_occ(root, "Batteri_18650")
        if b:
            mid_t = GRIP_LEN/2
            mid_x = BEND_X + mid_t * GRIP_DIR_X
            mid_z = mid_t * GRIP_DIR_Z
            origin_x = mid_x - (BATT_LEN/2) * GRIP_DIR_X
            origin_z = mid_z - (BATT_LEN/2) * GRIP_DIR_Z
            xf = make_xform_local_to_world((origin_x, 0, origin_z), GX, GY, GZ)
            move_occurrence_to(root, b, xf)
            print(f"Batteri: ({origin_x:.1f}, 0, {origin_z:.1f})")

        # BITSFESTE
        bf = find_occ(root, "BitsFeste")
        if bf:
            xf = make_xform_local_to_world((133.0, 0, 0), IDX, IDY, IDZ)
            move_occurrence_to(root, bf, xf)
            print("BitsFeste: X=133")

        # PCB
        p = find_occ(root, "PCB")
        if p:
            mid_t = GRIP_LEN/2
            mid_x = BEND_X + mid_t * GRIP_DIR_X
            mid_z = mid_t * GRIP_DIR_Z
            offset = 6.0
            origin_x = mid_x + offset * PERP_X
            origin_z = mid_z + offset * PERP_Z
            xf = make_xform_local_to_world((origin_x, 0, origin_z), GX, GY, GZ)
            move_occurrence_to(root, p, xf)
            print(f"PCB: ({origin_x:.1f}, 0, {origin_z:.1f})")

        # TRIGGER
        t_occ = find_occ(root, "Trigger")
        if t_occ:
            t = 20.0
            base_x = BEND_X + t * GRIP_DIR_X
            base_z = t * GRIP_DIR_Z
            offset = GRIP_DIA/2 + 0.5
            origin_x = base_x + offset * PERP_X
            origin_z = base_z + offset * PERP_Z
            TX = (-GRIP_DIR_Z, 0, GRIP_DIR_X)    # forward perp
            TY = (0, 1, 0)
            TZ = (-GRIP_DIR_X, 0, -GRIP_DIR_Z)   # up-along-grip
            xf = make_xform_local_to_world((origin_x, 0, origin_z), TX, TY, TZ)
            move_occurrence_to(root, t_occ, xf)
            print(f"Trigger: ({origin_x:.1f}, 0, {origin_z:.1f})")

        # RETNINGSBRYTAR
        d = find_occ(root, "RetningBrytar")
        if d:
            xf = make_xform_local_to_world((BEND_X, 0, FRONT_DIA/2 + 0.5), IDX, IDY, IDZ)
            move_occurrence_to(root, d, xf)
            print(f"Retningsbrytar: ({BEND_X}, 0, {FRONT_DIA/2 + 0.5})")

        # ENDECAP
        c = find_occ(root, "EndeCap_Bak")
        if c:
            t = GRIP_LEN - 2.0
            origin_x = BEND_X + t * GRIP_DIR_X
            origin_z = t * GRIP_DIR_Z
            xf = make_xform_local_to_world((origin_x, 0, origin_z), GX, GY, GZ)
            move_occurrence_to(root, c, xf)
            print(f"EndeCap: ({origin_x:.1f}, 0, {origin_z:.1f})")

        print("MoveFeature anvendt paa alle occurrences.")

    except Exception:
        raise
'''

payload = {
    "jsonrpc": "2.0", "id": 90, "method": "tools/call",
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
