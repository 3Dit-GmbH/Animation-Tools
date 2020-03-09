import bpy


class BakeParticlesOperator(bpy.types.Operator):
    """Bake all Particles to Keyframes"""
    bl_idname = "object.bake_particles"
    bl_label = "Bake Particles"

    KEYFRAME_LOCATION : bpy.props.BoolProperty()
    KEYFRAME_ROTATION : bpy.props.BoolProperty()
    KEYFRAME_SCALE : bpy.props.BoolProperty()
    KEYFRAME_VISIBILITY : bpy.props.BoolProperty()  # Viewport and render visibility.  

    @classmethod
    def poll(cls, context):
        if len(context.object.particle_systems) > 0:
            return True
        return False

    def create_objects_for_particles(self, ps, obj):
        # Duplicate the given object for every particle and return the duplicates.
        # Use instances instead of full copies.
        obj_list = []
        mesh = obj.data

        # Create a new collection and link it to the scene.
        particleCollection = bpy.data.collections.new("Particle Collection")
        bpy.context.scene.collection.children.link(particleCollection)

        for particle in ps.particles:
            dupli = bpy.data.objects.new(name=obj.name, object_data=mesh)
            particleCollection.objects.link(dupli)
            obj_list.append(dupli)
        return obj_list

    def match_and_keyframe_objects(self, ps, obj_list, start_frame, end_frame):
        # Match and keyframe the objects to the particles for every frame in the
        # given range.
        for frame in range(start_frame, end_frame + 1):
            bpy.context.scene.frame_set(frame)
            for p, obj in zip(ps.particles, obj_list):
                self.match_object_to_particle(p, obj)
                self.keyframe_obj(obj)

    def match_object_to_particle(self, p, obj):
        # Match the location, rotation, scale and visibility of the object to
        # the particle.
        loc = p.location
        rot = p.rotation
        size = p.size
        obj.location = loc
        # Set rotation mode to quaternion to match particle rotation.
        obj.rotation_mode = 'QUATERNION'
        obj.rotation_quaternion = rot
        obj.scale = (size, size, size)
        if self.KEYFRAME_VISIBILITY:
            if p.alive_state == 'ALIVE':
                vis = True
            else:
                vis = False

            obj.hide_viewport = not(vis)
            obj.hide_render = not(vis)

    def keyframe_obj(self, obj):
        # Keyframe location, rotation, scale and visibility if specified.
        if self.KEYFRAME_LOCATION:
            obj.keyframe_insert("location")
        if self.KEYFRAME_ROTATION:
            obj.keyframe_insert("rotation_quaternion")
        if self.KEYFRAME_SCALE:
            obj.keyframe_insert("scale")
        if self.KEYFRAME_VISIBILITY:
            obj.keyframe_insert("hide_viewport")
            obj.keyframe_insert("hide_render")

    # def main():

    def execute(self, context):

        # Assume only 2 objects are selected.
        # The active object should be the one with the particle system.
        emitter = bpy.context.object
        instance = emitter.particle_systems[0].settings.instance_object

        depsgraph = bpy.context.evaluated_depsgraph_get()

        # Extract locations
        ps = depsgraph.objects[emitter.name].particle_systems[0]

        start_frame = bpy.context.scene.frame_start
        end_frame = bpy.context.scene.frame_end
        obj_list = self.create_objects_for_particles(ps, instance)
        self.match_and_keyframe_objects(ps, obj_list, start_frame, end_frame)

        return {'FINISHED'}
