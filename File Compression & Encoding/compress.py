import zlib
import base64

# Read the contents of the file named 'demo.txt'
data = open('demo.txt', 'r').read()

# Convert the read data into bytes using UTF-8 encoding
data_bytes = bytes(data, 'utf-8')

# Compress the data using zlib with compression level 9 (highest)
compressed_data = zlib.compress(data_bytes, 9)

# Encode the compressed data using base64 encoding
encoded_data = base64.b64encode(compressed_data)

# Decode the bytes to a UTF-8 string
decoded_data = encoded_data.decode('utf-8')

# Open a new file named 'compressed.txt' in write mode
compressed_file = open('compressed.txt', 'w')

# Write the decoded and encoded data to the 'compressed.txt' file
compressed_file.write(decoded_data)

# Close the 'compressed.txt' file to ensure that the changes are saved
compressed_file.close()

decompressed_data = zlib.decompress(base64.b64decode(compressed_data))


