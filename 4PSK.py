import numpy as np
import matplotlib.pyplot as plt

# Function to map binary pairs to phase shifts in radians
def bits_to_phase(binary_stream):
    phase_mapping = {
        '00': 0,            # 0 degrees
        '01': np.pi / 2,    # 90 degrees
        '11': np.pi,        # 180 degrees
        '10': 3 * np.pi / 2 # 270 degrees
    }
    
    phases = []
    # Ensure the binary stream length is even by padding with '0' if necessary
    if len(binary_stream) % 2 != 0:
        binary_stream = '0' + binary_stream
    
    for i in range(0, len(binary_stream), 2):
        bits = binary_stream[i:i+2]
        phases.append(phase_mapping[bits])
    
    return phases

# Function to generate the 4-PSK modulated signal
def generate_4psk_wave(binary_stream, carrier_freq=2, sample_rate=100, duration_per_symbol=1):
    phases = bits_to_phase(binary_stream)
    
    t = np.arange(0, len(phases) * duration_per_symbol, 1/sample_rate)
    modulated_wave = np.zeros_like(t)
    
    for i, phase in enumerate(phases):
        modulated_wave[i*sample_rate:(i+1)*sample_rate] = np.cos(2 * np.pi * carrier_freq * t[i*sample_rate:(i+1)*sample_rate] + phase)
    
    return t, modulated_wave

# Function to handle user input
def user_input():
    # Take binary stream input
    binary_stream = input("Enter a binary stream (e.g., 11001001): ")
    
    # Ensure that the input is only 0s and 1s
    while not all(bit in '01' for bit in binary_stream):
        print("Invalid input. Please enter a binary stream of 0s and 1s.")
        binary_stream = input("Enter a binary stream (e.g., 11001001): ")
    
    # Take carrier frequency input
    try:
        carrier_freq = float(input("Enter the carrier frequency (default is 2 Hz): ") or 2)
    except ValueError:
        print("Invalid input. Using default carrier frequency of 2 Hz.")
        carrier_freq = 2
    
    # Take sample rate input
    try:
        sample_rate = int(input("Enter the sample rate (default is 100): ") or 100)
    except ValueError:
        print("Invalid input. Using default sample rate of 100.")
        sample_rate = 100
    
    # Take symbol duration input
    try:
        duration_per_symbol = float(input("Enter the duration per symbol (default is 1 second): ") or 1)
    except ValueError:
        print("Invalid input. Using default duration per symbol of 1 second.")
        duration_per_symbol = 1
    
    return binary_stream, carrier_freq, sample_rate, duration_per_symbol

# Main function
def main():
    # Get user input
    binary_stream, carrier_freq, sample_rate, duration_per_symbol = user_input()

    # Generate the 4-PSK modulated wave
    t, modulated_wave = generate_4psk_wave(binary_stream, carrier_freq, sample_rate, duration_per_symbol)

    # Plot the wave
    plt.figure(figsize=(10, 6))
    plt.plot(t, modulated_wave)
    plt.title(f'4-PSK Modulated Wave\nBinary Stream: {binary_stream}, Carrier Freq: {carrier_freq} Hz')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

# Run the program
if __name__ == "__main__":
    main()
