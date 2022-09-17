# VRC2Neos Blender Plugin

A tool designed to easily convert VRChat/Unity-humanoid Avatar armature bone names to NeoVR ones with a single button.

#### Download here: [VRC2Neos Blender Plugin](https://github.com/hazre/VRC2NeosBones-blender-plugin/archive/main.zip)

## Features
 - Rename bones (VRChat/Unity-humanoid => NeosVR)

## Requirements
 - Blender **2.80** or above

## Installation
 - Download the plugin: **[VRC2Neos Blender Plugin](https://github.com/hazre/VRC2NeosBones-blender-plugin/archive/main.zip)**
   - **Important: Do NOT extract the downloaded zip! You will need the zip file during installation!**
 - Install the addon in blender like so:
   - *This shows Blender 3.30.*

![](https://i.imgur.com/4jNSSsp.gif)

 - Check your 3d view and there should be a new menu item called **VRC2Neos**

![](https://i.imgur.com/UbtLwHd.gif)

## Supported Bone Names

|Name                   |Alternative|Description                           |
|-----------------------|-----------|--------------------------------------|
|Hips                   |           |This is the Hips bone.                |
|LeftUpperLeg           |UpperLeg_L |This is the Left Upper Leg bone.      |
|RightUpperLeg          |UpperLeg_R |This is the Right Upper Leg bone.     |
|LeftLowerLeg           |LowerLeg_L |This is the Left Knee bone.           |
|RightLowerLeg          |LowerLeg_R |This is the Right Knee bone.          |
|LeftFoot               |Foot_L     |This is the Left Ankle bone.          |
|RightFoot              |Foot_R     |This is the Right Ankle bone.         |
|Spine                  |           |This is the first Spine bone.         |
|Chest                  |           |This is the Chest bone.               |
|UpperChest             |           |This is the Upper Chest bone.         |
|Neck                   |           |This is the Neck bone.                |
|Head                   |           |This is the Head bone.                |
|LeftShoulder           |Shoulder_L |This is the Left Shoulder bone.       |
|RightShoulder          |Shoulder_R |This is the Right Shoulder bone.      |
|LeftUpperArm           |UpperArm_L |This is the Left Upper Arm bone.      |
|RightUpperArm          |UpperArm_R |This is the Right Upper Arm bone.     |
|LeftLowerArm           |LowerArm_L |This is the Left Elbow bone.          |
|RightLowerArm          |LowerArm_R |This is the Right Elbow bone.         |
|LeftHand               |Hand_R     |This is the Left Wrist bone.          |
|RightHand              |Hand_L     |This is the Right Wrist bone.         |
|LeftToes               |Toe_L      |This is the Left Toes bone.           |
|RightToes              |Toe_R      |This is the Right Toes bone.          |
|LeftEye                |           |This is the Left Eye bone.            |
|RightEye               |           |This is the Right Eye bone.           |
|Jaw                    |           |This is the Jaw bone.                 |
|LeftThumbProximal      |Thumb1_L   |This is the left thumb 1st phalange.  |
|LeftThumbIntermediate  |Thumb2_L   |This is the left thumb 2nd phalange.  |
|LeftThumbDistal        |Thumb3_L   |This is the left thumb 3rd phalange.  |
|LeftIndexProximal      |Index1_R   |This is the left index 1st phalange.  |
|LeftIndexIntermediate  |Index2_R   |This is the left index 2nd phalange.  |
|LeftIndexDistal        |Index3_R   |This is the left index 3rd phalange.  |
|LeftMiddleProximal     |Middle1_L  |This is the left middle 1st phalange. |
|LeftMiddleIntermediate |Middle2_L  |This is the left middle 2nd phalange. |
|LeftMiddleDistal       |Middle3_L  |This is the left middle 3rd phalange. |
|LeftRingProximal       |Ring1_L    |This is the left ring 1st phalange.   |
|LeftRingIntermediate   |Ring2_L    |This is the left ring 2nd phalange.   |
|LeftRingDistal         |Ring3_L    |This is the left ring 3rd phalange.   |
|LeftLittleProximal     |Pinky1_L   |This is the left little 1st phalange. |
|LeftLittleIntermediate |Pinky2_L   |This is the left little 2nd phalange. |
|LeftLittleDistal       |Pinky3_L   |This is the left little 3rd phalange. |
|RightThumbProximal     |Thumb1_R   |This is the right thumb 1st phalange. |
|RightThumbIntermediate |Thumb2_R   |This is the right thumb 2nd phalange. |
|RightThumbDistal       |Thumb3_R   |This is the right thumb 3rd phalange. |
|RightIndexProximal     |Index1_R   |This is the right index 1st phalange. |
|RightIndexIntermediate |Index2_R   |This is the right index 2nd phalange. |
|RightIndexDistal       |Index3_R   |This is the right index 3rd phalange. |
|RightMiddleProximal    |Middle1_R  |This is the right middle 1st phalange.|
|RightMiddleIntermediate|Middle2_R  |This is the right middle 2nd phalange.|
|RightMiddleDistal      |Middle3_R  |This is the right middle 3rd phalange.|
|RightRingProximal      |Ring1_R    |This is the right ring 1st phalange.  |
|RightRingIntermediate  |Ring2_R    |This is the right ring 2nd phalange.  |
|RightRingDistal        |Ring3_R    |This is the right ring 3rd phalange.  |
|RightLittleProximal    |Pinky1_R   |This is the right little 1st phalange.|
|RightLittleIntermediate|Pinky2_R   |This is the right little 2nd phalange.|
|RightLittleDistal      |Pinky3_R   |This is the right little 3rd phalange.|

## Documents
  - [Gamepretty - Source Filmmaker: How to Rename Blender Bone Easily](https://www.gamepretty.com/source-filmmaker-how-to-rename-blender-bone-easily-working-2022/)
  - [Unity - HumanBodyBones](https://docs.unity3d.com/2019.4/Documentation/ScriptReference/HumanBodyBones.html)
  - [Neos - Humanoid Rig Requirements for IK](https://wiki.neos.com/Humanoid_Rig_Requirements_for_IK)
  - [Github - Cats Blender Plugin Readme (used as template)](https://github.com/absolute-quantum/cats-blender-plugin/blob/master/README.md)