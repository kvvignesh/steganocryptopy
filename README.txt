# Steganocryptopy - The simplest Python Steganography with crypto out there!

## Usage

In the following paragraphs, I am going to describe how you can get and use Steganocryptopy for your own projects.

###  Getting it

To download steganocryptopy, either fork this github repo or simply use Pypi via pip.
```sh
$ pip install steganocryptopy
```

### Using it

Steganocryptopy was programmed with ease-of-use in mind. First, import Steganography from Steganocryptopy

```Python
from steganocryptopy.steganography import Steganography
```

And you are ready to go!

### Example Code

```Python
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
```

## Steganography

Let’s understand what is steganography, digital images, pixels, and color models.

### What is steganography?

> [Steganography](https://en.wikipedia.org/wiki/Steganography) is the practice of concealing a file, message, image, or video within another file, message, image, or video.

### What is the advantage of steganography over cryptography?
> The advantage of steganography over [cryptography](https://en.wikipedia.org/wiki/Cryptography) alone is that the intended secret message does not attract attention to itself as an object of scrutiny. Plainly visible encrypted messages, no matter how unbreakable they are, arouse interest and may in themselves be incriminating in countries in which [encryption](https://en.wikipedia.org/wiki/Encryption) is illegal.

In other words, steganography is more discreet than cryptography when we want to send a secret information. On the other hand, the hidden message is easier to extract.


**You can check out the result in the following image**:

The below image is the original image used for the encrypting the data and storing into it

<p align="center"><img src="https://github.com/kvvignesh/steganocryptopy/raw/master/input.png" width="400" /> </p>

Below is the image where the data is stored in its pixel

<p align="center"><img src="https://github.com/kvvignesh/steganocryptopy/raw/master/output.png" width="400" /> </p>

As you can see in the image above, you can't find any difference between the both the images

## Limitations
- This program will **ONLY** work with PNG images. JPEG images have a specific compression issue that screws with the encryption algorithim.
- You can only encrypt a specific amount of characters within an image. The exact amount is based off the size of the image (one pixel is dedicated to each character).
