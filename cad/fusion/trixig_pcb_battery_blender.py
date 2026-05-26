"""
Build a millimeter-scale TRIXIG PCB + 18650 battery asset for Blender.

Hard dimensions are taken from the caliper reference photos:
  - PCB length: 95.39 mm
  - PCB max width: 26.31 mm
  - PCB thickness: 1.60 mm, typical FR4
  - Battery length: 65.02 mm
  - Battery diameter: 18.60 mm, 18650-class cell envelope

Run:
  "C:/Program Files/Blender Foundation/Blender 5.1/blender.exe" --background --python trixig_pcb_battery_blender.py

Outputs are written next to this script in:
  pcb_battery_asset/trixig_pcb_battery_scaled.blend
  pcb_battery_asset/trixig_pcb_battery_scaled.glb
  pcb_battery_asset/trixig_pcb_battery_scaled.obj

The authored dimensions are in millimeters, but Blender/GLTF geometry is stored
internally in meters so imports into normal Blender scenes come in at 1:1 scale.
"""

from __future__ import annotations

import math
from pathlib import Path

import bpy
from mathutils import Vector


SCRIPT_DIR = Path(__file__).resolve().parent
OUT_DIR = SCRIPT_DIR / "pcb_battery_asset"
OUT_DIR.mkdir(exist_ok=True)

BLEND_PATH = OUT_DIR / "trixig_pcb_battery_scaled.blend"
GLB_PATH = OUT_DIR / "trixig_pcb_battery_scaled.glb"
OBJ_PATH = OUT_DIR / "trixig_pcb_battery_scaled.obj"
PNG_PATH = OUT_DIR / "trixig_pcb_battery_preview.png"
ASSET_COLLECTION_NAME = "TRIXIG_PCB_BATTERY_SCALED_MM"
PREVIEW_COLLECTION_NAME = "preview_not_for_append"


# Millimeter dimensions.
PCB_LENGTH = 95.39
PCB_WIDTH = 26.31
PCB_THICKNESS = 1.60

CELL_LENGTH = 65.02
CELL_DIAMETER = 18.60
CELL_RADIUS = CELL_DIAMETER / 2.0

CELL_X0 = (PCB_LENGTH - CELL_LENGTH) / 2.0
CELL_X1 = CELL_X0 + CELL_LENGTH
CELL_CX = (CELL_X0 + CELL_X1) / 2.0
CELL_CY = 0.0
CELL_CZ = PCB_THICKNESS + CELL_RADIUS + 0.35
MM_TO_M = 0.001


def m(value_mm: float) -> float:
    return value_mm * MM_TO_M


def v3_mm(values: tuple[float, float, float]) -> tuple[float, float, float]:
    return (m(values[0]), m(values[1]), m(values[2]))


def dims_mm(values: tuple[float, float, float]) -> tuple[float, float, float]:
    return (m(values[0]), m(values[1]), m(values[2]))


def reset_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    bpy.context.scene.unit_settings.system = "METRIC"
    bpy.context.scene.unit_settings.scale_length = 1.0
    bpy.context.scene.unit_settings.length_unit = "MILLIMETERS"


def make_mat(
    name: str,
    color: tuple[float, float, float, float],
    metallic: float = 0.0,
    roughness: float = 0.55,
) -> bpy.types.Material:
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        if "Base Color" in bsdf.inputs:
            bsdf.inputs["Base Color"].default_value = color
        if "Metallic" in bsdf.inputs:
            bsdf.inputs["Metallic"].default_value = metallic
        if "Roughness" in bsdf.inputs:
            bsdf.inputs["Roughness"].default_value = roughness
    return mat


def add_weighted_normals(obj: bpy.types.Object) -> None:
    mod = obj.modifiers.new("weighted_normals", "WEIGHTED_NORMAL")
    mod.keep_sharp = True


def add_bevel(obj: bpy.types.Object, width: float, segments: int = 2) -> None:
    bevel = obj.modifiers.new("small_edge_bevel", "BEVEL")
    bevel.width = m(width)
    bevel.segments = segments
    bevel.affect = "EDGES"
    add_weighted_normals(obj)


def assign_mat(obj: bpy.types.Object, mat: bpy.types.Material) -> bpy.types.Object:
    obj.data.materials.append(mat)
    return obj


def move_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for existing in list(obj.users_collection):
        existing.objects.unlink(obj)
    collection.objects.link(obj)


