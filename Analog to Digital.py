import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Original Sampling frequency (Hz)
t = np.linspace(0, 1, fs)  # Time vector from 0 to 1 second
f = 5  # Frequency of the sine wave (Hz)
amplitude = 1  # Amplitude of the sine wave

# User-defined parameters
sample_rate = 100  # User-defined sampling rate (number of samples per second)
num_levels = 16  # Number of quantization levels for PCM

# Generate the analog signal (sine wave)
analog_signal = amplitude * np.sin(2 * np.pi * f * t)

# Sampling the signal
sampled_signal = analog_signal[::fs // sample_rate]
t_sampled = t[::fs // sample_rate]  # Adjust time vector for sampled signal

# PAM Modulation (amplitude values are the sampled values)
pam_signal = np.zeros_like(analog_signal)
for i, sample in enumerate(sampled_signal):
    pam_signal[i * (fs // sample_rate)] = sample

# Quantization for PCM
max_val = np.max(sampled_signal)
min_val = np.min(sampled_signal)
quantized_signal = np.round((sampled_signal - min_val) / (max_val - min_val) * (num_levels - 1))

# PCM Encoding (convert quantized values to binary)
pcm_encoded = [format(int(sample), '04b') for sample in quantized_signal]  # 4 bits for each quantization level

# Signal Reconstruction (for visualization)
reconstructed_signal = np.zeros_like(analog_signal)
for i, sample in enumerate(quantized_signal):
    reconstructed_signal[i * (fs // sample_rate)] = (sample / (num_levels - 1)) * (max_val - min_val) + min_val

# Plotting the results
plt.figure(figsize=(12, 10))

# Plot analog signal
plt.subplot(5, 1, 1)
plt.plot(t, analog_signal, label='Analog Signal', color='blue')
plt.title('Analog Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# Plot sampled signal
plt.subplot(5, 1, 2)
plt.stem(t_sampled, sampled_signal, label='Sampled Signal', linefmt='orange', markerfmt='ro', basefmt=' ')
plt.title('Sampled Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# Plot PAM signal
plt.subplot(5, 1, 3)
plt.plot(t, pam_signal, label='PAM Signal', color='green')
plt.title('Pulse Amplitude Modulation (PAM) Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# Plot quantized signal (for PCM)
plt.subplot(5, 1, 4)
plt.stem(t_sampled, quantized_signal, label='Quantized Signal (PCM)', linefmt='purple', markerfmt='go', basefmt=' ')
plt.title('Quantized Signal (PCM)')
plt.xlabel('Time (s)')
plt.ylabel('Quantized Level')
plt.grid()
plt.legend()

# Plot reconstructed signal
plt.subplot(5, 1, 5)
plt.plot(t, reconstructed_signal, label='Reconstructed Signal', color='brown', alpha=0.6)
plt.title('Reconstructed Signal from Quantized Levels')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# Display PCM Encoded Output
print("PCM Encoded Values:")
print(pcm_encoded)
