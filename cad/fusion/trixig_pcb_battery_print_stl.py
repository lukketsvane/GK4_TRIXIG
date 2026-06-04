"""
Create a simplified, 3D-print-oriented STL of the TRIXIG PCB + battery module.

This version intentionally removes tiny render-only details from the GLB:
  - no SMD resistors/caps, traces, silkscreen, or loose wires
  - simplified main blocks for USB-C, switch, connector, tape, tabs, and cell caps
  - raw STL coordinates are millimeters for slicers such as Bambu Studio/PrusaSlicer
"""

from __future__ import annotations

from pathlib import Path
import math

import bpy


SCRIPT_DIR = Path(__file__).resolve().parent
ASSET_DIR = SCRIPT_DIR / "pcb_battery_asset"
PRINT_DIR = SCRIPT_DIR.parent / "print" / "trixig_redesign" / "for_bambu"
ASSET_DIR.mkdir(exist_ok=True)
PRINT_DIR.mkdir(parents=True, exist_ok=True)

STL_PATH = ASSET_DIR / "trixig_pcb_battery_simplified_print_mm.stl"
PRINT_STL_PATH = PRINT_DIR / "pcb_battery_simplified_print_mm.stl"
BLEND_PATH = ASSET_DIR / "trixig_pcb_battery_simplified_print_mm.blend"


# Hard scale anchors from the caliper photos.
PCB_LENGTH = 95.39
PCB_WIDTH = 26.31
PCB_THICKNESS = 1.60

CELL_LENGTH = 65.02
CELL_DIAMETER = 18.60
CELL_RADIUS = CELL_DIAMETER / 2.0
CELL_X0 = (PCB_LENGTH - CELL_LENGTH) / 2.0
CELL_X1 = CELL_X0 + CELL_LENGTH
CELL_CX = (CELL_X0 + CELL_X1) / 2.0
CELL_CZ = PCB_THICKNESS + CELL_RADIUS - 0.35  # slight overlap into PCB for slicing


def reset_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    bpy.context.scene.unit_settings.system = "METRIC"
    bpy.context.scene.unit_settings.scale_length = 0.001
    bpy.context.scene.unit_settings.length_unit = "MILLIMETERS"


def material(name: str, rgba: tuple[float, float, float, float]) -> bpy.types.Material:
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = rgba
    return mat


def add_bevel(obj: bpy.types.Object, width: float, segments: int = 2) -> None:
    bevel = obj.modifiers.new("print_softened_edges", "BEVEL")
    bevel.width = width
    bevel.segments = segments
    bevel.affect = "EDGES"
    normals = obj.modifiers.new("weighted_normals", "WEIGHTED_NORMAL")
    normals.keep_sharp = True


