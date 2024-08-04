
import whisper
import os

def transcribe_audio(audio_path, model_size="base"):
    """
    Transcribe an audio file to text using the Whisper model.

    Parameters:
    - audio_path (str): The path to the audio file to transcribe.
    - model_size (str): The size of the Whisper model to use. Options include 'tiny', 'base', 'small', 'medium', 'large-v1', 'large-v2', 'large-v3'.

    Returns:
    - str: The transcribed text from the audio.
    """
    try:
        # Load the Whisper model (will use cached version if available)
        model = whisper.load_model(model_size)
        
        # Transcribe the audio file
        result = model.transcribe(audio_path)
        
        # Return the transcribed text
        return result['text']
    
    except Exception as e:
        return f"An error occurred during transcription: {e}"

# Example usage:
# audio_file_path = "path/to/your/audio/file.mp3"
# transcription = transcribe_audio(audio_file_path, model_size="base")
# print(transcription)
