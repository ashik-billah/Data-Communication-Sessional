import numpy as np
import matplotlib.pyplot as plt

# Function to generate binary input
data_input = input("Enter a binary sequence (e.g., 101010): ")
binary_signal = np.array([int(bit) for bit in data_input])

# Time axis
sampling_rate = 1000  # samples per second
duration = 1  # duration of each bit in seconds
time = np.linspace(0, len(binary_signal), len(binary_signal) * sampling_rate)

# Carrier Frequencies for Modulations
carrier_freq1 = 5  # in Hz for ASK and PSK
carrier_freq2 = 10  # in Hz for FSK

# ASK Modulation
ask_signal = np.array([])
for bit in binary_signal:
    carrier = (1 if bit == 1 else 0.5) * np.sin(2 * np.pi * carrier_freq1 * time[:sampling_rate])
    ask_signal = np.concatenate((ask_signal, carrier))

# FSK Modulation
fsk_signal = np.array([])
for bit in binary_signal:
    carrier = np.sin(2 * np.pi * (carrier_freq2 if bit == 1 else carrier_freq1) * time[:sampling_rate])
    fsk_signal = np.concatenate((fsk_signal, carrier))

# PSK Modulation
psk_signal = np.array([])
phase = 0
for bit in binary_signal:
    if bit == 1:
        phase = np.pi if phase == 0 else 0
    carrier = np.sin(2 * np.pi * carrier_freq1 * time[:sampling_rate] + phase)
    psk_signal = np.concatenate((psk_signal, carrier))

# Plotting
plt.figure(figsize=(12, 8))

# Plot Binary Signal
plt.subplot(2, 2, 1)
plt.step(np.arange(len(binary_signal)), binary_signal, where='post', label='Binary Data')
plt.title('Binary Signal')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot ASK Modulation
plt.subplot(2, 2, 2)
plt.plot(ask_signal, label='ASK Signal')
plt.title('ASK Modulation')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot FSK Modulation
plt.subplot(2, 2, 3)
plt.plot(fsk_signal, label='FSK Signal')
plt.title('FSK Modulation')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot PSK Modulation
plt.subplot(2, 2, 4)
plt.plot(psk_signal, label='PSK Signal')
plt.title('PSK Modulation')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