def box(
    name: str,
    loc: tuple[float, float, float],
    dims: tuple[float, float, float],
    mat: bpy.types.Material,
    bevel: float = 0.0,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=v3_mm(loc))
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_mesh"
    obj.dimensions = dims_mm(dims)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    assign_mat(obj, mat)
    if bevel > 0:
        add_bevel(obj, bevel)
    return obj


def cyl(
    name: str,
    loc: tuple[float, float, float],
    radius: float,
    depth: float,
    mat: bpy.types.Material,
    vertices: int = 96,
    rotation: tuple[float, float, float] = (0.0, 0.0, 0.0),
    bevel: bool = False,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=m(radius),
        depth=m(depth),
        location=v3_mm(loc),
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_mesh"
    assign_mat(obj, mat)
    bpy.ops.object.shade_smooth()
    if bevel:
        add_bevel(obj, 0.08, 2)
    return obj


def make_pcb_outline(mat: bpy.types.Material) -> bpy.types.Object:
    half_w = PCB_WIDTH / 2.0
    # Clockwise outline, simplified from the top-down PCB photo.
    # The hard extents are exact: X = 0..95.39, Y = +/-13.155.
    pts = [
        (0.00, -5.25),
        (0.00, 5.25),
        (3.20, 5.25),
        (3.20, 9.20),
        (8.20, 9.20),
        (11.10, 12.15),
        (31.50, 12.65),
        (58.00, half_w),
        (75.00, half_w),
        (78.50, 12.10),
        (89.25, 12.10),
        (95.39, 8.60),
        (95.39, -8.60),
        (89.25, -12.10),
        (78.50, -12.10),
        (75.00, -half_w),
        (58.00, -half_w),
        (31.50, -12.65),
        (11.10, -12.15),
        (8.20, -9.20),
        (3.20, -9.20),
        (3.20, -5.25),
    ]

    verts = [(m(x), m(y), 0.0) for x, y in pts] + [
        (m(x), m(y), m(PCB_THICKNESS)) for x, y in pts
    ]
    n = len(pts)
    faces = [tuple(range(n - 1, -1, -1)), tuple(range(n, 2 * n))]
    for i in range(n):
        faces.append((i, (i + 1) % n, (i + 1) % n + n, i + n))

    mesh = bpy.data.meshes.new("pcb_outline_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(f"PCB_{PCB_LENGTH:.2f}x{PCB_WIDTH:.2f}x{PCB_THICKNESS:.2f}mm", mesh)
    bpy.context.collection.objects.link(obj)
    assign_mat(obj, mat)
    add_bevel(obj, 0.18, 3)
    return obj


def disk_on_pcb(
    name: str,
    x: float,
    y: float,
    r: float,
    mat: bpy.types.Material,
    z_offset: float = 0.045,
    height: float = 0.09,
) -> bpy.types.Object:
    return cyl(
        name,
        (x, y, PCB_THICKNESS + z_offset),
        r,
        height,
        mat,
        vertices=48,
        bevel=True,
    )


def make_poly_curve(
    name: str,
    points: list[tuple[float, float, float]],
    radius: float,
    mat: bpy.types.Material,
) -> bpy.types.Object:
    curve = bpy.data.curves.new(name, "CURVE")
    curve.dimensions = "3D"
    curve.resolution_u = 8
    curve.bevel_depth = m(radius)
    curve.bevel_resolution = 5
    spl = curve.splines.new("POLY")
    spl.points.add(len(points) - 1)
    for pnt, co in zip(spl.points, points):
        pnt.co = (m(co[0]), m(co[1]), m(co[2]), 1.0)
    obj = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(mat)
    return obj


def add_text(
    name: str,
    text: str,
    loc: tuple[float, float, float],
    size: float,
    mat: bpy.types.Material,
    rot: tuple[float, float, float] = (0.0, 0.0, 0.0),
) -> bpy.types.Object:
    bpy.ops.object.text_add(location=v3_mm(loc), rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_font"
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = m(size)
    obj.data.extrude = m(0.02)
    obj.data.materials.append(mat)
    return obj


def look_at(obj: bpy.types.Object, target: tuple[float, float, float]) -> None:
    direction = Vector(v3_mm(target)) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def build_asset() -> list[bpy.types.Object]:
    reset_scene()
    asset_collection = bpy.data.collections.new(ASSET_COLLECTION_NAME)
    preview_collection = bpy.data.collections.new(PREVIEW_COLLECTION_NAME)
    bpy.context.scene.collection.children.link(asset_collection)
    bpy.context.scene.collection.children.link(preview_collection)

    # Materials.
    mat_pcb = make_mat("pcb_fr4_green", (0.02, 0.28, 0.12, 1.0), 0.0, 0.72)
    mat_pcb_edge = make_mat("pcb_edge_fr4_pale", (0.60, 0.62, 0.50, 1.0), 0.0, 0.75)
    mat_blue = make_mat("battery_blue_wrapper", (0.00, 0.42, 0.92, 1.0), 0.0, 0.38)
    mat_metal = make_mat("brushed_nickel_tabs", (0.78, 0.76, 0.68, 1.0), 0.75, 0.30)
    mat_solder = make_mat("solder_blobs", (0.86, 0.82, 0.72, 1.0), 1.0, 0.20)
    mat_black = make_mat("black_plastic_and_foam", (0.005, 0.005, 0.004, 1.0), 0.0, 0.70)
    mat_dark = make_mat("dark_component_black", (0.01, 0.012, 0.012, 1.0), 0.0, 0.45)
    mat_gold = make_mat("gold_pads", (0.95, 0.67, 0.22, 1.0), 1.0, 0.22)
    mat_copper = make_mat("copper_insulator_strip", (0.86, 0.25, 0.12, 1.0), 0.2, 0.35)
    mat_white = make_mat("white_connector_plastic", (0.90, 0.86, 0.75, 1.0), 0.0, 0.38)
    mat_led = make_mat("warm_led_lenses", (1.0, 0.95, 0.35, 1.0), 0.0, 0.20)
    mat_red = make_mat("red_wire", (0.80, 0.02, 0.02, 1.0), 0.0, 0.45)
    mat_wire_black = make_mat("black_wire", (0.0, 0.0, 0.0, 1.0), 0.0, 0.45)
    mat_silk = make_mat("white_silkscreen", (0.86, 0.90, 0.82, 1.0), 0.0, 0.60)

    objects: list[bpy.types.Object] = []
    parent = bpy.data.objects.new("TRIXIG_PCB_BATTERY_ASSET_ORIGIN_left_edge_pcb_bottom", None)
    parent.empty_display_type = "ARROWS"
    parent.empty_display_size = 8.0
    bpy.context.collection.objects.link(parent)
    parent["units"] = "millimeters"
    parent["pcb_length_mm"] = PCB_LENGTH
    parent["pcb_max_width_mm"] = PCB_WIDTH
    parent["pcb_thickness_mm"] = PCB_THICKNESS
    parent["battery_length_mm"] = CELL_LENGTH
    parent["battery_diameter_mm"] = CELL_DIAMETER
    objects.append(parent)

    pcb = make_pcb_outline(mat_pcb)
    objects.append(pcb)

    # Pale FR4 edge stripe along the long visible side.
    objects.append(box("PCB_laminated_edge_visible", (47.70, -13.26, 0.80), (86.0, 0.22, 1.30), mat_pcb_edge))

    # Battery core and terminals.
    battery = cyl(
        f"Battery_18650_{CELL_LENGTH:.2f}x{CELL_DIAMETER:.2f}mm",
        (CELL_CX, CELL_CY, CELL_CZ),
        CELL_RADIUS,
        CELL_LENGTH,
        mat_blue,
        vertices=128,
        rotation=(0.0, math.radians(90), 0.0),
    )
    add_weighted_normals(battery)
    objects.append(battery)
    objects.append(cyl("battery_negative_cap", (CELL_X0 - 0.34, 0, CELL_CZ), 9.05, 0.68, mat_metal, 96, (0, math.radians(90), 0), True))
    objects.append(cyl("battery_positive_cap", (CELL_X1 + 0.34, 0, CELL_CZ), 9.05, 0.68, mat_metal, 96, (0, math.radians(90), 0), True))
    objects.append(cyl("battery_positive_button", (CELL_X1 + 0.76, 0, CELL_CZ), 4.25, 0.42, mat_solder, 64, (0, math.radians(90), 0), True))

    # Battery tabs, foam and insulating strips.
    top_z = CELL_CZ + CELL_RADIUS
    objects.append(box("left_nickel_battery_tab_top", (CELL_X0 + 7.7, 0, top_z + 0.48), (15.4, 11.5, 0.80), mat_metal, 0.22))
    objects.append(box("left_nickel_battery_tab_drop", (CELL_X0 + 0.65, -5.35, 6.25), (1.30, 1.25, 10.0), mat_metal, 0.14))
    objects.append(box("right_nickel_battery_tab_top", (CELL_X1 - 7.7, 0, top_z + 0.48), (15.4, 11.5, 0.80), mat_metal, 0.22))
    objects.append(box("right_nickel_battery_tab_drop", (CELL_X1 - 0.65, 5.35, 6.25), (1.30, 1.25, 10.0), mat_metal, 0.14))
    objects.append(box("copper_isolator_left_under_tab", (CELL_X0 + 7.5, 0, top_z + 0.08), (15.0, 13.0, 0.35), mat_copper, 0.12))
    objects.append(box("black_foam_retaining_tape_over_cell", (CELL_CX + 7.0, 0, top_z + 1.05), (23.0, 20.0, 1.10), mat_black, 0.20))
    objects.append(box("black_foam_tape_left_side", (CELL_CX + 7.0, -10.0, CELL_CZ), (22.0, 1.1, 18.6), mat_black, 0.12))
    objects.append(box("black_foam_tape_right_side", (CELL_CX + 7.0, 10.0, CELL_CZ), (22.0, 1.1, 18.6), mat_black, 0.12))

    # USB-C receptacle at the tail end.
    objects.append(box("USB_C_outer_shell", (98.15, 0.0, 3.10), (6.1, 9.4, 4.1), mat_metal, 0.24))
    objects.append(box("USB_C_black_receptacle_opening", (101.25, 0.0, 3.10), (0.18, 7.15, 2.35), mat_black, 0.08))
    objects.append(box("USB_C_plastic_tongue", (101.36, 0.0, 3.10), (0.22, 4.35, 0.72), mat_dark, 0.04))
    for y in [-3.8, -1.9, 0.0, 1.9, 3.8]:
        objects.append(box(f"usb_c_pin_{y:+.1f}", (94.7, y, PCB_THICKNESS + 0.10), (1.0, 0.42, 0.10), mat_gold, 0.02))

    # Motor connector / wire solder area at the left end.
    objects.append(box("motor_wire_white_connector", (8.9, -6.9, 4.05), (8.6, 4.2, 5.1), mat_white, 0.22))
    objects.append(box("motor_wire_connector_socket_shadow", (8.9, -6.9, 6.20), (6.9, 2.8, 0.18), mat_dark, 0.04))
    objects.append(disk_on_pcb("B_plus_solder_pad", 20.0, 8.9, 1.85, mat_solder, 0.08, 0.16))
    objects.append(disk_on_pcb("B_minus_solder_pad", 73.2, 8.9, 1.85, mat_solder, 0.08, 0.16))
    objects.append(disk_on_pcb("motor_red_solder_pad", 10.7, -10.2, 1.55, mat_solder, 0.08, 0.16))
    objects.append(disk_on_pcb("motor_black_solder_pad", 5.7, -10.1, 1.55, mat_solder, 0.08, 0.16))

    # Visual holes and plated pads.
    for i, (x, y, r) in enumerate(
        [
            (2.55, -4.2, 0.92),
            (2.55, 4.2, 0.92),
            (46.5, -10.9, 1.15),
            (76.8, -6.1, 0.95),
            (83.7, 6.5, 1.05),
        ]
    ):
        objects.append(disk_on_pcb(f"pcb_dark_hole_{i+1}", x, y, r, mat_black, 0.09, 0.11))
        objects.append(disk_on_pcb(f"pcb_gold_annular_ring_{i+1}", x, y, r + 0.42, mat_gold, 0.04, 0.05))

    # Perforated pad blocks at both ends.
    for base_x, base_y, nx, ny, prefix in [(7.8, 8.1, 4, 5, "left"), (88.2, -7.8, 5, 4, "right")]:
        for ix in range(nx):
            for iy in range(ny):
                objects.append(disk_on_pcb(f"{prefix}_perf_pad_{ix}_{iy}", base_x + ix * 1.25, base_y + iy * 1.10, 0.26, mat_solder, 0.08, 0.07))

    # Representative ICs, passives, LEDs and switch components from the PCB photo.
    objects.append(box("left_soic_ic", (18.4, 4.2, PCB_THICKNESS + 0.70), (5.0, 6.4, 1.20), mat_dark, 0.14))
    objects.append(box("center_soic_controller", (46.0, -3.3, PCB_THICKNESS + 0.78), (6.4, 9.8, 1.25), mat_dark, 0.14))
    objects.append(box("right_tact_switch_body", (74.5, 1.3, PCB_THICKNESS + 1.15), (6.4, 6.4, 2.1), mat_dark, 0.18))
    objects.append(cyl("right_tact_switch_button", (74.5, 1.3, PCB_THICKNESS + 2.35), 2.65, 0.55, mat_black, 48, (0, 0, 0), True))
    objects.append(box("slide_switch_metal_can", (87.1, 4.5, PCB_THICKNESS + 2.6), (8.7, 13.5, 5.2), mat_metal, 0.22))
    objects.append(box("slide_switch_black_knob", (87.1, 4.5, PCB_THICKNESS + 5.6), (2.0, 5.4, 1.1), mat_black, 0.12))

    for i, x in enumerate([24.7, 30.1, 35.5, 40.9]):
        objects.append(box(f"status_led_{i+1}", (x, -1.0, PCB_THICKNESS + 0.45), (2.0, 1.55, 0.55), mat_led, 0.08))

    passive_specs = [
        (13.0, 0.0, 2.0, 1.0),
        (13.0, -3.0, 2.0, 1.0),
        (22.2, -5.4, 2.2, 1.1),
        (26.0, -5.4, 2.2, 1.1),
        (30.0, -5.4, 2.2, 1.1),
        (34.0, -5.4, 2.2, 1.1),
        (38.0, -5.4, 2.2, 1.1),
        (41.0, 5.7, 2.4, 1.1),
        (44.5, 5.7, 2.4, 1.1),
        (54.5, 5.6, 2.1, 1.0),
        (58.2, 5.6, 2.1, 1.0),
        (61.9, 5.6, 2.1, 1.0),
        (70.2, -7.5, 2.2, 1.0),
        (72.8, -7.5, 2.2, 1.0),
        (68.8, 7.2, 1.9, 0.95),
        (82.4, -2.8, 2.0, 1.0),
    ]
    for i, (x, y, sx, sy) in enumerate(passive_specs):
        mat = mat_white if i % 3 == 0 else mat_gold
        objects.append(box(f"smd_passive_{i+1:02d}", (x, y, PCB_THICKNESS + 0.33), (sx, sy, 0.48), mat, 0.05))

    # Simple trace/pad strips.
    trace_data = [
        (31.0, 2.9, 23.0, 0.22),
        (31.0, 3.9, 23.0, 0.22),
        (31.0, 4.9, 23.0, 0.22),
        (58.8, -1.0, 20.0, 0.20),
        (60.5, -2.1, 18.0, 0.20),
        (62.0, -3.2, 16.0, 0.20),
        (76.5, 9.6, 12.0, 0.24),
    ]
    for i, (x, y, sx, sy) in enumerate(trace_data):
        objects.append(box(f"exposed_copper_trace_{i+1}", (x, y, PCB_THICKNESS + 0.055), (sx, sy, 0.05), mat_gold, 0.02))

    # Wires leading out toward the motor.
    objects.append(make_poly_curve("red_motor_wire", [(10.7, -10.2, 2.5), (4.0, -16.0, 7.5), (-11.0, -19.5, 9.0), (-22.0, -18.0, 10.0)], 0.62, mat_red))
    objects.append(make_poly_curve("black_motor_wire", [(5.7, -10.1, 2.5), (0.0, -14.0, 8.5), (-13.0, -13.0, 11.0), (-24.0, -11.5, 11.5)], 0.62, mat_wire_black))
    objects.append(make_poly_curve("red_battery_lead", [(21.2, 7.5, 2.4), (22.8, 3.0, 7.8), (31.0, -8.5, 8.8), (42.0, -10.6, 8.8)], 0.52, mat_red))
    objects.append(make_poly_curve("black_battery_lead_shadow", [(67.0, -9.2, 2.2), (58.0, -10.5, 3.8), (47.0, -10.5, 4.8)], 0.45, mat_wire_black))

    # Silkscreen and polarity labels.
    objects.append(add_text("silkscreen_model_code", "PLMP-1454", (62.0, 0.2, PCB_THICKNESS + 0.12), 3.2, mat_silk))
    objects.append(add_text("silkscreen_b_plus", "B+", (20.1, 6.0, PCB_THICKNESS + 0.12), 2.4, mat_silk))
    objects.append(add_text("silkscreen_b_minus", "B-", (73.2, 6.0, PCB_THICKNESS + 0.12), 2.4, mat_silk))
    objects.append(add_text("battery_print", "3.6V Li-ion  +", (CELL_CX + 16.5, -2.5, top_z + 1.66), 3.2, mat_black))

    # Parent all asset geometry to the millimeter origin empty.
    for obj in objects:
        if obj is not parent:
            obj.parent = parent
        move_to_collection(obj, asset_collection)

    # Lighting and camera for verification preview.
    bpy.context.scene.world.color = (0.70, 0.72, 0.72)
    bpy.context.scene.view_settings.view_transform = "Standard"
    bpy.context.scene.view_settings.look = "Medium High Contrast"
    bpy.context.scene.view_settings.exposure = 0.7
    bpy.context.scene.view_settings.gamma = 1.0

    bpy.ops.object.light_add(type="AREA", location=v3_mm((40, -50, 70)))
    light = bpy.context.object
    light.name = "preview_softbox"
    light.data.energy = 950
    light.data.size = 70
    bpy.ops.object.light_add(type="SUN", location=v3_mm((20, -10, 80)))
    sun = bpy.context.object
    sun.name = "preview_fill_sun"
    sun.data.energy = 1.25

    bpy.ops.object.camera_add(location=v3_mm((122, -118, 76)))
    camera = bpy.context.object
    look_at(camera, (48, 0, 8))
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = m(125)
    bpy.context.scene.camera = camera

    # Add a neutral reference plane under the asset, excluded from exports.
    mat_floor = make_mat("preview_floor_matte", (0.78, 0.78, 0.74, 1.0), 0.0, 0.8)
    floor = box("preview_floor_not_exported", (48, 0, -0.08), (125, 58, 0.08), mat_floor)
    floor.hide_select = True
    for preview_obj in (light, sun, camera, floor):
        move_to_collection(preview_obj, preview_collection)

    return objects


def export_asset(objects: list[bpy.types.Object]) -> None:
    export_objects = [obj for obj in objects if obj.type != "EMPTY"]
    for obj in bpy.context.scene.objects:
        obj.select_set(False)
    for obj in export_objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = export_objects[0]

    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))

    bpy.ops.export_scene.gltf(
        filepath=str(GLB_PATH),
        export_format="GLB",
        use_selection=True,
        export_apply=True,
    )

    if "obj_export" in dir(bpy.ops.wm):
        bpy.ops.wm.obj_export(
            filepath=str(OBJ_PATH),
            export_selected_objects=True,
            export_materials=True,
            apply_modifiers=True,
            forward_axis="Y",
            up_axis="Z",
        )
    elif "obj" in dir(bpy.ops.export_scene):
        bpy.ops.export_scene.obj(
            filepath=str(OBJ_PATH),
            use_selection=True,
            use_materials=True,
            use_mesh_modifiers=True,
        )

    # Preview render, kept out of the exported selection.
    for obj in bpy.context.scene.objects:
        obj.select_set(False)
    bpy.context.scene.render.filepath = str(PNG_PATH)
    bpy.context.scene.render.resolution_x = 1800
    bpy.context.scene.render.resolution_y = 1200
    try:
        bpy.context.scene.render.engine = "BLENDER_EEVEE_NEXT"
    except TypeError:
        pass
    bpy.ops.render.render(write_still=True)


def main() -> None:
    objects = build_asset()
    export_asset(objects)
    print("TRIXIG PCB/battery asset generated:")
    print(f"  blend: {BLEND_PATH}")
    print(f"  glb:   {GLB_PATH}")
    print(f"  obj:   {OBJ_PATH}")
    print(f"  png:   {PNG_PATH}")
    print(
        "Scale anchors: PCB {:.2f} x {:.2f} x {:.2f} mm, cell {:.2f} x {:.2f} mm".format(
            PCB_LENGTH, PCB_WIDTH, PCB_THICKNESS, CELL_LENGTH, CELL_DIAMETER
        )
    )


if __name__ == "__main__":
    main()
