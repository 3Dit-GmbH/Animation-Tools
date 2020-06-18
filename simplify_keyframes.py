import bpy

class SimplifyKeyframes(bpy.types.Operator):
    bl_idname = "scene.simplify_keyframes"
    bl_label = "Simplify Keyframes"
    bl_description = "Simplify the Keyframes by the selected decimate ratio, higher values will reduce more keyframes"
    bl_options = {"REGISTER"}

    decimate_ratio : bpy.props.FloatProperty()
    mode : bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        context.area.type = 'GRAPH_EDITOR'
        bpy.ops.graph.select_all(action='SELECT')

        # bpy.ops.graph.decimate(mode='RATIO', remove_ratio=0.8)
        bpy.ops.graph.decimate(mode=self.mode,remove_ratio=self.decimate_ratio, remove_error_margin=self.decimate_ratio)

        context.area.type = 'VIEW_3D'

        return {"FINISHED"}
