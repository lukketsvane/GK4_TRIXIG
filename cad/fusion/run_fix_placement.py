"""Korriger plassering av alle komponentar med setWithCoordinateSystem."""
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

# Grep-akse: 110 grader interior fra +X, peikar ned-og-litt-bak
# = (cos(250 grader), sin(250 grader)) = (-0.342, -0.940)
GRIP_DIR_X = -math.cos(math.radians(180-GRIP_ANGLE_FROM_X))   # -cos(70) = -0.342
GRIP_DIR_Z = -math.sin(math.radians(180-GRIP_ANGLE_FROM_X))   # -sin(70) = -0.940
# Forward perpendikuler i XZ-planet (mot triggeren-sida)
PERP_X = -GRIP_DIR_Z   # +0.940
PERP_Z =  GRIP_DIR_X   # -0.342


def xform(origin_mm, lx, ly, lz):
    """Lokal-til-verda transform."""
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


def run(_ctx):
    try:
        app = adsk.core.Application.get()
        design = adsk.fusion.Design.cast(app.activeProduct)
        root = design.rootComponent

        # Identitets-aksar
        IDX = (1, 0, 0); IDY = (0, 1, 0); IDZ = (0, 0, 1)
        # Grep-aksar (lokal +X langs grep-down)
        GX = (GRIP_DIR_X, 0, GRIP_DIR_Z)
        GY = (0, 1, 0)
        GZ = (PERP_X, 0, PERP_Z)   # lokal +Z mot triggeren

        # ===== MOTOR =====
        # Motor lokal +X = verda +X. Origin = (FRONT_LEN_TOTAL - BIT_HOLDER_LEN - MOTOR_TOTAL, 0, 0)
        motor = find_occ(root, "Motor_Girkasse")
        if motor:
            mx = FRONT_LEN_TOTAL - BIT_HOLDER_LEN - MOTOR_TOTAL  # 26.6
            motor.transform2 = xform((mx, 0, 0), IDX, IDY, IDZ)
            print(f"Motor at X={mx}")

        # ===== BATTERI =====
        # Lokal +X langs grep-down. Origin slik at batteri-midten ligg paa GRIP_LEN/2.
        batt = find_occ(root, "Batteri_18650")
        if batt:
            mid_t = GRIP_LEN/2
            mid_x = BEND_X + mid_t * GRIP_DIR_X
            mid_z = mid_t * GRIP_DIR_Z
            # Origin = midten - (BATT_LEN/2) langs lokal +X = midten - (BATT_LEN/2) * GRIP_DIR
            origin_x = mid_x - (BATT_LEN/2) * GRIP_DIR_X
            origin_z = mid_z - (BATT_LEN/2) * GRIP_DIR_Z
            batt.transform2 = xform((origin_x, 0, origin_z), GX, GY, GZ)
            print(f"Batteri origin=({origin_x:.1f}, 0, {origin_z:.1f})")

        # ===== BITSFESTE =====
        # Lokal +X = verda +X. Origin foran motor-shaft.
        bit = find_occ(root, "BitsFeste")
        if bit:
            origin_x = MOTOR_TOTAL + (FRONT_LEN_TOTAL - BIT_HOLDER_LEN - MOTOR_TOTAL) - BIT_HOLDER_LEN/2 + BIT_HOLDER_LEN/2  # = 133
            # Faktisk: motor-shaft endar ved X = 26.6 + 106.4 = 133. Bitsfeste byrjar her.
            bit.transform2 = xform((133.0, 0, 0), IDX, IDY, IDZ)
            print(f"Bitsfeste at X=133")

        # ===== PCB =====
        # Lokal +X langs grep-down (lengd 85). Origin = midten av grep + 6 mm forward perp.
        pcb = find_occ(root, "PCB")
        if pcb:
            mid_t = GRIP_LEN/2
            mid_x = BEND_X + mid_t * GRIP_DIR_X
            mid_z = mid_t * GRIP_DIR_Z
            # PCB sentrert paa lokal X=0 (sketch frå -42.5 til +42.5)
            # Sa origin = midten + offset
            offset = 6.0  # mm fram-perp (mot trigger)
            origin_x = mid_x + offset * PERP_X
            origin_z = mid_z + offset * PERP_Z
            pcb.transform2 = xform((origin_x, 0, origin_z), GX, GY, GZ)
            print(f"PCB origin=({origin_x:.1f}, 0, {origin_z:.1f})")

        # ===== TRIGGER =====
        # Trigger er ein flat ellipse-knapp, ekstrudert i lokal +X.
        # Vi vil at:
        #   lokal +X = forward-perp (knappen stikk ut mot brukaren)
        #   lokal +Y = lateral (12 mm major-akse Y)
        #   lokal +Z = grep-down (7 mm minor-akse Z)
        # Origin = ved fram-flata av grepet, t=20 mm ned frae bend.
        trig = find_occ(root, "Trigger")
        if trig:
            t = 20.0
            base_x = BEND_X + t * GRIP_DIR_X
            base_z = t * GRIP_DIR_Z
            offset = GRIP_DIA/2 + 0.5  # ut frå grep-overflata
            origin_x = base_x + offset * PERP_X
            origin_z = base_z + offset * PERP_Z
            # Lokal +Z langs grep-down
            TZ = (GRIP_DIR_X, 0, GRIP_DIR_Z)
            # Lokal +Y = (0,1,0)
            TY = (0, 1, 0)
            # Lokal +X = TY x TZ
            # (0,1,0) x (gx,0,gz) = (1*gz - 0*0, 0*gx - 0*gz, 0*0 - 1*gx) = (gz, 0, -gx)
            TX = (GRIP_DIR_Z, 0, -GRIP_DIR_X)   # = (-0.940, 0, 0.342) — peikar bakover-perp
            # Det er feil retning — vi vil at +X peikar UT (mot trigger-sida)
            # Snu TX:
            TX = (-GRIP_DIR_Z, 0, GRIP_DIR_X)   # = (0.940, 0, -0.342) — forward perp
            # Sjekk: TX cross TY = TZ ?
            # (0.940,0,-0.342) x (0,1,0) = (0*0 - (-0.342)*1, -0.342*0 - 0.940*0, 0.940*1 - 0*0)
            #                            = (0.342, 0, 0.940)
            # Vi vil ha TZ = (gx, 0, gz) = (-0.342, 0, -0.940). Det er motsatt.
            # Sa flip TZ:
            TZ = (-GRIP_DIR_X, 0, -GRIP_DIR_Z)  # = (0.342, 0, 0.940) — peikar OPP-perp-langs-grep
            trig.transform2 = xform((origin_x, 0, origin_z), TX, TY, TZ)
            print(f"Trigger origin=({origin_x:.1f}, 0, {origin_z:.1f})")

        # ===== RETNINGSBRYTAR =====
        # Boks 16x8x4. Verdsaksar. Origin paa toppen av frontkroppen ved BEND_X.
        dsw = find_occ(root, "RetningBrytar")
        if dsw:
            dsw.transform2 = xform((BEND_X, 0, FRONT_DIA/2 + 0.5), IDX, IDY, IDZ)
            print(f"Retningsbrytar at ({BEND_X}, 0, {FRONT_DIA/2 + 0.5})")

        # ===== ENDECAP =====
        # Sylinder GRIP_DIA x 4 langs grep-aksen. Origin = botn av grep.
        cap = find_occ(root, "EndeCap_Bak")
        if cap:
            t = GRIP_LEN - 2.0
            origin_x = BEND_X + t * GRIP_DIR_X
            origin_z = t * GRIP_DIR_Z
            cap.transform2 = xform((origin_x, 0, origin_z), GX, GY, GZ)
            print(f"EndeCap origin=({origin_x:.1f}, 0, {origin_z:.1f})")

        print("Plasseringar oppdatert.")

    except Exception:
        raise
'''

payload = {
    "jsonrpc": "2.0", "id": 60, "method": "tools/call",
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
