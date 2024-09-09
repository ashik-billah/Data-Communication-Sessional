import numpy as np
from matplotlib import pyplot as plt

# Taking user input for the binary data
data_input = input("Enter a binary sequence (e.g., 010110): ")
data = np.array([int(bit) for bit in data_input])

time = np.arange(len(data))

# Unipolar Encoding
plt.subplot(2, 3, 1)
plt.step(time, data, where='post')
plt.title('Unipolar')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0, 2, data)
plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.xticks(time)

# NRZ-L Encoding
signal = np.zeros(len(data), dtype=int)
for i in range(len(data)):
    signal[i] = 1 if data[i] == 1 else -1

plt.subplot(2, 3, 2)
plt.step(time, signal, where='post')
plt.title('NRZ-L')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.text(0, 2, data)
plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.xticks(time)

# NRZ-I Encoding
signal = np.zeros(len(data), dtype=int)
flg = True
for i in range(len(data)):
    if data[i] == 1:
        flg = not flg
    signal[i] = 1 if flg else -1

plt.subplot(2, 3, 3)
plt.step(time, signal, where='post')
plt.title('NRZ-I')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0, 2, data)
plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.xticks(time)

# RZ Encoding
time_rz = np.linspace(0, len(data), len(data) * 2)
signal_rz = np.zeros(2 * len(data), dtype=int)
for i in range(0, 2 * len(data), 2):
    signal_rz[i] = 1 if data[i // 2] == 1 else -1
    signal_rz[i + 1] = 0

plt.subplot(2, 3, 4)
plt.step(time_rz, signal_rz, where='post')
plt.title('RZ')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0, 2, data)
plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.xticks(np.arange(len(data)))

# Manchester Encoding
time_org = np.arange(len(data))
signal_manchester = np.zeros(len(data) * 2, dtype=int)
for i in range(0, len(data) * 2, 2):
    if data[i // 2] == 0:
        signal_manchester[i] = 1
        signal_manchester[i + 1] = -1
    else:
        signal_manchester[i] = -1
        signal_manchester[i + 1] = 1

plt.subplot(2, 3, 5)
plt.step(np.arange(len(signal_manchester)), signal_manchester, where='post')
plt.title('Manchester')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0, 2, data)
plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.xticks(time_org * 2, time_org)

# Differential Manchester Encoding
signal_differential_manchester = np.zeros(len(data) * 2, dtype=int)
start = False
for i in range(0, len(data) * 2, 2):
    if start:
        if data[i // 2] == 0:
            signal_differential_manchester[i] = -1 * signal_differential_manchester[i - 1]
            signal_differential_manchester[i + 1] = signal_differential_manchester[i - 1]
        else:
            signal_differential_manchester[i] = signal_differential_manchester[i - 1]
            signal_differential_manchester[i + 1] = -1 * signal_differential_manchester[i - 1]
    else:
        start = True
        if data[i // 2] == 0:
            signal_differential_manchester[i] = -1
            signal_differential_manchester[i + 1] = 1
        else:
            signal_differential_manchester[i] = 1
            signal_differential_manchester[i + 1] = -1

plt.subplot(2, 3, 6)
plt.step(np.arange(len(signal_differential_manchester)), signal_differential_manchester, where='post')
plt.title('Differential Manchester')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0, 2, data)
plt.grid(True)
plt.yticks([-2, -1, 0, 1, 2, 3])
plt.xticks(time_org * 2, time_org)

plt.subplots_adjust(hspace=1)
plt.show()
