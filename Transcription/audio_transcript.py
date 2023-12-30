import speech_recognition as sr
import os
folder_path = '/Users/dontizi/Documents/Rewind/Transcription/transcript_txt'  # Replace this with your desired folder path

# Initialize recognizer
r = sr.Recognizer()

# Load the audio file
audio_file_path = '/Users/dontizi/Documents/Rewind/Audio/recordedFile.wav'  # Replace this with your audio file path
with sr.AudioFile(audio_file_path) as source:
    audio = r.record(source)  # Read the entire audio file

# Transcribe the audio to text
try:
    print("Transcribing audio...")
    text = r.recognize_google(audio)  # Using Google Speech Recognition
    print("Transcription: " + text)
    file_path = os.path.join(folder_path, 'transcription.txt')
    # Check if folder exists and create it if not
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


    # Saving the transcribed text into a .txt file
    with open(file_path, 'w') as f:
        f.write(text)
        print("Transcription saved to transcription.txt")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
# Check if folder exists and create it if not



