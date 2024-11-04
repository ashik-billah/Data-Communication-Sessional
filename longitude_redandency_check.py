def calculate_lrc(bit_stream, bit_length=4):
    lrc = [0] * bit_length  # Initialize the LRC byte with 0s (for 4-bit LRC)
    
    # Iterate over each bit position (0 to bit_length - 1)
    for bit_pos in range(bit_length):
        ones_count = 0
        # Count the number of 1s in the bit_pos across all bytes
        for byte in bit_stream:
            ones_count += int(byte[bit_pos])
        # Determine the LRC bit: 1 if odd number of 1s, 0 if even
        lrc[bit_pos] = '1' if ones_count % 2 != 0 else '0'
    
    return ''.join(lrc)

def check_lrc(sent_stream, received_lrc, bit_length=4):
    calculated_lrc = calculate_lrc(sent_stream, bit_length)
    return calculated_lrc == received_lrc

# User input: bit stream (each chunk should be 4 bits, separated by space)
bit_stream = input("Enter the bit stream (each chunk should be multiple of 4 bits, separated by space): ").split()

# Step 1: Calculate the LRC byte
lrc_byte = calculate_lrc(bit_stream, bit_length=4)
print(f"Calculated LRC: {lrc_byte}")

# Simulate sending the bit stream with the LRC byte appended
sent_stream = bit_stream + [lrc_byte]
print(f"Sent bit stream with LRC: {' '.join(sent_stream)}")

# Step 2: Simulate receiving the bit stream and the LRC byte
received_stream = input("Enter the received bit stream (with LRC at the end, separated by space): ").split()
received_lrc = received_stream[-1]  # The last chunk is the received LRC
received_data = received_stream[:-1]  # Data without the LRC

# Step 3: Check for errors using LRC
if check_lrc(received_data, received_lrc, bit_length=4):
    print("No errors detected.")
else:
    print("Error detected in the received data.")
