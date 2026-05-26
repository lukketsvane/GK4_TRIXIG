"""
Realistic Bambu Textured PEI Plate material for Blender.
Run from Blender's Scripting workspace (open script -> Run).

What it does:
1. Finds the build plate object (printplate / base) in the scene.
2. Builds a procedural gold-textured PEI material (no external textures needed):
   - gold base color
   - speckled Voronoi micro-grain for the textured PEI surface
   - low-frequency noise so the gold is not perfectly uniform
   - bump map driven by Voronoi + Noise for real geometric texture
   - slight anisotropic look via roughness variation
3. Sets the world background to the bright white look from earlier.
4. Switches the active render engine to Cycles and enables a few quality settings.
"""

import bpy
import math


# -------------------------------------------------------------------------
# 1. Locate the build plate object
# -------------------------------------------------------------------------
def find_plate():
    candidates = []
    # Prefer objects in a 'printplate' collection
    for col in bpy.data.collections:
        if "printplate" in col.name.lower() or "print_plate" in col.name.lower():
            for ob in col.all_objects:
                if ob.type == "MESH":
                    candidates.append(ob)
    # Fallback: any mesh whose name hints it is the plate / base
    if not candidates:
        for ob in bpy.data.objects:
            if ob.type != "MESH":
                continue
            n = ob.name.lower()
            if any(k in n for k in ("plate", "base", "build")):
                candidates.append(ob)
    if not candidates:
        return None
    # Pick the largest mesh (the plate is bigger than tiny "base" sub-parts)
    return max(candidates, key=lambda o: o.dimensions.x * o.dimensions.y)


# -------------------------------------------------------------------------
# 2. Build the PEI gold material with shader nodes
# -------------------------------------------------------------------------
def build_pei_material(name="Bambu_Textured_PEI"):
    mat = bpy.data.materials.get(name)
    if mat is None:
        mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nt = mat.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)

    # Output + Principled BSDF
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    out.location = (1100, 0)

    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.location = (700, 0)

    # Texture coordinates -> Mapping (so we can scale the speckles)
    tex_coord = nt.nodes.new("ShaderNodeTexCoord")
    tex_coord.location = (-1100, 0)

    mapping = nt.nodes.new("ShaderNodeMapping")
    mapping.location = (-900, 0)
    mapping.inputs["Scale"].default_value = (1.0, 1.0, 1.0)
    nt.links.new(tex_coord.outputs["Object"], mapping.inputs["Vector"])

    # ---- Speckle (Voronoi) — the dominant PEI grain ---------------------
    voronoi = nt.nodes.new("ShaderNodeTexVoronoi")
    voronoi.location = (-650, 250)
    voronoi.feature = "F1"
    voronoi.inputs["Scale"].default_value = 1200.0      # very fine grain
    voronoi.inputs["Randomness"].default_value = 1.0
    nt.links.new(mapping.outputs["Vector"], voronoi.inputs["Vector"])

    voronoi_ramp = nt.nodes.new("ShaderNodeValToRGB")   # ColorRamp
    voronoi_ramp.location = (-400, 250)
    cr = voronoi_ramp.color_ramp
    # remap so most pixels are mid-bright with darker pits
    cr.elements[0].position = 0.0
    cr.elements[0].color = (0.05, 0.05, 0.05, 1.0)
    cr.elements[1].position = 0.55
    cr.elements[1].color = (1.0, 1.0, 1.0, 1.0)
    nt.links.new(voronoi.outputs["Distance"], voronoi_ramp.inputs["Fac"])

    # ---- Larger noise so the gold isn't uniform -------------------------
    noise = nt.nodes.new("ShaderNodeTexNoise")
    noise.location = (-650, -100)
    noise.inputs["Scale"].default_value = 18.0
    noise.inputs["Detail"].default_value = 6.0
    noise.inputs["Roughness"].default_value = 0.6
    nt.links.new(mapping.outputs["Vector"], noise.inputs["Vector"])

    noise_ramp = nt.nodes.new("ShaderNodeValToRGB")
    noise_ramp.location = (-400, -100)
    nr = noise_ramp.color_ramp
    nr.elements[0].position = 0.35
    nr.elements[0].color = (0.0, 0.0, 0.0, 1.0)
    nr.elements[1].position = 0.65
    nr.elements[1].color = (1.0, 1.0, 1.0, 1.0)
    nt.links.new(noise.outputs["Fac"], noise_ramp.inputs["Fac"])

    # ---- Gold colour mix -----------------------------------------------
    gold_dark = nt.nodes.new("ShaderNodeRGB")
    gold_dark.location = (-400, 500)
    gold_dark.outputs[0].default_value = (0.42, 0.30, 0.10, 1.0)

    gold_light = nt.nodes.new("ShaderNodeRGB")
    gold_light.location = (-400, 700)
    gold_light.outputs[0].default_value = (0.95, 0.78, 0.32, 1.0)

    color_mix = nt.nodes.new("ShaderNodeMixRGB")
    color_mix.location = (-100, 500)
    color_mix.blend_type = "MIX"
    nt.links.new(noise_ramp.outputs["Color"], color_mix.inputs["Fac"])
    nt.links.new(gold_dark.outputs[0], color_mix.inputs[1])
    nt.links.new(gold_light.outputs[0], color_mix.inputs[2])

    # Tint by speckle so pits look slightly darker
    final_color = nt.nodes.new("ShaderNodeMixRGB")
    final_color.location = (200, 500)
    final_color.blend_type = "MULTIPLY"
    final_color.inputs["Fac"].default_value = 0.55
    nt.links.new(color_mix.outputs["Color"], final_color.inputs[1])
    nt.links.new(voronoi_ramp.outputs["Color"], final_color.inputs[2])
    nt.links.new(final_color.outputs["Color"], bsdf.inputs["Base Color"])

    # ---- Roughness: not too smooth, slightly varying --------------------
    rough_ramp = nt.nodes.new("ShaderNodeValToRGB")
    rough_ramp.location = (-100, 200)
    rr = rough_ramp.color_ramp
    rr.elements[0].position = 0.0
    rr.elements[0].color = (0.45, 0.45, 0.45, 1.0)
    rr.elements[1].position = 1.0
    rr.elements[1].color = (0.85, 0.85, 0.85, 1.0)
    nt.links.new(voronoi_ramp.outputs["Color"], rough_ramp.inputs["Fac"])
    nt.links.new(rough_ramp.outputs["Color"], bsdf.inputs["Roughness"])

    # ---- Bump: real surface texture -------------------------------------
    bump_combine = nt.nodes.new("ShaderNodeMixRGB")
    bump_combine.location = (200, -150)
    bump_combine.blend_type = "ADD"
    bump_combine.inputs["Fac"].default_value = 0.6
    nt.links.new(voronoi_ramp.outputs["Color"], bump_combine.inputs[1])
    nt.links.new(noise_ramp.outputs["Color"], bump_combine.inputs[2])

    bump = nt.nodes.new("ShaderNodeBump")
    bump.location = (450, -150)
    bump.inputs["Strength"].default_value = 0.55
    bump.inputs["Distance"].default_value = 0.02
    nt.links.new(bump_combine.outputs["Color"], bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])

    # ---- Metallic / specular --------------------------------------------
    bsdf.inputs["Metallic"].default_value = 0.85
    # IOR/Specular tweak when available (varies between Blender versions)
    if "Specular IOR Level" in bsdf.inputs:
        bsdf.inputs["Specular IOR Level"].default_value = 0.5
    elif "Specular" in bsdf.inputs:
        bsdf.inputs["Specular"].default_value = 0.5

    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


