bl_info = {
    "name": "VRC2NeosBones",
    "blender": (2, 80, 0),
    'version': (0, 1, 0),
    'author': 'hazre',
    "description": "A tool designed to rename VRChat avatar bones to NeosVR ones.",
    "category": "3D View",
    "location": "View 3D > Tool Shelf > VRC2Neos",
    "tracker_url": "https://github.com/hazre/VRC2NeosBones-blender-plugin/issues",
}

import bpy

class VRC2NeosBones_bones_panel(bpy.types.Panel):
    bl_label = "Bones"
    bl_idname = "VRC2NeosBones_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "VRC2Neos"

    def draw(self, context):
        layout = self.layout
        layout.operator("vrc2neosbones.operator")

class VRC2NeosBones_op(bpy.types.Operator):
    bl_label = "Rename"
    bl_idname = "vrc2neosbones.operator"

    def execute(self, context):
        
        #you still need to fix it up until the point you would normally rename the bones
        #credit to Hallow for original script https://gamebanana.com/tools/6414
        #edited by hazre for VRChat to NeosVR avatar conversion

        obj = context.object
        namelist = [
        #("BoneNameYouWantRenamed", "BoneNameToRenameBoneTo")
        #Example:
        #("chest_a", "Spine1"),
        # Templete

        ("Hips", "Hips"),
        ("Spine", "Spine"),
        ("Chest", "Chest"),
        ("Neck", "Neck"),
        ("Jaw", "jawbone"),

        ("LeftEye", "Eye.L"),
        ("RightEye", "Eye.L"),

        ("Shoulder_R", "Shoulder.R"),
        ("UpperArm_R", "Upper_Arm.R"),
        ("LowerArm_R", "Lower_Arm.R"),
        ("Hand_R", "Hand.R"),

        ("Shoulder_L", "Shoulder.L"),
        ("UpperArm_L", "Upper_Arm.L"),
        ("LowerArm_L", "Lower_Arm.L"),
        ("Hand_L", "Hand.L"),

        #alternative for unity
        ("RightShoulder", "Shoulder.R"),
        ("RightUpperArm", "Upper_Arm.R"),
        ("RightLowerArm", "Lower_Arm.R"),
        ("RightHand", "Hand.R"),

        ("LeftShoulder", "Shoulder.R"),
        ("LeftUpperArm", "Upper_Arm.R"),
        ("LeftLowerArm", "Lower_Arm.R"),
        ("LeftHand", "Hand.R"),

        ("UpperLeg_R", "Upper_Leg.R"),
        ("LowerLeg_R", "Lower_Leg.R"),
        ("Foot_R", "Foot.R"),
        ("Toe_R", "Toe.R"),

        ("UpperLeg_L", "Upper_Leg.L"),
        ("LowerLeg_L", "Lower_Leg.L"),
        ("Foot_L", "Foot.L"),
        ("Toe_L", "Toe.L"),

        #alternative for unity
        ("RightUpperLeg", "Upper_Leg.R"),
        ("RightLowerLeg", "Lower_Leg.R"),
        ("RightFoot", "Foot.R"),
        ("RightToes", "Toe.R"),

        ("LeftUpperLeg", "Upper_Leg.L"),
        ("LeftLowerLeg", "Lower_Leg.L"),
        ("LeftFoot", "Foot.L"),
        ("LeftToes", "Toe.L"),

        ("Index1_R", "Index1.R"),
        ("Thumb1_R", "Thumb1.R"),
        ("Middle1_R", "Middle1.R"),
        ("Ring1_R", "Ring1.R"),
        ("Pinky1_R", "Pinky1.R"),
        ("Index2_R", "Index2.R"),
        ("Thumb2_R", "Thumb2.R"),
        ("Middle2_R", "Middle2.R"),
        ("Ring2_R", "Ring2.R"),
        ("Pinky2_R", "Pinky2.R"),
        ("Index3_R", "Index3.R"),
        ("Thumb3_R", "Thumb3.R"),
        ("Middle3_R", "Middle3.R"),
        ("Ring3_R", "Ring3.R"),
        ("Pinky3_R", "Pinky3.R"),

        ("Index1_L", "Index1.L"),
        ("Thumb1_L", "Thumb1.L"),
        ("Middle1_L", "Middle1.L"),
        ("Ring1_L", "Ring1.L"),
        ("Pinky1_L", "Pinky1.L"),
        ("Index2_L", "Index2.L"),
        ("Thumb2_L", "Thumb2.L"),
        ("Middle2_L", "Middle2.L"),
        ("Ring2_L", "Ring2.L"),
        ("Pinky2_L", "Pinky2.L"),
        ("Index3_L", "Index3.L"),
        ("Thumb3_L", "Thumb3.L"),
        ("Middle3_L", "Middle3.L"),
        ("Ring3_L", "Ring3.L"),
        ("Pinky3_L", "Pinky3.L"),

        #alternative for unity
        ("LeftIndexProximal", "Index1.L"),
        ("LeftThumbProximal", "Thumb1.L"),
        ("LeftMiddleProximal", "Middle1.L"),
        ("LeftRingProximal", "Ring1.L"),
        ("LeftLittleProximal", "Pinky1.L"),
        ("LeftIndexIntermediate", "Index2.L"),
        ("LeftThumbIntermediate", "Thumb2.L"),
        ("LeftMiddleIntermediate", "Middle2.L"),
        ("LeftRingIntermediate", "Ring2.L"),
        ("LeftLittleIntermediate", "Pinky2.L"),
        ("LeftIndexDistal", "Index3.L"),
        ("LeftThumbDistal", "Thumb3.L"),
        ("LeftMiddleDistal", "Middle3.L"),
        ("LeftRingDistal", "Ring3.L"),
        ("LeftLittleDistal", "Pinky3.L"),

        ("RightIndexProximal", "Index1.R"),
        ("RightThumbProximal", "Thumb1.R"),
        ("RightMiddleProximal", "Middle1.R"),
        ("RightRingProximal", "Ring1.R"),
        ("RightLittleProximal", "Pinky1.R"),
        ("RightIndexIntermediate", "Index2.R"),
        ("RightThumbIntermediate", "Thumb2.R"),
        ("RightMiddleIntermediate", "Middle2.R"),
        ("RightRingIntermediate", "Ring2.R"),
        ("RightLittleIntermediate", "Pinky2.R"),
        ("RightIndexDistal", "Index3.R"),
        ("RightThumbDistal", "Thumb3.R"),
        ("RightMiddleDistal", "Middle3.R"),
        ("RightRingDistal", "Ring3.R"),
        ("RightLittleDistal", "Pinky3.R"),
        ]

        for name, newname in namelist:
            # get the pose bone with name
            pb = obj.pose.bones.get(name)
            # continue if no bone of that name
            if pb is None:
                continue
            # rename
            pb.name = newname

        return {"FINISHED"}

classes = [VRC2NeosBones_bones_panel, VRC2NeosBones_op]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
