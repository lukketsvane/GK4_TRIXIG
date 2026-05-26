"""Helper: send a Fusion script to MCP and print result."""
import json, urllib.request

FUSION_SCRIPT = r'''
import adsk.core, adsk.fusion, math, traceback

def revolve_profile(comp, sketch, axis, op=None):
    if op is None:
        op = adsk.fusion.FeatureOperations.NewBodyFeatureOperation
    prof = sketch.profiles.item(0)
    rIn = comp.features.revolveFeatures.createInput(prof, axis, op)
    rIn.setAngleExtent(False, adsk.core.ValueInput.createByReal(2*math.pi))
    return comp.features.revolveFeatures.add(rIn)

def extrude_profile(comp, sketch, distance_mm, direction="positive", op=None):
    if op is None:
        op = adsk.fusion.FeatureOperations.NewBodyFeatureOperation
    prof = sketch.profiles.item(0)
    eIn = comp.features.extrudeFeatures.createInput(prof, op)
    if direction == "positive":
        d = adsk.fusion.ExtentDirections.PositiveExtentDirection
    elif direction == "negative":
        d = adsk.fusion.ExtentDirections.NegativeExtentDirection
    else:
        d = adsk.fusion.ExtentDirections.SymmetricExtentDirection
    eIn.setOneSideExtent(
        adsk.fusion.DistanceExtentDefinition.create(
            adsk.core.ValueInput.createByReal(distance_mm/10)),
        d,
    )
    return comp.features.extrudeFeatures.add(eIn)

def move_body(comp, body, transform_matrix):
    objs = adsk.core.ObjectCollection.create()
    objs.add(body)
    mIn = comp.features.moveFeatures.createInput(objs, transform_matrix)
    return comp.features.moveFeatures.add(mIn)


def run(_ctx):
    try:
        app = adsk.core.Application.get()
        design = adsk.fusion.Design.cast(app.activeProduct)
        root = design.rootComponent

        # === 1. SLETT GAMMALT SKALL ===
        for occ in list(root.occurrences):
            if occ.component.name == "Skall_Utvendig":
                occ.deleteMe()

        # === 2. PARAMETRAR (mm) ===
        FRONT_LEN_TOTAL = 145.0
        FRONT_DIA = 38.0
        NOSE_DIA = 22.0
        NOSE_LEN = 13.0
        FRONT_BODY_LEN = FRONT_LEN_TOTAL - NOSE_LEN

        BEND_X = 85.0
        GRIP_LEN = 105.5
        GRIP_DIA = 33.0
        GRIP_ANGLE_FROM_X = 110.0
        GRIP_OVERLAP = 8.0

        MOTOR_TOTAL = 106.4
        BIT_HOLDER_LEN = 12.0
        MOTOR_X_START = FRONT_LEN_TOTAL - BIT_HOLDER_LEN - MOTOR_TOTAL  # 26.6

        BATT_LEN = 65.0

        # === 3. BYGG NYTT SKALL ===
        transform = adsk.core.Matrix3D.create()
        occ_skall = root.occurrences.addNewComponent(transform)
        occ_skall.component.name = "Skall_Utvendig"
        occ_skall.component.partNumber = "TRX-SHL-001"
        occ_skall.component.description = "Yttre skall, ABS, 2.0-2.5 mm vegg"
        comp = occ_skall.component

        # 3a. Front: revolve
        sk_f = comp.sketches.add(comp.xYConstructionPlane)
        sk_f.isComputeDeferred = True
        x0, x1, x2 = 0.0, FRONT_BODY_LEN, FRONT_LEN_TOTAL
        pts = [
            (x0, 0),
            (x0, FRONT_DIA/2),
            (x1, FRONT_DIA/2),
            (x2, NOSE_DIA/2),
            (x2, 0),
        ]
        lines = sk_f.sketchCurves.sketchLines
        for i in range(len(pts)):
            a = pts[i]; b = pts[(i+1) % len(pts)]
            lines.addByTwoPoints(
                adsk.core.Point3D.create(a[0]/10, a[1]/10, 0),
                adsk.core.Point3D.create(b[0]/10, b[1]/10, 0),
            )
        sk_f.isComputeDeferred = False
        front_body = revolve_profile(comp, sk_f, comp.xConstructionAxis).bodies.item(0)
        front_body.name = "Skall_Front"

        # 3b. Grep
        sk_g = comp.sketches.add(comp.yZConstructionPlane)
        sk_g.isComputeDeferred = True
        sk_g.sketchCurves.sketchCircles.addByCenterRadius(
            adsk.core.Point3D.create(0, 0, 0), GRIP_DIA/2/10)
        sk_g.isComputeDeferred = False
        grip_body = extrude_profile(
            comp, sk_g, GRIP_LEN + GRIP_OVERLAP, direction="negative").bodies.item(0)
        grip_body.name = "Skall_Grep"

        # Roter -70 grader om Y for aa peike grep ned-bak
        rot = adsk.core.Matrix3D.create()
        rot.setToRotation(
            math.radians(-(180 - GRIP_ANGLE_FROM_X)),
            adsk.core.Vector3D.create(0, 1, 0),
            adsk.core.Point3D.create(0, 0, 0)
        )
        move_body(comp, grip_body, rot)

        trans = adsk.core.Matrix3D.create()
        trans.translation = adsk.core.Vector3D.create(BEND_X/10, 0, 0)
        move_body(comp, grip_body, trans)

        # 3c. Boolean union
        tools = adsk.core.ObjectCollection.create()
        tools.add(grip_body)
        cIn = comp.features.combineFeatures.createInput(front_body, tools)
        cIn.operation = adsk.fusion.FeatureOperations.JoinFeatureOperation
        comp.features.combineFeatures.add(cIn)
        front_body.name = "Skall_Solid"

        # 3d. Fillet
        edges = adsk.core.ObjectCollection.create()
        for e in front_body.edges:
            edges.add(e)
        if edges.count > 0:
            try:
                fIn = comp.features.filletFeatures.createInput()
                fIn.addConstantRadiusEdgeSet(
                    edges, adsk.core.ValueInput.createByReal(3.0/10), True)
                comp.features.filletFeatures.add(fIn)
            except Exception as fe:
                print("Fillet aatvarsel:", str(fe))

        # === 4. PLASSER MOTOR ===
        for occ in root.occurrences:
            if occ.component.name == "Motor_Girkasse":
                t = adsk.core.Matrix3D.create()
                t.translation = adsk.core.Vector3D.create(MOTOR_X_START/10, 0, 0)
                occ.transform2 = t
                print(f"Motor flyttet til X={MOTOR_X_START}")
                break

        # === 5. PLASSER BATTERI ===
        for occ in root.occurrences:
            if occ.component.name == "Batteri_18650":
                grip_dir_x = -math.sin(math.radians(180-GRIP_ANGLE_FROM_X))
                grip_dir_z = -math.cos(math.radians(180-GRIP_ANGLE_FROM_X))
                center_t = 0.50 * GRIP_LEN
                center_x = BEND_X + center_t * grip_dir_x
                center_z = 0 + center_t * grip_dir_z
                rot_deg = GRIP_ANGLE_FROM_X
                origin_x = center_x - (BATT_LEN/2) * grip_dir_x
                origin_z = center_z - (BATT_LEN/2) * grip_dir_z

                m = adsk.core.Matrix3D.create()
                m.setToRotation(
                    math.radians(rot_deg),
                    adsk.core.Vector3D.create(0, 1, 0),
                    adsk.core.Point3D.create(0, 0, 0)
                )
                tt = adsk.core.Matrix3D.create()
                tt.translation = adsk.core.Vector3D.create(origin_x/10, 0, origin_z/10)
                m.transformBy(tt)
                occ.transform2 = m
                print(f"Batteri plassert: origin=({origin_x:.1f},0,{origin_z:.1f})")
                break

        # === 6. RAPPORT ===
        print("=" * 40)
        for b in comp.bRepBodies:
            bb = b.boundingBox
            mx, mn = bb.maxPoint, bb.minPoint
            print(f"Skall {b.name}: {(mx.x-mn.x)*10:.1f} x {(mx.y-mn.y)*10:.1f} x {(mx.z-mn.z)*10:.1f} mm")
            print(f"  X: {mn.x*10:.1f} -> {mx.x*10:.1f}")
            print(f"  Z: {mn.z*10:.1f} -> {mx.z*10:.1f}")

    except Exception:
        raise
'''

payload = {
    "jsonrpc": "2.0", "id": 40, "method": "tools/call",
    "params": {
        "name": "fusion_mcp_execute",
        "arguments": {"featureType": "script", "object": {"script": FUSION_SCRIPT}},
    }
}
req = urllib.request.Request(
    "http://127.0.0.1:27182/mcp",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json", "Accept": "application/json, text/event-stream"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=180) as resp:
    print(resp.read().decode("utf-8"))
