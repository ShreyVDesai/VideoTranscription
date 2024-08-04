import subprocess
import os

def convert_video_to_audio(video_file_path, output_format='mp3'):
    # Get the base name of the video file without extension
    base_name = os.path.splitext(video_file_path)[0]
    # Define the output audio file path
    audio_file_path = f"{base_name}.{output_format}"

    # ffmpeg command to extract and convert audio
    command = [
        'ffmpeg',
        '-i', video_file_path,         # Input file
        '-vn',                         # No video
        '-acodec', 'libmp3lame',       # Convert to mp3 using the libmp3lame codec
        '-q:a', '2',                   # Set quality level (0=best, 9=worst)
        audio_file_path                # Output file
    ]

    try:
        # Run the command
        subprocess.run(command, check=True)
        print(f"Audio extracted and saved as {audio_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

    return audio_file_path

# # Example usage
# convert_video_to_audio('D:\\Downloads\\IntelliJ-setup.mp4', 'mp3')
