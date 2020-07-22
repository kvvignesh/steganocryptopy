import click
from PIL import Image
from cryptography.fernet import Fernet
import os

class Steganography(object):

    @staticmethod
    def __read_file_as_bytes(file):
        """Reads the file.
        :param file: Input file
        :return: bytes.
        """
        
        file = open(file, 'rb')
        data = file.read()
        file.close()
        return data

    @staticmethod
    def __generate_data(data):
        """Convert encoding data into 8-bit binary form using ASCII value of characters.
        :param data: Text message that needs to be encrypted
        :return: List.
        """
        
        newd = []  
          
        for i in data:
            newd.append(format(ord(i), '08b')) 
        return newd 
                
    @staticmethod
    def __mod_pix(pix, data):
        """Pixels are modified according to the 8-bit binary data and finally returned
        :param pix: Image data
        :param data: Text message that needs to be encrypted
        :return: pixel.
        """

        datalist = Steganography.__generate_data(data) 
        lendata = len(datalist) 
        imdata = iter(pix) 
    
        for i in range(lendata): 
            pix = [value for value in imdata.__next__()[:3] +
                                      imdata.__next__()[:3] +
                                      imdata.__next__()[:3]] 

            for j in range(0, 8): 
                if (datalist[i][j]=='0') and (pix[j]% 2 != 0): 

                    if (pix[j]% 2 != 0): 
                        pix[j] -= 1

                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0): 
                    pix[j] -= 1
 
            if (i == lendata - 1): 
                if (pix[-1] % 2 == 0): 
                    pix[-1] -= 1
            else: 
                if (pix[-1] % 2 != 0): 
                    pix[-1] -= 1
    
            pix = tuple(pix) 
            yield pix[0:3] 
            yield pix[3:6] 
            yield pix[6:9]

    @staticmethod
    def __read_file_as_str(file):
        """Reads the file.
        :param file: Input file
        :return: str.
        """
        
        return open(file, "r").read()

    @staticmethod
    def generate_key(name):
        """Generates Key
        :param name: File name
        """
        key = Fernet.generate_key()
        file = open(name if name is not None and len(name) > 0 else 'key.key', 'wb')
        file.write(key)
        file.close()

    @staticmethod
    def write_file(file, data):
        """Reads the file.
        :param file: Output file name
        :param data: bytes that needs to be written in the file
        """
        
        file_output = open(file, "w")
        file_output.write(data)
        file_output.close()

    @staticmethod
    def encrypt(key, img, file):
        """Encrypt data and merge into the image
        :param key: Key that needs for encryption
        :param img: Image used to store data
        :param file: File which has the text data
        :return: A new encrypted image.
        """

        # Read the file which has the text data
        data = Steganography.__read_file_as_str(file)
    
        # Encrypt the text data using the key
        f = Fernet(Steganography.__read_file_as_bytes(key))
        encrypted = f.encrypt(data.encode())
        hidden_message = encrypted.decode()

        # Read the original image
        image = Image.open(img, 'r')

        w = image.size[0] 
        (x, y) = (0, 0) 

        for pixel in Steganography.__mod_pix(image.getdata(), hidden_message): 

            # Putting modified pixels in the new image 
            image.putpixel((x, y), pixel) 
            if (x == w - 1): 
                x = 0
                y += 1
            else: 
                x += 1
        
        return image

    @staticmethod
    def decrypt(key, img):
        """Extract the data from the image
        :param key: Key used for encryption.
        :param img: The input image.
        :return: Extracted text data from image
        """

        # Read the image and try to restore the message
        image = Image.open(img, 'r') 
      
        data = '' 
        imgdata = iter(image.getdata()) 

        while (True): 
            pixels = [value for value in imgdata.__next__()[:3] +
                                      imgdata.__next__()[:3] +
                                      imgdata.__next__()[:3]] 
            # string of binary data 
            binstr = '' 

            for i in pixels[:8]: 
                if (i % 2 == 0): 
                    binstr += '0'
                else: 
                    binstr += '1'

            data += chr(int(binstr, 2)) 
            if (pixels[-1] % 2 != 0): 
                break

        f = Fernet(Steganography.__read_file_as_bytes(key))
        decrypted = f.decrypt(data.replace("\x00", "").encode())
        return decrypted.decode()


@click.group()
def main():
    pass


@main.command()
@click.option('--name', required=False, type=str, help='Key file name')
def generate_key(name):
    Steganography.generate_key(name)


@main.command()
@click.option('--key', required=True, type=str, help='Key that needs to be used for encryption')
@click.option('--img', required=True, type=str, help='Image that is used to hide data')
@click.option('--file', required=True, type=str, help='Text file which needs to be stored into the image')
@click.option('--output', required=False, type=str, help='Output image name')
def encrypt(key, img, file, output):
    filename, file_extension = os.path.splitext(img)
    encrypted_image = Steganography.encrypt(key, img, file)
    encrypted_image.save(output + file_extension if output is not None and len(output) > 0 else "output" + file_extension)


@main.command()
@click.option('--key', required=True, type=str, help='Key that used during encryption')
@click.option('--img', required=True, type=str, help='Image that has the data stored')
@click.option('--file', required=True, type=str, help='Output file name with extension')
def decrypt(key, img, file):
    decrypted_text = Steganography.decrypt(key, img)
    Steganography.write_file(file, decrypted_text)


if __name__ == '__main__':
    main()
