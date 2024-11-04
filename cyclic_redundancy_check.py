def xor(a, b):
    result = []
    for i in range(1, len(b)):  # XOR operation starts from the second bit
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)

def binary_division(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    
    while pick < len(dividend):
        if tmp[0] == '1':
            # Perform XOR between divisor and the portion of the dividend
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            # Perform XOR between 0's (equivalent to just shifting)
            tmp = xor('0' * pick, tmp) + dividend[pick]
        
        pick += 1
    
    # For the last bit comparison
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)
    
    return tmp

def calculate_crc(data, divisor):
    # Append zeros (len(divisor) - 1) to the data for division
    padded_data = data + '0' * (len(divisor) - 1)
    
    # Perform binary division to get the remainder (CRC)
    remainder = binary_division(padded_data, divisor)
    
    return remainder

def check_crc(received_data, divisor):
    # Perform binary division on the received data
    remainder = binary_division(received_data, divisor)
    
    # If remainder is all zeros, no error
    if '1' in remainder:
        return False  # Error detected
    return True  # No error

# User input: Bit stream (data) and the generator polynomial (divisor)
bit_stream = input("Enter the bit stream (binary): ")
divisor = input("Enter the generator polynomial (binary): ")

# Step 1: Calculate CRC
crc_remainder = calculate_crc(bit_stream, divisor)
print(f"CRC remainder: {crc_remainder}")

# Step 2: Append the CRC remainder to the bit stream
sent_data = bit_stream + crc_remainder
print(f"Sent bit stream with CRC: {sent_data}")

# Step 3: Simulate receiving the bit stream (with CRC)
received_data = input("Enter the received bit stream (binary): ")

# Step 4: Check for errors using CRC
if check_crc(received_data, divisor):
    print("No errors detected.")
else:
    print("Error detected in the received data.")
