# VideoTranscription
Local Directory video transcription using ffmpeg and OpenAI Whisper
## Quick Start Guide
### Project Dependencies:
ffmpeg 7.0.1, Python 3.11.0, Python Modules - OpenAI's Whisper, time, os
### Steps to run the program:
1. In a secure environment, install the dependencies.
2. Using a command line tool, navigate to the directory containing the main.py file.
3. Run the command `python main.py`
4. Follow the command line instructions to input the directory paths as well as the txt file path where the transcripts should be stored.
## Algorithm Outline:
1. Traverse Local Directory: Implements a script to recursively search and identify video files within a specified directory structure.
2. Convert Videos to Audio: Utilizes ffmpeg to extract audio tracks from identified video files, ensuring compatibility and quality.
3. Transcription Using Whisper: Integrates Whisper for local audio transcription, leveraging its accuracy and efficiency in converting speech to text.
4. Cooling Time Implementation: Incorporate intervals between transcription tasks to prevent system overheating, enhancing long-term stability.
5. Generates Combined Transcript: Merges individual transcriptions into a cohesive transcript document, ensuring clarity and coherence.
## Features:
1. Converts video files to MP3 audio format
2. Transcribes audio to text using OpenAI's Whisper model
3. Processes videos in batches with multi-threading
4. Implements cooling periods for system stability

