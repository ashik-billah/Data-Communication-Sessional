def calculate_parity(bits, positions):
    """Calculate parity for given bits at specified positions."""
    parity = 0
    for pos in positions:
        parity ^= bits[pos - 1]
    return parity


def hamming_encode(data):
    """Encode data using Hamming code with reverse indexing for data bit placement."""
    # Convert data to a list of integers
    d = [int(bit) for bit in data][::-1]  # Reverse data bits
    m = len(d)  # number of data bits

    # Determine the number of parity bits needed
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1

    # Initialize the list with space for data and parity bits
    bits = [0] * (m + r)

    # Position data bits from the right, skipping positions that are powers of 2
    j = 0  # Data bit index
    for i in range(1, len(bits) + 1):
        if i & (i - 1) == 0:  # Power of 2, reserve for parity bit
            continue
        bits[i - 1] = d[j]
        j += 1

    # Calculate and position parity bits
    for i in range(r):
        parity_pos = 2 ** i
        bits[parity_pos - 1] = calculate_parity(bits, [j + 1 for j in range(len(bits)) if (j + 1) & parity_pos])

    return bits[::-1]  # Reverse bits to match the original order


def hamming_decode(received):
    """Decode data received and correct single-bit error if exists, with reverse indexing."""
    # Convert received bits to a list of integers and reverse them for correct indexing
    received_bits = [int(bit) for bit in received][::-1]
    n = len(received_bits)

    # Determine number of parity bits (assume n = m + r)
    r = 0
    while (2 ** r) < (n + 1):
        r += 1

    # Calculate parity bits to detect errors
    error_pos = 0
    for i in range(r):
        parity_pos = 2 ** i
        expected_parity = calculate_parity(received_bits, [j + 1 for j in range(n) if (j + 1) & parity_pos])
        if expected_parity != 0:
            error_pos += parity_pos

    if error_pos == 0:
        print("No error detected.")
    else:
        print(f"Error detected at position {error_pos}. Correcting it.")
        received_bits[error_pos - 1] ^= 1  # Correct the bit
        print("Corrected Code with Parity Bits:", ''.join(map(str, received_bits[::-1])))  # Show corrected data

    # Extract the original data bits
    decoded_data = [received_bits[i] for i in range(n) if (i + 1) & (i) != 0]  # Skip parity positions
    return decoded_data[::-1]  # Reverse decoded data back to original order


# Main program
data = input("Enter binary data (e.g., 1001101): ")
if not all(bit in '01' for bit in data):
    print("Invalid input. Please enter binary data (0s and 1s only).")
else:
    encoded = hamming_encode(data)
    print("Encoded Hamming Code:", ''.join(map(str, encoded)))

    # Simulate received data with a possible error
    received = input("Enter the received code (with or without error): ")
    if not all(bit in '01' for bit in received):
        print("Invalid input. Please enter binary data (0s and 1s only).")
    else:
        decoded_data = hamming_decode(received)
        print("Decoded Data:", ''.join(map(str, decoded_data)))