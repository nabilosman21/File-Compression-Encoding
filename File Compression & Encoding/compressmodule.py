import zlib
import base64

def compress(inputfile, outputfile):
    # Read the contents of the file specified by 'inputfile'
    data = open(inputfile, 'r').read()

    # Convert the read data into bytes using UTF-8 encoding
    data_bytes = bytes(data, 'utf-8')

    # Compress the data using zlib with compression level 9 (highest)
    compressed_data = zlib.compress(data_bytes, 9)

    # Encode the compressed data using base64 encoding
    encoded_data = base64.b64encode(compressed_data)

    # Decode the bytes to a UTF-8 string
    decoded_data = encoded_data.decode('utf-8')

    # Open a new file specified by 'outputfile' in write mode
    compressed_file = open(outputfile, 'w')

    # Write the decoded and encoded data to the 'outputfile'
    compressed_file.write(decoded_data)

    # Close the file to ensure that the changes are saved
    compressed_file.close()


def decompress(inputfile, outputfile):
    # Read the contents of the file specified by 'inputfile'
    file_content = open(inputfile, 'r').read()

    # Encode the file content into bytes using UTF-8 encoding
    encoded_data = file_content.encode('utf-8')

    # Decompress the encoded data using zlib and decode it using base64
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))

    # Decode the decompressed data to a UTF-8 string
    decoded_data = decompressed_data.decode('utf-8')

    # Open a new file specified by 'outputfile' in write mode
    output_file = open(outputfile, 'w')

    # Write the decoded data to the 'outputfile'
    output_file.write(decoded_data)

    # Close the file to ensure that the changes are saved
    output_file.close()
