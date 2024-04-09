from scipy.io import wavfile

def read_audio(input_file):
    sample_rate, signal = wavfile.read(input_file)
    
    # Check if stereo and convert to mono
    if len(signal.shape) > 1:
        signal = signal.mean(axis = 1) 
           
    return sample_rate, signal