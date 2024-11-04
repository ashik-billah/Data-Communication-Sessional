import matplotlib.pyplot as plt

def ami_encoding(data):
    """AMI (Alternate Mark Inversion) encoding."""
    encoded_signal = []
    last_polarity = -1  # Start with negative polarity for the first '1'

    for bit in data:
        if bit == '0':
            encoded_signal.append(0)  # Zero voltage for '0'
        else:
            last_polarity = -last_polarity
            encoded_signal.append(last_polarity)

    return encoded_signal


def b8zs_encoding(data):
    """B8ZS (Bipolar with 8-Zero Substitution) encoding."""
    encoded_signal = []
    zero_count = 0
    last_polarity = -1

    for bit in data:
        if bit == '0':
            zero_count += 1
            if zero_count == 8:
                zero_count = 0
                substitution_pattern = [0, 0, 0, last_polarity, -last_polarity, 0, -last_polarity, last_polarity]
                encoded_signal.extend(substitution_pattern)
            else:
                encoded_signal.append(0)
        else:
            zero_count = 0
            last_polarity = -last_polarity
            encoded_signal.append(last_polarity)

    return encoded_signal


def hdb3_encoding(data):
    """HDB3 (High-Density Bipolar 3 Zeros) encoding."""
    encoded_signal = []
    zero_count = 0
    violation_count = 0
    last_polarity = -1

    for bit in data:
        if bit == '0':
            zero_count += 1
            if zero_count == 4:
                zero_count = 0
                if violation_count % 2 == 0:
                    substitution_pattern = [last_polarity, 0, 0, -last_polarity]
                else:
                    substitution_pattern = [0, 0, 0, last_polarity]
                encoded_signal.extend(substitution_pattern)
                violation_count += 1
            else:
                encoded_signal.append(0)
        else:
            zero_count = 0
            last_polarity = -last_polarity
            encoded_signal.append(last_polarity)
            violation_count += 1

    return encoded_signal


def plot_all_encodings(data, ami_signal, b8zs_signal, hdb3_signal):
    """Plot all encoded signals on a single page using subplots."""
    fig, axs = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    # Plot AMI encoding
    axs[0].step(range(len(ami_signal)), ami_signal, where='mid', color='b', linewidth=2)
    axs[0].set_title("AMI Encoding")
    axs[0].set_ylim(-2, 2)
    axs[0].grid(True)

    # Plot B8ZS encoding
    axs[1].step(range(len(b8zs_signal)), b8zs_signal, where='mid', color='g', linewidth=2)
    axs[1].set_title("B8ZS Encoding")
    axs[1].set_ylim(-2, 2)
    axs[1].grid(True)

    # Plot HDB3 encoding
    axs[2].step(range(len(hdb3_signal)), hdb3_signal, where='mid', color='r', linewidth=2)
    axs[2].set_title("HDB3 Encoding")
    axs[2].set_ylim(-2, 2)
    axs[2].grid(True)

    # General plot settings
    fig.suptitle(f"Bipolar Line Encoding (Input Data: {data})", fontsize=14)
    plt.xlabel('Time')
    plt.tight_layout()
    plt.show()


# User input for binary data
data = input("Enter binary data: ")

# Perform each encoding
ami_signal = ami_encoding(data)
b8zs_signal = b8zs_encoding(data)
hdb3_signal = hdb3_encoding(data)

# Plot all encodings
plot_all_encodings(data, ami_signal, b8zs_signal, hdb3_signal)
