import bpy
import math
import random

def create_plant(name, height, leaf_count, flower_count, fruit_count=0, growth_stage='mature'):
    # Creează tulpina
    bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=height)
    stem = bpy.context.active_object
    stem.name = f"{name}_stem"

    # Ajustează dimensiunile în funcție de stadiul de creștere
    if growth_stage == 'seedling':
        stem.scale = (0.3, 0.3, 0.2)
        leaf_count = max(2, leaf_count // 4)
        flower_count = 0
        fruit_count = 0
    elif growth_stage == 'young':
        stem.scale = (0.6, 0.6, 0.5)
        leaf_count = max(4, leaf_count // 2)
        flower_count = flower_count // 2
        fruit_count = fruit_count // 4

    # Adaugă frunze
    for i in range(leaf_count):
        bpy.ops.mesh.primitive_plane_add(size=0.3)
        leaf = bpy.context.active_object
        leaf.name = f"{name}_leaf_{i}"
        
        # Poziționează și rotește frunza
        angle = (i / leaf_count) * 2 * math.pi
        leaf.location = (0.1 * math.cos(angle), 0.1 * math.sin(angle), (i / leaf_count) * height)
        leaf.rotation_euler = (random.uniform(0, 0.5), random.uniform(0, 0.5), angle)
        
        # Adaugă modificator Subdivision Surface
        subsurf = leaf.modifiers.new(type="SUBSURF", name="Subsurf")
        subsurf.levels = 2
        
        # Parent la tulpină
        leaf.parent = stem

    # Adaugă flori
    for i in range(flower_count):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1)
        flower = bpy.context.active_object
        flower.name = f"{name}_flower_{i}"
        
        # Poziționează floarea
        angle = (i / flower_count) * 2 * math.pi
        flower.location = (0.15 * math.cos(angle), 0.15 * math.sin(angle), height * 0.8 + 0.1)
        
        # Adaugă material pentru floare
        mat = bpy.data.materials.new(name=f"{name}_flower_material")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        material_output = nodes.get("Material Output")
        node_emission = nodes.new(type="ShaderNodeEmission")
        node_emission.inputs[0].default_value = (1, 1, 0.5, 1)  # Culoare galbenă
        mat.node_tree.links.new(node_emission.outputs[0], material_output.inputs[0])
        flower.data.materials.append(mat)
        
        # Parent la tulpină
        flower.parent = stem

    # Adaugă fructe
    for i in range(fruit_count):
        if name == "tomato":
            bpy.ops.mesh.primitive_uv_sphere_add(radius=0.15)
        elif name == "cucumber":
            bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.3)
        elif name == "bell_pepper":
            bpy.ops.mesh.primitive_cone_add(radius1=0.1, radius2=0.05, depth=0.2)
        elif name == "strawberry":
            bpy.ops.mesh.primitive_cone_add(radius1=0.08, radius2=0.05, depth=0.1)
        else:
            continue

        fruit = bpy.context.active_object
        fruit.name = f"{name}_fruit_{i}"
        
        # Poziționează fructul
        angle = (i / fruit_count) * 2 * math.pi
        fruit.location = (0.2 * math.cos(angle), 0.2 * math.sin(angle), height * 0.6 + 0.1)
        
        # Adaugă material pentru fruct
        mat = bpy.data.materials.new(name=f"{name}_fruit_material")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        material_output = nodes.get("Material Output")
        node_emission = nodes.new(type="ShaderNodeEmission")
        if name == "tomato":
            node_emission.inputs[0].default_value = (1, 0, 0, 1)  # Roșu
        elif name == "cucumber":
            node_emission.inputs[0].default_value = (0, 0.5, 0, 1)  # Verde închis
        elif name == "bell_pepper":
            node_emission.inputs[0].default_value = (1, 0.5, 0, 1)  # Portocaliu
        elif name == "strawberry":
            node_emission.inputs[0].default_value = (1, 0, 0.2, 1)  # Roșu-roz
        mat.node_tree.links.new(node_emission.outputs[0], material_output.inputs[0])
        fruit.data.materials.append(mat)
        
        # Parent la tulpină
        fruit.parent = stem

    return stem

def create_greenhouse(width, length, height):
    # Creează podeaua
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, location=(0, 0, 0))
    floor = bpy.context.active_object
    floor.name = "Greenhouse_Floor"
    floor.scale = (width, length, 1)

    # Creează pereții
    for i in range(4):
        bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False)
        wall = bpy.context.active_object
        wall.name = f"Greenhouse_Wall_{i}"
        if i % 2 == 0:
            wall.scale = (width, height, 1)
            wall.location = (0, length/2 * (-1)**i, height/2)
            wall.rotation_euler = (math.pi/2, 0, 0)
        else:
            wall.scale = (length, height, 1)
            wall.location = (width/2 * (-1)**((i-1)//2), 0, height/2)
            wall.rotation_euler = (math.pi/2, 0, math.pi/2)

    # Creează acoperișul
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, location=(0, 0, height))
    roof = bpy.context.active_object
    roof.name = "Greenhouse_Roof"
    roof.scale = (width, length, 1)

    # Adaugă material transparent pentru pereți și acoperiș
    glass_material = bpy.data.materials.new(name="Glass")
    glass_material.use_nodes = True
    nodes = glass_material.node_tree.nodes
    links = glass_material.node_tree.links
    material_output = nodes.get("Material Output")
    node_glass = nodes.new(type="ShaderNodeBsdfGlass")
    node_glass.inputs["Roughness"].default_value = 0.1
    links.new(node_glass.outputs["BSDF "], material_output.inputs["Surface"])
    for obj in bpy.data.objects:
        if obj.name.startswith("Greenhouse_"):
            obj.data.materials.append(glass_material)

# Creează plantele
plants = [
    create_plant("Tomato", 1.5, 10, 5, 3, 'mature'),
    create_plant("Cucumber", 2.0, 15, 1, 2, 'young'),
    create_plant("Bell Pepper", 1.2, 8, 3, 1, 'seedling'),
    create_plant("Basil", 0.8, 6, 1, 0, 'mature'),
    create_plant("Strawberry", 0.5, 4, 1, 2, 'young')
]

# Creează serea
create_greenhouse(5, 10, 3)

# Setează camera activă
bpy.context.scene.camera = bpy.context.object

# Renderizează scena
bpy.ops.render.render(write_still=True)
