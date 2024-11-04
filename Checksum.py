def calculate_checksum(bit_stream):
    total_sum = 0
    
    # Convert each byte (8-bit string) to an integer and sum them
    for byte in bit_stream:
        total_sum += int(byte, 2)  # Convert binary string to integer
    
    # Take only the lower 8 bits of the total sum (1-byte checksum)
    checksum = total_sum % 256  # To simulate an 8-bit checksum
    
    # Return the complement of the sum (as checksum is usually the complement)
    return format((~checksum) & 0xFF, '08b')  # Return 8-bit binary string

def verify_checksum(received_stream, received_checksum):
    total_sum = 0
    
    # Sum the received bytes
    for byte in received_stream:
        total_sum += int(byte, 2)
    
    # Add the received checksum to the total sum
    total_sum += int(received_checksum, 2)
    
    # If the final sum modulo 256 is zero, no error occurred
    return total_sum % 256 == 0

# User input: bit stream (binary, 8 bits per byte)
bit_stream = input("Enter the bit stream (each byte should be multiple of 8 bits, separated by space): ").split()

# Step 1: Calculate the checksum
checksum = calculate_checksum(bit_stream)
print(f"Calculated checksum: {checksum}")

# Step 2: Append the checksum to the bit stream
sent_stream = bit_stream + [checksum]
print(f"Sent bit stream with checksum: {' '.join(sent_stream)}")

# Step 3: Simulate receiving the bit stream (with checksum)
received_stream = input("Enter the received bit stream (with checksum at the end, separated by space): ").split()
received_checksum = received_stream[-1]  # Last byte is the received checksum
received_data = received_stream[:-1]  # Data without the checksum

# Step 4: Verify the checksum
if verify_checksum(received_data, received_checksum):
    print("No errors detected.")
else:
    print("Error detected in the received data.")
