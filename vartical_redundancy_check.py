def calculate_parity(bit_stream):
    parity_bits = []
    for byte in bit_stream:
        # Count the number of 1s in the byte
        count_ones = byte.count('1')
        # Even parity: if the number of 1s is odd, parity bit is 1; otherwise, it's 0
        parity_bit = '1' if count_ones % 2 != 0 else '0'
        parity_bits.append(parity_bit)
    return parity_bits

def append_parity_bits(bit_stream, parity_bits):
    return [bit + parity for bit, parity in zip(bit_stream, parity_bits)]

def check_for_errors(sent_stream):
    error_indices = []
    for i, byte in enumerate(sent_stream):
        data_bits = byte[:-1]  # All bits except the last one (parity bit)
        parity_bit = byte[-1]  # The last bit is the parity bit
        # Check parity
        count_ones = data_bits.count('1')
        calculated_parity = '1' if count_ones % 2 != 0 else '0'
        if calculated_parity != parity_bit:
            error_indices.append(i)
    return error_indices

# User input: bit stream (each byte is a string of 8 bits)
bit_stream = input("Enter the bit stream : ").split()

# Step 1: Calculate parity bits
parity_bits = calculate_parity(bit_stream)

# Step 2: Append parity bits to the bit stream
sent_stream = append_parity_bits(bit_stream, parity_bits)
print(f"Sent bit stream with parity bits: {' '.join(sent_stream)}")

# Simulate receiving the same bit stream (with or without errors)
received_stream = input("Enter the received bit stream (each byte should include the parity bit, separated by space): ").split()

# Step 3: Check for errors in the received stream
error_indices = check_for_errors(received_stream)

if error_indices:
    print(f"Error detected in the received message")
else:
    print("No errors detected.")
