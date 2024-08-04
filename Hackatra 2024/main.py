# import video_sensing
# import audio_file_extractor
# import audio_transcription
# import time
# import os

# dir_path = input("Enter the directory path containing the videos: ")
# videos = video_sensing.find_video_paths(dir_path)
# text = ''
# for video in videos:
#     path = audio_file_extractor.convert_video_to_audio(video)
#     text += '\n' + 'Transcript for video at path '+ path + '\n' + audio_transcription.transcribe_audio(path)
#     os.remove(path)
#     time.sleep(5)

# file_path = input('Enter path to save the transcription to: ')

# with open(file_path, 'w') as file:
#     file.write(text)

# main.py
import video_sensing
import audio_file_extractor
import audio_transcription
import concurrent.futures
import os
import time

def process_video(video):
    try:
        # Convert video to audio
        audio_path = audio_file_extractor.convert_video_to_audio(video)
        # Transcribe audio to text
        transcript = audio_transcription.transcribe_audio(audio_path)
        # Remove audio file after transcription
        os.remove(audio_path)
        # Return transcript with video path for reference
        return f"Transcript for video at path {video}:\n{transcript}"
    except Exception as e:
        return f"An error occurred processing video {video}: {e}"

def main():
    dir_path = input("Enter the directory path containing the videos: ")
    if not os.path.exists(dir_path):
        print("Directory does not exist.")
        return

    # Find all video files in the directory
    videos = video_sensing.find_video_paths(dir_path)

    # List to store transcripts
    transcripts = []

    # Use ThreadPoolExecutor for parallel processing
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Process each video file in parallel
        results = executor.map(process_video, videos)

    # Collect results
    for result in results:
        transcripts.append(result)
        time.sleep(1)  # Optional: Add a small delay between tasks if necessary

    # Write all transcripts to a file
    file_path = input('Enter path to save the transcription to: ')
    try:
        with open(file_path, 'w') as file:
            file.write('\n'.join(transcripts))
        print(f"Transcriptions saved to {file_path}")
    except IOError as e:
        print(f"Failed to write transcriptions to file: {e}")

if __name__ == "__main__":
    main()
