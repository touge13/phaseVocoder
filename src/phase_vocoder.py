from numpy.fft import fft, ifft
from numpy import zeros, hanning, sqrt, angle, mod, exp, pi, real

def phase_vocoder(signal, stretch_factor):
    # Parameters
    window_size = 2048
    hop_size = window_size // 4
        
    # Initialize output signal
    output_length = int(len(signal) / stretch_factor)
    output_signal = zeros(output_length)
    
    phase_acc = zeros(window_size) # Initialize phase accumulator
    
    # Main phase vocoder loop
    for i in range(0, len(signal) - window_size, hop_size):
        hop_out = round(hop_size / stretch_factor)
        
        # Window the input signal
        window = hanning(window_size)
        windowed_signal = signal[i:i + window_size] * window / sqrt((window_size / hop_out) / 2)

        spectrum = fft(windowed_signal)                                                 # Perform FFT on windowed signal
        phase_diff = angle(spectrum) - phase_acc                                        # Calculate phase difference
        phase_diff_stretched = phase_diff * stretch_factor                              # Stretch/compress phase difference
        phase_diff_wrapped = mod(phase_diff_stretched + pi, 2 * pi) - pi                # Wrap phase difference
        spectrum_stretched = abs(spectrum) * exp(1j * (phase_acc + phase_diff_wrapped)) # Calculate stretched spectrum
        windowed_stretched = real(ifft(spectrum_stretched))                             # Inverse FFT to get stretched signal
        
        # Overlap-add to reconstruct signal
        output_index = int(i / stretch_factor)
        if output_index + window_size <= len(output_signal):
            output_signal[output_index:output_index + window_size] += windowed_stretched * window
        
        # Update phase accumulator
        phase_acc += phase_diff    
        
    return output_signal
