import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
fs = 1000  # Sampling frequency (samples per second)
t = np.linspace(0, 1, fs)  # Time vector (1 second)
carrier_freq = 100  # Carrier frequency (Hz)
modulating_freq = 5  # Modulating signal frequency (Hz)
modulation_index_am = 0.5  # Modulation index for AM
modulation_index_fm = 5  # Modulation index for FM
modulation_index_pm = np.pi / 2  # Modulation index for PM

# Modulating signal (sine wave)
modulating_signal = np.sin(2 * np.pi * modulating_freq * t)

# Carrier signal
carrier_signal = np.cos(2 * np.pi * carrier_freq * t)

# Amplitude Modulation (AM)
am_signal = (1 + modulation_index_am * modulating_signal) * carrier_signal

# Frequency Modulation (FM)
fm_signal = np.cos(2 * np.pi * carrier_freq * t + modulation_index_fm * np.sin(2 * np.pi * modulating_freq * t))

# Phase Modulation (PM)
pm_signal = np.cos(2 * np.pi * carrier_freq * t + modulation_index_pm * modulating_signal)

# Plotting the signals
plt.figure(figsize=(10, 10))

# Plot Modulating signal
plt.subplot(5, 1, 1)
plt.plot(t, modulating_signal, label="Modulating Signal", color='b')
plt.title('Modulating Signal (Message Signal)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot Carrier signal
plt.subplot(5, 1, 2)
plt.plot(t, carrier_signal, label="Carrier Signal", color='c')
plt.title('Carrier Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot AM signal
plt.subplot(5, 1, 3)
plt.plot(t, am_signal, label="AM Signal", color='m')
plt.title('Amplitude Modulation (AM)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot FM signal
plt.subplot(5, 1, 4)
plt.plot(t, fm_signal, label="FM Signal", color='r')
plt.title('Frequency Modulation (FM)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot PM signal
plt.subplot(5, 1, 5)
plt.plot(t, pm_signal, label="PM Signal", color='g')
plt.title('Phase Modulation (PM)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()
