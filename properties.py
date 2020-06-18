import bpy
from bpy.props import BoolProperty, StringProperty, PointerProperty, IntProperty, FloatProperty, EnumProperty


class ParticleSettings(bpy.types.PropertyGroup):
    key_loc: BoolProperty(name="Key Location", default=1)
    key_rot: BoolProperty(name="Key Rotation", default=1)
    key_scale: BoolProperty(name="Key Scale", default=1)
    key_vis: BoolProperty(name="Key Visibility", default=0)
    frame_offset: IntProperty(name="Frame Offset", default=1)
    collection_name: StringProperty(
        name="Collection Name", default="Collection Name")


bpy.utils.register_class(ParticleSettings)
bpy.types.Scene.particle_settings = PointerProperty(type=ParticleSettings)


class AnimationSettings(bpy.types.PropertyGroup):
    simplify_keyframes_modes = [
        ("RATIO", "RATIO",
         "Use a percentage to specify how many keyframes you want to remove."),
        ("ERROR", "ERROR ", "Use an error margin to specify how much the curve is allowed to deviate from the original path.")
    ]

    simplify_keyframes_enum: EnumProperty(
        name='Simplify Mode', description='Choose mode to decimate keyframes', items=simplify_keyframes_modes)
    join_anim_name: StringProperty(
        name="Animation Name", default="Animation Name")
    decimate_ratio: FloatProperty(name="Decimate Ratio", default=0.1)


bpy.utils.register_class(AnimationSettings)
bpy.types.Scene.animation_settings = PointerProperty(type=AnimationSettings)
