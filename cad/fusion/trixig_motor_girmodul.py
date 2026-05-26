"""
DC GEAR MOTOR (TRIXIG) - Fusion 360 modeling script
====================================================

Bygger TRIXIG-girmotoren som ein parametrisk rotasjonslekam i Fusion 360.
Basert paa "DC GEAR MOTOR ASSEMBLY - REFERENCE DRAWING FOR 3D MODELING"
(referansebilder/, mai 2026).

KOEYRING I FUSION 360:
  1. Open Fusion 360.
  2. Utilities (eller Tools)  ->  Scripts and Add-Ins.
  3. "Scripts"-fana  ->  My Scripts  ->  trykk "+" (Add existing).
  4. Naviger til denne fila og vel ho.
  5. Vel scriptet i lista og trykk "Run".

Tilpass parametrane nedanfor og koeyr scriptet paa nytt for aa justere
modellen. Modellen blir bygd i origo, med rotasjonsaksen langs X (motor-
bakkant ved X=0, aksel-tipp ved X=106.4).

SPESIFIKASJON FRAA REFERANSEN:
  Motorhus:     stal,             Diameter32.0 mm, lengd 47.0 mm
  Girkasse:     plast (POM/PA),   Diameter35.0 mm, lengd 35.4 mm
  Frontboss:    plast,            Diameter18.0 mm (synleg paa front view)
  Aksel:        stal, ikkje notet, Diameter10.0 mm, fri lengd 24.0 mm
  Total lengd:  106.4 mm
  Spenning:     12 V DC
  RPM (no load): ~120
  Gearing:      ~150:1
  Vekt:         ~110 g
  Konnektor:    XH2.54-2P, raud (+) / svart (-) leiing aa 100 mm

Detaljar som IKKJE er med i denne fyrste versjonen, men kan leggjast til:
  - Ovalt ventilasjons-spalte paa motor-sida
  - 2 koparpinnar (terminalar) paa motor-bakflata
  - M3-gjengeinnlegg paa girkasse-front (panel 7 i referansen)
  - XH2.54-2P-konnektor og leiingar
  - Skilje motor / girkasse i to body-ar for ulike materialer
"""

import adsk.core
import adsk.fusion
import math
import traceback


# -----------------------------------------------------------------------------
# Parametrar (mm). Endre her - alt skalerer automatisk.
# -----------------------------------------------------------------------------

# Motor (boerstemotor, stalhus)
MOTOR_DIA = 32.0
MOTOR_LEN = 47.0

# Girkasse (plasthus). GEARBOX_TOTAL_LEN = girkasse-kropp + frontboss.
GEARBOX_DIA = 35.0
GEARBOX_TOTAL_LEN = 35.4
FRONT_BOSS_DIA = 18.0
FRONT_BOSS_LEN = 3.0  # estimat - ikkje eksplisitt malt, men synleg paa side view
GEARBOX_BODY_LEN = GEARBOX_TOTAL_LEN - FRONT_BOSS_LEN  # 32.4 mm

# Utgaaande aksel (rund, ikkje notet, press-fit)
SHAFT_DIA = 10.0
SHAFT_LEN = 24.0


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        # Lag eit nytt design (visningseining styrer brukar i UI - geometri i cm)
        app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = adsk.fusion.Design.cast(app.activeProduct)

        root = design.rootComponent
        # Root component name kan ikkje endrast i Fusion - dropp omdoeyping

        # Bygg halvprofilen i mm. Profilen ligg i XY-planet, langs X-aksen,
        # og er lukka mot Y = 0 (rotasjonsaksen).
        x = 0.0
        pts = [(x, 0.0), (x, MOTOR_DIA / 2)]

        x += MOTOR_LEN
        pts += [(x, MOTOR_DIA / 2), (x, GEARBOX_DIA / 2)]

        x += GEARBOX_BODY_LEN
        pts += [(x, GEARBOX_DIA / 2), (x, FRONT_BOSS_DIA / 2)]

        x += FRONT_BOSS_LEN
        pts += [(x, FRONT_BOSS_DIA / 2), (x, SHAFT_DIA / 2)]

        x += SHAFT_LEN
        pts += [(x, SHAFT_DIA / 2), (x, 0.0)]

        total_len = x

        # Skissér profilen som lukka polygon
        sketch = root.sketches.add(root.xYConstructionPlane)
        sketch.name = "Halvprofil"
        sketch.isComputeDeferred = True
        lines = sketch.sketchCurves.sketchLines
        for i in range(len(pts)):
            a = pts[i]
            b = pts[(i + 1) % len(pts)]
            # Fusion API jobbar i cm internt
            p1 = adsk.core.Point3D.create(a[0] / 10.0, a[1] / 10.0, 0)
            p2 = adsk.core.Point3D.create(b[0] / 10.0, b[1] / 10.0, 0)
            lines.addByTwoPoints(p1, p2)
        sketch.isComputeDeferred = False

        # Roter profilen 360 grader rundt X-aksen
        prof = sketch.profiles.item(0)
        rev_input = root.features.revolveFeatures.createInput(
            prof,
            root.xConstructionAxis,
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation,
        )
        rev_input.setAngleExtent(
            False, adsk.core.ValueInput.createByReal(2 * math.pi)
        )
        rev = root.features.revolveFeatures.add(rev_input)
        rev.bodies.item(0).name = "MotorGirkasse"

        print(
            "DC-girmotor bygd som rotasjonslekam. "
            "Total mekanisk lengd: {:.2f} mm. "
            "Stoerste diameter: {:.2f} mm.".format(total_len, GEARBOX_DIA)
        )

    except Exception:
        # Re-raise so MCP-klienten ser feilen i staden for ein modal dialog
        raise
