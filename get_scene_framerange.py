import bpy


def get_framerange(scenepath):
    start_frame =  bpy.context.scene.frame_start
    end_frame =  bpy.context.scene.frame_end
    return (start_frame, end_frame)
    

if __name__ == "__main__":
    
    import sys       # to get command line args
    import argparse  # to parse options for us and print a nice help message
    
    if len(sys.argv) != 2:
        print("Incorrect arguments provided. Use blend scene path only")
        sys.exit(1)
    
    # Run the function to extract frame range
    fr = get_framerange(sys.argv[1])
    print(fr)