def add_box(
    name: str,
    loc: tuple[float, float, float],
    dims: tuple[float, float, float],
    mat: bpy.types.Material,
    bevel: float = 0.0,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    if bevel:
        add_bevel(obj, bevel)
    return obj


def add_cylinder(
    name: str,
    loc: tuple[float, float, float],
    radius: float,
    depth: float,
    mat: bpy.types.Material,
    vertices: int = 64,
    rotation: tuple[float, float, float] = (0, 0, 0),
    bevel: float = 0.0,
) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=radius,
        depth=depth,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_mesh"
    obj.data.materials.append(mat)
    bpy.ops.object.shade_smooth()
    if bevel:
        add_bevel(obj, bevel)
    return obj


def make_pcb_outline(mat: bpy.types.Material) -> bpy.types.Object:
    half_w = PCB_WIDTH / 2.0
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
    verts = [(x, y, 0.0) for x, y in pts] + [(x, y, PCB_THICKNESS) for x, y in pts]
    n = len(pts)
    faces = [tuple(range(n - 1, -1, -1)), tuple(range(n, 2 * n))]
    for i in range(n):
        faces.append((i, (i + 1) % n, (i + 1) % n + n, i + n))

    mesh = bpy.data.meshes.new("PCB_print_outline_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new("PCB_print_outline_95.39x26.31x1.60mm", mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(mat)
    add_bevel(obj, 0.18, 2)
    return obj


def build_print_model() -> list[bpy.types.Object]:
    reset_scene()
    mat_pcb = material("print_pcb_green", (0.0, 0.35, 0.12, 1))
    mat_cell = material("print_cell_body", (0.0, 0.35, 0.85, 1))
    mat_detail = material("print_simplified_detail", (0.85, 0.82, 0.74, 1))
    mat_tape = material("print_foam_tape_black", (0.02, 0.02, 0.02, 1))

    objects: list[bpy.types.Object] = []
    objects.append(make_pcb_outline(mat_pcb))

    # One 18650 cell, kept exact in length/diameter and slightly overlapped with the PCB.
    objects.append(
        add_cylinder(
            "battery_18650_print_65.02x18.60mm",
            (CELL_CX, 0.0, CELL_CZ),
            CELL_RADIUS,
            CELL_LENGTH,
            mat_cell,
            vertices=80,
            rotation=(0, math.radians(90), 0),
            bevel=0.05,
        )
    )
    objects.append(add_cylinder("battery_negative_cap_print", (CELL_X0 - 0.25, 0, CELL_CZ), 9.05, 0.50, mat_detail, 64, (0, math.radians(90), 0), 0.05))
    objects.append(add_cylinder("battery_positive_cap_print", (CELL_X1 + 0.25, 0, CELL_CZ), 9.05, 0.50, mat_detail, 64, (0, math.radians(90), 0), 0.05))

    top_z = CELL_CZ + CELL_RADIUS

    # Printable large details only.
    objects.append(add_box("left_battery_tab_print", (CELL_X0 + 8.0, 0, top_z + 0.25), (16.0, 11.0, 0.70), mat_detail, 0.18))
    objects.append(add_box("right_battery_tab_print", (CELL_X1 - 8.0, 0, top_z + 0.25), (16.0, 11.0, 0.70), mat_detail, 0.18))
    objects.append(add_box("central_foam_retainer_print", (CELL_CX + 7.0, 0, top_z + 0.85), (24.0, 20.0, 1.40), mat_tape, 0.20))

    objects.append(add_box("usb_c_block_print", (98.0, 0.0, 3.1), (6.5, 9.8, 4.4), mat_detail, 0.22))
    objects.append(add_box("usb_c_opening_recess_print", (101.35, 0.0, 3.1), (0.55, 6.9, 2.0), mat_tape, 0.08))
    objects.append(add_box("motor_connector_block_print", (8.8, -6.8, 4.0), (8.8, 4.4, 5.2), mat_detail, 0.20))
    objects.append(add_box("slide_switch_block_print", (87.1, 4.5, PCB_THICKNESS + 2.6), (8.8, 13.2, 5.2), mat_detail, 0.20))
    objects.append(add_box("slide_switch_knob_print", (87.1, 4.5, PCB_THICKNESS + 5.7), (2.2, 5.2, 1.2), mat_tape, 0.10))
    objects.append(add_box("center_controller_block_print", (46.0, -3.2, PCB_THICKNESS + 0.85), (6.6, 9.8, 1.35), mat_tape, 0.12))
    objects.append(add_box("left_ic_block_print", (18.4, 4.2, PCB_THICKNESS + 0.75), (5.2, 6.4, 1.25), mat_tape, 0.12))
    objects.append(add_box("right_tact_switch_print", (74.5, 1.3, PCB_THICKNESS + 1.15), (6.4, 6.4, 2.1), mat_tape, 0.15))

    # Bigger-than-real LED nubs so the visual read survives a print.
    for i, x in enumerate([25.0, 30.5, 36.0, 41.5], start=1):
        objects.append(add_box(f"status_led_lump_{i}_print", (x, -1.0, PCB_THICKNESS + 0.42), (2.1, 1.6, 0.65), mat_detail, 0.08))

    # A few large solder/rivet marks as raised printable circles.
    for i, (x, y, r) in enumerate([(2.5, -4.2, 1.1), (2.5, 4.2, 1.1), (20.0, 8.9, 1.9), (73.2, 8.9, 1.9), (83.7, 6.5, 1.1)], start=1):
        objects.append(add_cylinder(f"large_pad_{i}_print", (x, y, PCB_THICKNESS + 0.10), r, 0.20, mat_detail, 32, bevel=0.03))

    return objects


def export_stl(objects: list[bpy.types.Object], path: Path) -> None:
    bpy.ops.object.select_all(action="DESELECT")
    for obj in objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]
    bpy.ops.wm.stl_export(
        filepath=str(path),
        export_selected_objects=True,
        apply_modifiers=True,
        ascii_format=False,
        global_scale=1.0,
        use_scene_unit=False,
    )


def main() -> None:
    objects = build_print_model()
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    export_stl(objects, STL_PATH)
    export_stl(objects, PRINT_STL_PATH)
    print("Simplified print STL generated:")
    print(f"  {STL_PATH}")
    print(f"  {PRINT_STL_PATH}")
    print(f"  {BLEND_PATH}")


if __name__ == "__main__":
    main()
