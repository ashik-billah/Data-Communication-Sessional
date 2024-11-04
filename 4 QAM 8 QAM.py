import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # Time vector for 1 second
carrier_freq = 10  # Carrier frequency (Hz)

# Mapping for 4-QAM (2 bits per symbol)
qam_4_symbols = {
    '00': (1 + 1j),     # Symbol for '00'
    '01': (-1 + 1j),    # Symbol for '01'
    '11': (-1 - 1j),    # Symbol for '11'
    '10': (1 - 1j)      # Symbol for '10'
}

# Mapping for 8-QAM (3 bits per symbol)
qam_8_symbols = {
    '000': (1 + 1j),
    '001': (1 + 0.5j),
    '010': (0.5 + 1j),
    '011': (0.5 + 0.5j),
    '100': (-1 - 1j),
    '101': (-1 - 0.5j),
    '110': (-0.5 - 1j),
    '111': (-0.5 - 0.5j)
}

# Function to map binary data to QAM symbols
def map_to_qam_symbols(bit_stream, symbol_mapping, bits_per_symbol):
    symbols = []
    for i in range(0, len(bit_stream), bits_per_symbol):
        bits = bit_stream[i:i+bits_per_symbol]
        symbols.append(symbol_mapping[bits])
    return symbols

# Sample binary data for 4-QAM and 8-QAM
bit_stream_4qam = '00011011'
bit_stream_8qam = '000001010111'

# Map bit streams to QAM symbols
symbols_4qam = map_to_qam_symbols(bit_stream_4qam, qam_4_symbols, 2)
symbols_8qam = map_to_qam_symbols(bit_stream_8qam, qam_8_symbols, 3)

# Generate QAM modulated signal for each symbol
def generate_qam_signal(symbols, carrier_freq, fs, symbol_duration=0.1):
    t_symbol = np.linspace(0, symbol_duration, int(fs * symbol_duration), endpoint=False)
    qam_signal = np.array([])
    for symbol in symbols:
        carrier = np.exp(1j * 2 * np.pi * carrier_freq * t_symbol)
        modulated_signal = symbol * carrier
        qam_signal = np.concatenate((qam_signal, modulated_signal.real))
    return qam_signal

# Generate QAM signals
qam_signal_4qam = generate_qam_signal(symbols_4qam, carrier_freq, fs)
qam_signal_8qam = generate_qam_signal(symbols_8qam, carrier_freq, fs)

# Plotting the constellation diagram for 4-QAM and 8-QAM
plt.figure(figsize=(12, 6))

# 4-QAM Constellation
plt.subplot(1, 2, 1)
for bits, point in qam_4_symbols.items():
    plt.plot(point.real, point.imag, 'bo')
    plt.text(point.real, point.imag, f' {bits}', verticalalignment='bottom', horizontalalignment='right')
plt.title("4-QAM Constellation Diagram")
plt.xlabel("In-phase")
plt.ylabel("Quadrature")
plt.grid(True)

# 8-QAM Constellation
plt.subplot(1, 2, 2)
for bits, point in qam_8_symbols.items():
    plt.plot(point.real, point.imag, 'ro')
    plt.text(point.real, point.imag, f' {bits}', verticalalignment='bottom', horizontalalignment='right')
plt.title("8-QAM Constellation Diagram")
plt.xlabel("In-phase")
plt.ylabel("Quadrature")
plt.grid(True)

plt.tight_layout()
plt.show()

# Plotting the QAM modulated signals
plt.figure(figsize=(12, 8))

# Plot 4-QAM signal
plt.subplot(2, 1, 1)
plt.plot(np.linspace(0, len(qam_signal_4qam) / fs, len(qam_signal_4qam)), qam_signal_4qam)
plt.title("4-QAM Modulated Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot 8-QAM signal
plt.subplot(2, 1, 2)
plt.plot(np.linspace(0, len(qam_signal_8qam) / fs, len(qam_signal_8qam)), qam_signal_8qam)
plt.title("8-QAM Modulated Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
