import bpy



class BakeParticlesPanel(bpy.types.Panel):
    bl_idname = "PS2KEY_PT_bake_ps_panel"
    bl_label = "Bake Particles"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # particle settings
        layout.prop(scene.particle_settings,"key_loc",text="Key Location")
        layout.prop(scene.particle_settings,"key_rot",text="Key Rotation")
        layout.prop(scene.particle_settings,"key_scale",text="Key Scale")
        layout.prop(scene.particle_settings,"key_vis",text="Key Visibility")
        layout.prop(scene.particle_settings,"frame_offset",text="Frame Offset")
        layout.prop(scene.particle_settings,"collection_name",text="")

        # Bake Operator
        bake_particle_op = layout.operator("object.bake_particles", text="Bake Particles")
        bake_particle_op.KEYFRAME_LOCATION = scene.particle_settings.key_loc
        bake_particle_op.KEYFRAME_ROTATION = scene.particle_settings.key_rot
        bake_particle_op.KEYFRAME_SCALE = scene.particle_settings.key_scale
        bake_particle_op.KEYFRAME_VISIBILITY = scene.particle_settings.key_vis


class AnimationNaming(bpy.types.Panel):
    bl_idname = "PS2KEY_PT_anim_rename_panel"
    bl_label = "Animation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # DECIMATE KEYFRAMES
        layout.label(text="Decimate Keyframes")
        layout.prop(scene.animation_settings,"simplify_keyframes_enum",text="")
        layout.prop(scene.animation_settings,"decimate_ratio",text="")
        simplify_keyframe_op = layout.operator("scene.simplify_keyframes",text="Simplify Keyframes")
        simplify_keyframe_op.mode = scene.animation_settings.simplify_keyframes_enum
        simplify_keyframe_op.decimate_ratio = scene.animation_settings.decimate_ratio

        # JOIN ANIMATION
        layout.label(text="Animation")
        layout.prop(scene.animation_settings,"join_anim_name",text="")
        layout.operator("scene.rename_anim", text="Rename Animaiton").anim_name = scene.animation_settings.join_anim_name
        layout.operator("scene.join_anim", text="Join Animaiton").anim_name = scene.animation_settings.join_anim_name
