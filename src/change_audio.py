from read_audio import read_audio
from phase_vocoder import phase_vocoder
from write_audio import write_audio
from audio_visualization import audio_visualization

def change_audio(input_file, output_file, stretch_factor):
    sample_rate, signal = read_audio(input_file)
    stretched_signal = phase_vocoder(signal, stretch_factor) # Apply phase vocoder
    write_audio(output_file, sample_rate, stretched_signal)
    print(f"The audio recording of '{input_file}' has been successfully changed by a factor of '{stretch_factor}'. New file name: '{output_file}'")

    audio_visualization(signal, stretched_signal, sample_rate, output_file) # Creating .png files that show the frequency difference between the input and output files
