import os

def find_video_paths(dir):
    video_paths = []
    # Add more extensions as required
    video_extensions = [
    '.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm', '.m4v', 
    '.mpeg', '.mpg', '.3gp', '.3g2', '.ogv', '.rm', '.rmvb', '.vob', 
    '.ts', '.m2ts', '.mxf', '.f4v', '.f4p', '.f4a', '.f4b', '.divx', 
    '.xvid', '.asf', '.mpe', '.mpv', '.m2v', '.m1v', '.h264', '.h265', 
    '.hevc', '.yuv', '.mjpg', '.mjpeg', '.drc', '.ivf', '.ogm', '.qt'
    ]

    for root, dirs, files in os.walk(dir):
        try:
            for file in files:
                if any(file.lower().endswith(ext) for ext in video_extensions):
                    video_paths.append(os.path.join(root, file))
        except OSError as e:
            print(f"Error accessing directory: {e}")

    return video_paths