# -------------------------------------------------------------------------
# 3. Bright white world background (the look you liked)
# -------------------------------------------------------------------------
def setup_world():
    world = bpy.context.scene.world
    if world is None:
        world = bpy.data.worlds.new("World")
        bpy.context.scene.world = world
    world.use_nodes = True
    nt = world.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)

    bg = nt.nodes.new("ShaderNodeBackground")
    bg.location = (0, 0)
    bg.inputs["Color"].default_value = (1.0, 1.0, 1.0, 1.0)
    bg.inputs["Strength"].default_value = 1.6  # bright but not blown out

    out = nt.nodes.new("ShaderNodeOutputWorld")
    out.location = (300, 0)
    nt.links.new(bg.outputs["Background"], out.inputs["Surface"])


# -------------------------------------------------------------------------
# 4. Render settings — Cycles, decent quality
# -------------------------------------------------------------------------
def setup_render():
    scn = bpy.context.scene
    scn.render.engine = "CYCLES"
    scn.cycles.samples = 256
    scn.cycles.use_denoising = True
    scn.view_settings.view_transform = "AgX" if "AgX" in [
        v.name for v in bpy.types.ColorManagedViewSettings.bl_rna.properties["view_transform"].enum_items
    ] else "Filmic"
    scn.view_settings.look = "Medium High Contrast"


# -------------------------------------------------------------------------
# main
# -------------------------------------------------------------------------
def main():
    plate = find_plate()
    if plate is None:
        print("[PEI] could not find a build-plate mesh; "
              "select it manually and re-run, or rename the collection to 'printplate'.")
        return

    print(f"[PEI] applying material to: {plate.name}")
    mat = build_pei_material()
    plate.data.materials.clear()
    plate.data.materials.append(mat)

    setup_world()
    setup_render()
    print("[PEI] done.")


main()
