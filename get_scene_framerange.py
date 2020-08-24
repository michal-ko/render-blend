import bpy


def get_framerange(scenepath):
    bpy.ops.wm.open_mainfile(filepath=scenepath)  # opens blender scene
    start_frame = bpy.context.scene.frame_start
    end_frame = bpy.context.scene.frame_end
    return {"start_frame": start_frame, "end_frame": end_frame}


if __name__ == "__main__":

    import sys

    if len(sys.argv) != 5:
        print("Incorrect arguments provided!\n"
              "Example: blender --background monkey_test.blend --python ./get_scene_framerange.py")
        sys.exit(1)

    abs_file_path = bpy.data.filepath
    print(f"Checking file: {abs_file_path}")

    # Run the function to extract frame range
    fr = get_framerange(abs_file_path)
    print(fr)
