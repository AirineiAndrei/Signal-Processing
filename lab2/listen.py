import sys
import sounddevice as sd
from scipy.io import wavfile

def play_audio(file_name):
    fs, data = wavfile.read(file_name)
    
    sd.play(data, fs)
    sd.wait()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python play_audio.py <path_to_audio_file.wav>")
        sys.exit(1)
    play_audio(sys.argv[1])
