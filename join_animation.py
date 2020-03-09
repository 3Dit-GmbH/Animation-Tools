import bpy

class JoinAnimationOperator(bpy.types.Operator):
    bl_idname = "scene.join_anim"
    bl_label = "Join Animation"
    bl_description = "Join animations for all selected objects by making an NLA strip for each object and naming the track consistently"
    bl_options = {"REGISTER"}

    anim_name : bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        sel_objects = context.selected_objects
        for obj in sel_objects:
            action = obj.animation_data.action
            if action:
                track = obj.animation_data.nla_tracks.new()
                track.strips.new(self.anim_name, action.frame_range[1], action)
                track.name = self.anim_name
                obj.animation_data.action = None
        return {"FINISHED"}
