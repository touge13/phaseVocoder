import matplotlib.pyplot as plt
from numpy import max as np_max, abs as np_abs, arange

def audio_visualization(signal, stretched_signal, sample_rate, output_file):
    # Determine the y-axis limit for the plot
    y_axis_limit = max(np_max(np_abs(signal)), np_max(np_abs(stretched_signal))) + 10000
    
    # Determine the maximum time
    max_length = max(len(signal), len(stretched_signal))
    max_time = max_length / sample_rate

    # Plot input and output audio signals
    plt.figure(figsize = (10, 6))
    plt.subplot(2, 1, 1)
    plt.title('Input audio')
    plt.plot(arange(len(signal)) / sample_rate, signal, color='blue')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (dB)')
    plt.ylim(-y_axis_limit, y_axis_limit)
    plt.xlim(0, max_time)

    plt.subplot(2, 1, 2)
    plt.title('Output audio')
    plt.plot(arange(len(stretched_signal)) / sample_rate, stretched_signal, color='red')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (dB)')
    plt.ylim(-y_axis_limit, y_axis_limit)
    plt.xlim(0, max_time)

    plt.tight_layout()
    plt.savefig(f'{output_file.replace('.wav', '')}.png')
