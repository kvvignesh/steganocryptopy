# https://github.com/kvvignesh/steganocryptopy

#Import the module
from steganocryptopy.steganography import Steganography

key = 'key.key'             # Key file name
input_image = 'input.png'   # Image name
input_file = 'LICENSE'      # File that needs to be encrypted
output_image = 'output.png' # Output image name
output_file = 'output.txt'  # Output file name

# Generate key
Steganography.generate_key(key)

# Encrypt the data and store in the image
encrypted_image = Steganography.encrypt(key, input_image, input_file)
encrypted_image.save(output_image)

# Decrypt the data from image
decrypted_text = Steganography.decrypt(key, output_image)

print(decrypted_text)

Steganography.write_file(output_file, decrypted_text)