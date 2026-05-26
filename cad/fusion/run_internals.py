"""Add internal/external parts: bit holder, PCB, trigger, direction switch, rear cap."""
import json, urllib.request

FUSION_SCRIPT = r'''
import adsk.core, adsk.fusion, math, traceback

# Konstantar (stadfest grip-akse-retning)
GRIP_ANGLE_FROM_X = 110.0
BEND_X = 85.0
GRIP_LEN = 105.5
FRONT_DIA = 38.0
GRIP_DIA = 33.0
BIT_HOLDER_LEN = 12.0
FRONT_LEN_TOTAL = 145.0

GRIP_DIR_X = -math.sin(math.radians(180-GRIP_ANGLE_FROM_X))   # -0.342
GRIP_DIR_Z = -math.cos(math.radians(180-GRIP_ANGLE_FROM_X))   # -0.940
# Lokalt-til-verda rotasjon for grep-aksen: rot +110 grader om Y
GRIP_ROT_DEG = GRIP_ANGLE_FROM_X


def add_simple_component(root, name, part_no, desc):
    transform = adsk.core.Matrix3D.create()
    occ = root.occurrences.addNewComponent(transform)
    occ.component.name = name
    occ.component.partNumber = part_no
    occ.component.description = desc
    return occ


def make_grip_axis_transform(t_along_grip_mm, axis_offset_mm=(0, 0)):
    """Lag transform for ein del som skal liggje langs grep-aksen.
    t_along_grip_mm = posisjon langs grep-aksen frå BEND (0..GRIP_LEN)
    axis_offset_mm = (forward_along_grip_perp_x, lateral_y) i lokal grip-frame
    """
    # Basis-posisjon: BEND_X + t * (GRIP_DIR_X, 0, GRIP_DIR_Z)
    base_x = BEND_X + t_along_grip_mm * GRIP_DIR_X
    base_z = 0       + t_along_grip_mm * GRIP_DIR_Z
    # Lokal "forward" perpendikuler (i grep-frame), peikar mot framsida av grepet
    # Grep-frame: +X = grep-down-aksen, +Z = lokal "front" (perpendikuler i XZ-plan)
    # Front-perpendikuler i verda = (-GRIP_DIR_Z, 0, GRIP_DIR_X) = (0.940, 0, -0.342)
    px = -GRIP_DIR_Z * axis_offset_mm[0]   # 0.940 * a
    pz =  GRIP_DIR_X * axis_offset_mm[0]   # -0.342 * a
    origin_x = base_x + px
    origin_y = axis_offset_mm[1]
    origin_z = base_z + pz

    m = adsk.core.Matrix3D.create()
    m.setToRotation(
        math.radians(GRIP_ROT_DEG),
        adsk.core.Vector3D.create(0, 1, 0),
        adsk.core.Point3D.create(0, 0, 0),
    )
    tt = adsk.core.Matrix3D.create()
    tt.translation = adsk.core.Vector3D.create(origin_x/10, origin_y/10, origin_z/10)
    m.transformBy(tt)
    return m


def run(_ctx):
    try:
        app = adsk.core.Application.get()
        design = adsk.fusion.Design.cast(app.activeProduct)
        root = design.rootComponent

        # Slett eksisterande "ekstra" komponentar viss vi byggjer paa nytt
        for name in ["BitsFeste", "PCB", "Trigger", "RetningBrytar", "EndeCap_Bak", "Reim"]:
            for occ in list(root.occurrences):
                if occ.component.name == name:
                    occ.deleteMe()

        # ============== BITSFESTE ==============
        # 1/4" hex bit socket + magnet, plassert framfor motor-shaft (X=133..145)
        occ_bit = add_simple_component(root, "BitsFeste", "TRX-BIT-001",
            "1/4 inch hex bitsfeste med neodym-magnet")
        comp_bit = occ_bit.component

        # Ytre sylinder (boersta staal), Diameter11 x 12 mm, sentrert paa X-aksen
        sk = comp_bit.sketches.add(comp_bit.yZConstructionPlane)
        sk.isComputeDeferred = True
        sk.sketchCurves.sketchCircles.addByCenterRadius(
            adsk.core.Point3D.create(0, 0, 0), 11.0/2/10)
        sk.isComputeDeferred = False
        prof = sk.profiles.item(0)
        eIn = comp_bit.features.extrudeFeatures.createInput(prof,
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        eIn.setOneSideExtent(
            adsk.fusion.DistanceExtentDefinition.create(
                adsk.core.ValueInput.createByReal(BIT_HOLDER_LEN/10)),
            adsk.fusion.ExtentDirections.PositiveExtentDirection,
        )
        bit_outer = comp_bit.features.extrudeFeatures.add(eIn).bodies.item(0)
        bit_outer.name = "Bitsfeste_Krage"

        # Plasser bitsfeste foran motor: motor-shaft endar ved X = 26.6 + 106.4 = 133
        t = adsk.core.Matrix3D.create()
        t.translation = adsk.core.Vector3D.create(133.0/10, 0, 0)
        occ_bit.transform2 = t

        # ============== PCB ==============
        # Rektangulaer flate, ~85 x 16 x 1.6 mm, plassert i grepet langs aksen
        occ_pcb = add_simple_component(root, "PCB", "TRX-PCB-001",
            "Hovudkort med USB-C, mikrobrytar og status-LED")
        comp_pcb = occ_pcb.component

        PCB_LEN = 85.0
        PCB_W = 16.0
        PCB_T = 1.6

        sk2 = comp_pcb.sketches.add(comp_pcb.xYConstructionPlane)
        sk2.isComputeDeferred = True
        # Rektangel: lengd langs X (vert grep-akse etter rotasjon), breidd langs Y
        x0 = -PCB_LEN/2; x1 = PCB_LEN/2
        y0 = -PCB_W/2;  y1 = PCB_W/2
        ls = sk2.sketchCurves.sketchLines
        ls.addByTwoPoints(
            adsk.core.Point3D.create(x0/10, y0/10, 0),
            adsk.core.Point3D.create(x1/10, y0/10, 0))
        ls.addByTwoPoints(
            adsk.core.Point3D.create(x1/10, y0/10, 0),
            adsk.core.Point3D.create(x1/10, y1/10, 0))
        ls.addByTwoPoints(
            adsk.core.Point3D.create(x1/10, y1/10, 0),
            adsk.core.Point3D.create(x0/10, y1/10, 0))
        ls.addByTwoPoints(
            adsk.core.Point3D.create(x0/10, y1/10, 0),
            adsk.core.Point3D.create(x0/10, y0/10, 0))
        sk2.isComputeDeferred = False

        prof2 = sk2.profiles.item(0)
        eIn2 = comp_pcb.features.extrudeFeatures.createInput(prof2,
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        eIn2.setSymmetricExtent(
            adsk.core.ValueInput.createByReal(PCB_T/10),
            True,
        )
        pcb_body = comp_pcb.features.extrudeFeatures.add(eIn2).bodies.item(0)
        pcb_body.name = "PCB_Hovudkort"

        # PCB plasserast langs grep-aksen, paa fram-sida av grepet (mot triggeren)
        # Sentrum paa 50% inn i grepet, offset +6 mm forover (mot trigger-sida)
        occ_pcb.transform2 = make_grip_axis_transform(
            t_along_grip_mm=GRIP_LEN/2,
            axis_offset_mm=(6.0, 0.0)
        )

        # ============== TRIGGER ==============
        # Avtrekkar, oval pute paa fram-sida av grepet ved bend
        occ_trig = add_simple_component(root, "Trigger", "TRX-TRG-001",
            "Avtrekkar, POM graa, 12x7 mm visible")
        comp_trig = occ_trig.component

        # Lag ein liten sylinder (flatt knapp), Diameter12 visible x 4 mm djup
        sk3 = comp_trig.sketches.add(comp_trig.yZConstructionPlane)
        sk3.isComputeDeferred = True
        # Ellipse 12 x 7 (forenkla til oval-slott)
        # Bruk ellipse: senter, major-akse-pkt, minor-radius
        sk3.sketchCurves.sketchEllipses.add(
            adsk.core.Point3D.create(0, 0, 0),
            adsk.core.Point3D.create(0, 12.0/2/10, 0),         # major-akse-pkt (Y)
            adsk.core.Point3D.create(7.0/2/10, 0, 0),          # punkt paa ellipsen (minor-akse)
        )
        sk3.isComputeDeferred = False
        prof3 = sk3.profiles.item(0)
        eIn3 = comp_trig.features.extrudeFeatures.createInput(prof3,
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        eIn3.setOneSideExtent(
            adsk.fusion.DistanceExtentDefinition.create(
                adsk.core.ValueInput.createByReal(4.0/10)),
            adsk.fusion.ExtentDirections.PositiveExtentDirection,
        )
        trig_body = comp_trig.features.extrudeFeatures.add(eIn3).bodies.item(0)
        trig_body.name = "Trigger_Knapp"

        # Plasser trigger paa fram-sida av grepet, omtrent 18 mm ned frae bend
        # (på den fram-vendte sida der peikfingeren går)
        occ_trig.transform2 = make_grip_axis_transform(
            t_along_grip_mm=20.0,
            axis_offset_mm=(GRIP_DIA/2 + 1.0, 0.0)  # ut fra grepets fram-flate
        )

        # ============== RETNINGSBRYTAR ==============
        # Lite vippe-element paa toppen av frontkroppen, ved bend
        occ_dir = add_simple_component(root, "RetningBrytar", "TRX-DSW-001",
            "Retningsbrytar (forover/bakover), graa POM")
        comp_dir = occ_dir.component

        # Boks 16 x 8 x 4 mm
        sk4 = comp_dir.sketches.add(comp_dir.xYConstructionPlane)
        sk4.isComputeDeferred = True
        DSW_L = 16.0; DSW_W = 8.0; DSW_T = 4.0
        ls4 = sk4.sketchCurves.sketchLines
        x0,y0 = -DSW_L/2, -DSW_W/2
        x1,y1 =  DSW_L/2,  DSW_W/2
        ls4.addByTwoPoints(adsk.core.Point3D.create(x0/10,y0/10,0), adsk.core.Point3D.create(x1/10,y0/10,0))
        ls4.addByTwoPoints(adsk.core.Point3D.create(x1/10,y0/10,0), adsk.core.Point3D.create(x1/10,y1/10,0))
        ls4.addByTwoPoints(adsk.core.Point3D.create(x1/10,y1/10,0), adsk.core.Point3D.create(x0/10,y1/10,0))
        ls4.addByTwoPoints(adsk.core.Point3D.create(x0/10,y1/10,0), adsk.core.Point3D.create(x0/10,y0/10,0))
        sk4.isComputeDeferred = False
        prof4 = sk4.profiles.item(0)
        eIn4 = comp_dir.features.extrudeFeatures.createInput(prof4,
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        eIn4.setOneSideExtent(
            adsk.fusion.DistanceExtentDefinition.create(
                adsk.core.ValueInput.createByReal(DSW_T/10)),
            adsk.fusion.ExtentDirections.PositiveExtentDirection,
        )
        dir_body = comp_dir.features.extrudeFeatures.add(eIn4).bodies.item(0)
        dir_body.name = "RetningBrytar_Vippe"

        # Plasser retningsbrytaren oppaa frontkroppen ved bend (X=BEND_X), Z = +front_radius + 1
        t_dir = adsk.core.Matrix3D.create()
        t_dir.translation = adsk.core.Vector3D.create(
            BEND_X/10, 0, (FRONT_DIA/2 + 1.0)/10)
        occ_dir.transform2 = t_dir

        # ============== ENDECAP BAK ==============
        # Liten flat sylinder ved botn av grepet med lanyard-hol
        occ_cap = add_simple_component(root, "EndeCap_Bak", "TRX-CAP-001",
            "Bakre endecap med reim-feste")
        comp_cap = occ_cap.component

        sk5 = comp_cap.sketches.add(comp_cap.yZConstructionPlane)
        sk5.isComputeDeferred = True
        sk5.sketchCurves.sketchCircles.addByCenterRadius(
            adsk.core.Point3D.create(0, 0, 0), GRIP_DIA/2/10)
        sk5.isComputeDeferred = False
        prof5 = sk5.profiles.item(0)
        eIn5 = comp_cap.features.extrudeFeatures.createInput(prof5,
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        eIn5.setOneSideExtent(
            adsk.fusion.DistanceExtentDefinition.create(
                adsk.core.ValueInput.createByReal(4.0/10)),
            adsk.fusion.ExtentDirections.PositiveExtentDirection,
        )
        cap_body = comp_cap.features.extrudeFeatures.add(eIn5).bodies.item(0)
        cap_body.name = "EndeCap"

        # Plasser ved botnenden av grepet (t = GRIP_LEN)
        occ_cap.transform2 = make_grip_axis_transform(
            t_along_grip_mm=GRIP_LEN - 2.0,
            axis_offset_mm=(0.0, 0.0)
        )

        # ============== REPORT ==============
        print("Komponentar oppretta:")
        for occ in root.occurrences:
            comp = occ.component
            print(f"  {comp.name}  ({comp.partNumber})")
        print(f"Totalt: {root.occurrences.count} occurrences")

    except Exception:
        raise
'''

payload = {
    "jsonrpc": "2.0", "id": 50, "method": "tools/call",
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
