import sys
from change_audio import change_audio

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python main.py <input.wav> <output.wav> <time_stretch_ratio>")
        sys.exit(1)

    # Assign input arguments to variables
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    stretch_factor = float(sys.argv[3])

    change_audio(input_file, output_file, stretch_factor)
