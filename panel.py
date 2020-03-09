import bpy
from bpy.props import BoolProperty, StringProperty

bpy.types.Scene.key_loc = BoolProperty(name="Key Location", default=1)
bpy.types.Scene.key_rot = BoolProperty(name="Key Rotation", default=1)
bpy.types.Scene.key_scale = BoolProperty(name="Key Scale", default=1)
bpy.types.Scene.key_vis = BoolProperty(name="Key Visibility", default=0)
bpy.types.Scene.join_anim_name = StringProperty(name="Animation Name", default="Animation Name")

class BakeParticlesPanel(bpy.types.Panel):
    bl_idname = "VIEWPORT_PT_bakeParticles_panel"
    bl_label = "Bake Particles"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # BAKE PARTICLE SYSTEM
        layout.prop(scene,"key_loc",text="Key Location")
        layout.prop(scene,"key_rot",text="Key Rotation")
        layout.prop(scene,"key_scale",text="Key Scale")
        layout.prop(scene,"key_vis",text="Key Visibility")
        bake_particle_op = layout.operator("object.bake_particles", text="Bake Particles")
        bake_particle_op.KEYFRAME_LOCATION = scene.key_loc
        bake_particle_op.KEYFRAME_ROTATION = scene.key_rot
        bake_particle_op.KEYFRAME_SCALE = scene.key_scale
        bake_particle_op.KEYFRAME_VISIBILITY = scene.key_vis

        # JOIN ANIMATION
        layout.prop(scene,"join_anim_name",text="Animation Name")
        join_anim_op = layout.operator("scene.join_anim", text="Join Animaiton")
        join_anim_op.anim_name = scene.join_anim_name

