from numpy import int16
from scipy.io import wavfile

def write_audio(output_file, sample_rate, signal):
    wavfile.write(output_file, sample_rate, signal.astype(int16)) # Convert to int16 data type for compatibility with the .wav format
